# -*- coding: UTF-8 -*-

import time
import serial
import RPi.GPIO as GPIO

class adaptadorBluetooth:
	
	serialConnection = None
	PIO11  = 15
	SUPPLY = 40 
	AT=False
	cBaud=9600
	cBaudB='9600,1,0'
	aBaud=38400
	aBaudB='38400,1,0'

	def __init__(self):
		self.serialConnection = serial.Serial(
		port='/dev/ttyAMA0',
		baudrate=self.aBaud,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
		)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.PIO11, GPIO.OUT)
		GPIO.setup(self.SUPPLY, GPIO.OUT)

		GPIO.output(self.PIO11,0)
		GPIO.output(self.SUPPLY,1)
		self.AT=False
		
		self.changeBaudBlue(self.cBaudB)

	def modoComunicacao(self):
		if self.AT:
			self.AT=False
			#print('entrou no metodo modoComunicacao')
			#GPIO.output(self.SUPPLY,0)
			GPIO.output(self.PIO11,0)
			time.sleep(1)
			#GPIO.output(self.SUPPLY,1)
			self.changeBaudBlue(self.cBaudB)
			self.serialConnection.setBaudrate(self.cBaud)
			

	def modoAT(self):
		if self.AT:
			#print('ja esta em modo AT')
			return
		else:
			self.AT=True
			#print('entrando no modo AT')
# 			GPIO.output(self.SUPPLY,0)
# 			GPIO.output(self.PIO11,0)
# 			time.sleep(0.3)
# 			GPIO.output(self.SUPPLY,1)
# 			GPIO.output(self.PIO11,0)
# 			time.sleep(0.3)
			GPIO.output(self.PIO11,1)
			time.sleep(1)
			self.changeBaudBlue(self.aBaudB)
			self.serialConnection.setBaudrate(self.aBaud)
			
	def sendToSerial(self, message, cmd, ok):

		retorno = False

		self.serialConnection.write(message.encode())
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')

		errorMessage = "Comando {0} nao funcionou. Retornou {1}".format(cmd, ret)
		successMessage = "Comando {} OK".format(cmd)

		if(ret == ok):
			print(successMessage)
			retorno = True
		else:
			print(errorMessage)
			retorno = False

		return retorno

	def receiveFromSerial(self):
		message=self.serialConnection.readline()
		message=message.decode().strip('\r\n')
		if(not message in ['', '1', '0', 'o']):
			return (True, message)
		else:
			return (False, message)	

	def master(self):  #define o modo de operacao do modulo como MASTER
		self.modoAT()
		retorno = self.sendToSerial('AT+ROLE=1\r\n', 'Master', 'OK')
		return retorno

	def adressing(self, param):
		self.modoAT()
		message = 'AT+CMODE={}\r\n'.format(param)
		retorno = self.sendToSerial(message, "Adressing", "OK")
		return retorno
	
	def inicialize(self): #inicializar bluetooth
		self.modoAT()
		retorno = self.sendToSerial('AT+INIT\r\n', "Inicialize", "OK")
		return retorno

	def  disconnect(self): #disconecta
		self.modoAT()
		retorno = self.sendToSerial('AT+DISC\r\n', "Disconect", "+DISC:SUCCESS")
		self.serialConnection.readline()
		
		return retorno

	def password(self,pin):  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		self.master()
		message = 'AT+PSWD={}\r\n'.format(pin)
		retorno = self.sendToSerial(message, "Password", "OK")
		return retorno

	def pair(self,adress):  #PAREAR COM O DISPOSITIVO
		self.modoAT()
		message = 'AT+PAIR={},5\r\n'.format(adress)
		time.sleep(5)
		retorno = self.sendToSerial(message, "Pair", "OK")
		return retorno

	def link(self,adress): #CONECTAR AO DISPOSITIVO
		self.modoAT()
		message = 'AT+LINK={}\r\n'.format(adress)
		retorno = self.sendToSerial(message, "Link", "OK")
		return retorno
	
	def reset(self): #RESETA
		self.modoAT()
		retorno = self.sendToSerial('AT+RESET\r\n', "Reset", "OK")
		return retorno
	
	def getBaudBlue(self):
		self.modoAT()
		self.serialConnection.write(b'AT+UART\r\n')
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		ret= ret.strip('+UART:')
		print( ret, ' getBaudBlue')
		
		ret2 = self.serialConnection.readline()
		ret2 = ret2.decode().strip('\r\n')
		print( ret2, ' getBaud2Blue')
		
		return ret
		
	def compareBaud(self,baud1,baud2):
		return baud1==baud2
	
	def changeBaudBlue(self,newBaud):
		baud2=self.getBaudBlue()
		
		if self.compareBaud(newBaud,baud2):
			print('FOI IGUAL')
			pass
		else:	
			message = 'AT+UART={}\r\n'.format(newBaud)
			retorno = self.sendToSerial(message, "changeBaudBlue", "OK")
			return retorno	
		
class hubParaModulo:
	adaptador=None
	def __init__(self):
		self.adaptador=adaptadorBluetooth()
	def gerenciar(self):
		
# 		self.adaptador.modoAT()
# 		self.adaptador.serialConnection.write(b'AT+STATE\r\n')
# 		ret = self.adaptador.serialConnection.readline()
# 		ret = ret.decode().strip('\r\n')
# 		print (ret,' STATE')
		
# 		ret = self.adaptador.serialConnection.readline()
# 		ret = ret.decode().strip('\r\n')
# 		print (ret," OK")
		
		self.adaptador.inicialize()
		
		print('entrando no modo master')
		self.adaptador.master()
		print('entrando no modo at')
		#self.adaptador.modoAT()
		
		
		
# 		self.adaptador.serialConnection.write(b'AT+STATE\r\n')
# 		print('ESTADO APOS ENTRAR NO MODO MASTER E MODO AT NOVAMENTE')
# 		ret = self.adaptador.serialConnection.readline()
# 		ret = ret.decode().strip('\r\n')
# 		print (ret,' STATE')
# 		ret = self.adaptador.serialConnection.readline()
# 		ret = ret.decode().strip('\r\n')
# 		print (ret," OK")
		
		self.adaptador.pair('2016,03,042425')
		time.sleep(5)
		self.adaptador.link('2016,03,042425')
		time.sleep(5)
		print('testando conexao')	
		
		print(self.adaptador.getBaudBlue(), 'BAUD BLUETOOTH')
		print( self.adaptador.serialConnection.getBaudrate() , 'BAUD HW' )
		
		
		self.adaptador.serialConnection.write(b'AT+STATE\r\n')
		print('VER ESTADO CoNEXAO')
		ret = self.adaptador.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print (ret,' STATE')
		ret = self.adaptador.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print (ret," OK")
		
		
		self.adaptador.modoComunicacao()
		print( self.adaptador.serialConnection.getBaudrate() , 'BAUD HW com' )
		self.adaptador.sendToSerial('ping', 'teste', 'OKmod')
		#self.adaptador.disconnect()
		
	def teste(self):
		print (self.adaptador.serialConnection.getBaudrate(), 'HW baud')
		
		baudAtual=self.adaptador.getBaudBlue()
		print(baudAtual,' baud atual BLUE')
		
		ret=self.adaptador.compareBaud('9600,1,0',baudAtual)
		print(ret,' == False')
		
		self.adaptador.changeBaudBlue('9600,1,0')
		
		print('vAI DAR ERRADO?? MUDOU P 9600')
		
		baudAtual=self.adaptador.getBaudBlue()
		print(baudAtual,' baud atual BLUE')
		
		ret=self.adaptador.compareBaud('9600,1,0',baudAtual)
		print(ret,' == True')

		
		self.adaptador.changeBaudBlue('38400,1,0')
		
		print('---------------------------------------------------------------------------------')
		self.adaptador.serialConnection.setBaudrate(9600)
		print (self.adaptador.serialConnection.getBaudrate(), 'HW baud2')
		
		baudAtual=self.adaptador.getBaudBlue()
		print(baudAtual,' baud atual')
		
		ret=self.adaptador.compareBaud('9600,1,0',baudAtual)
		print(ret,' == False')
		
		self.adaptador.changeBaudBlue('9600,1,0')
		
		baudAtual=self.adaptador.getBaudBlue()
		print(baudAtual,' baud atual')
		
		ret=self.adaptador.compareBaud('9600,1,0',baudAtual)
		print(ret,' == True')

				
					   
Hub=hubParaModulo()
Hub.gerenciar()
