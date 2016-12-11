# -*- coding: UTF-8 -*-

import time
import serial
import RPi.GPIO as GPIO

class adaptadorBluetooth:
	
	serialConnection = None
	PIO11  = 15
	SUPPLY = 40 
	AT=False

	def __init__(self):
		self.serialConnection = serial.Serial(
		port='/dev/ttyAMA0',
		baudrate=38400,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
		)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.PIO11, GPIO.OUT)
		#GPIO.setup(self.SUPPLY, GPIO.OUT)

		GPIO.output(self.PIO11,0)
		time.sleep(0.5)
		GPIO.output(self.PIO11,1)
		
		self.serialConnection.write(b'AT+UART=38400,1,0\r\n')
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print (ret," UART")
		#ret = self.serialConnection.readline()
		#ret = ret.decode().strip('\r\n')
		#print (ret," OK")
		#GPIO.output(self.SUPPLY,0)
		self.AT=True

	def modoComunicacao(self):
		if self.AT:
			print('entrou no metodo modoComunicacao')
			#GPIO.output(self.SUPPLY,0)
			time.sleep(0.5)
			GPIO.output(self.PIO11,0)
			time.sleep(0.5)
			#GPIO.output(self.SUPPLY,1)
			
			#if self.serialConnection.baudrate != 9600:
			#	self.serialConnection.write(b'AT+UART=9600,1,0\r\n')
			#	ret = self.serialConnection.readline()
			#	ret = ret.decode().strip('\r\n')
			#	print (ret," OK")
			#	self.serialConnection.setBaudrate(9600)
				
			self.AT=False

	def modoAT(self):
		if self.AT:
			GPIO.output(self.PIO11,0)
			time.sleep(0.5)
			GPIO.output(self.PIO11,1)
			time.sleep(0.5)
			print('ja esta em modo AT')
			return
		print('entrando no modo AT')
		#GPIO.output(self.SUPPLY,0)
		GPIO.output(self.PIO11,0)
		time.sleep(0.5)
		#GPIO.output(self.SUPPLY,1)
		GPIO.output(self.PIO11,1)
		time.sleep(0.5)
		
		self.serialConnection.write(b'AT+UART\r\n')
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print (ret," UART")
		
		if ret == "+UART:9600,1,0":
			self.serialConnection.write(b'AT+UART=38400,1,0\r\n')
			ret = self.serialConnection.readline()
			ret = ret.decode().strip('\r\n')
			print (ret," UART")
			
			self.serialConnection.setBaudrate(38400)
		self.AT=True

	def sendToSerial(self, message, cmd, ok):

		retorno = False

		self.serialConnection.write(message.encode())
		time.sleep(0.2)
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
		self.serialConnection.readline()
		retorno = self.sendToSerial('AT+ROLE=1\r\n', 'Master', 'OK')

		#GPIO.output(self.PIO11,1)#
		#GPIO.output(self.SUPPLY,1)

		return retorno

	def adressing(self, param):
		self.modoAT()
		self.serialConnection.readline()
		message = 'AT+CMODE={}\r\n'.format(param)
		retorno = self.sendToSerial(message, "Adressing", "OK")
		return retorno

	def inicialize(self): #inicializar bluetooth
		self.modoAT()
		self.serialConnection.readline()
		retorno = self.sendToSerial('AT+INIT\r\n', "Inicialize", "OK")
		return retorno

	def  disconnect(self): #disconecta
		self.modoAT()
		self.serialConnection.readline()
		retorno = self.sendToSerial('AT+DISC\r\n', "Disconect", "+DISC:SUCCESS")
		time.sleep(2)
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print(ret,' OK')
		return retorno

	def password(self,pin):  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		self.master()
		self.serialConnection.readline()
		message = 'AT+PSWD={}\r\n'.format(pin)
		retorno = self.sendToSerial(message, "Password", "OK")
		return retorno

	def pair(self,adress):  #PAREAR COM O DISPOSITIVO
		self.modoAT()
		self.serialConnection.readline()
		message = 'AT+PAIR={},2\r\n'.format(adress)
		self.serialConnection.write(message.encode())
		#time.sleep(2)
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		while ret == '':
			ret = self.serialConnection.readline()
			ret = ret.decode().strip('\r\n')
		
		errorMessage = "Comando {0} nao funcionou. Retornou {1}".format('Pair', ret)
		successMessage = "Comando {} OK".format('Pair')

		if(ret == 'OK'):
			print(successMessage)
			retorno = True
		else:
			print(errorMessage)
			retorno = False

		return retorno
		
		#retorno = self.sendToSerial(message, "Pair", "OK")
		
		#return retorno

	def link(self,adress): #CONECTAR AO DISPOSITIVO
		self.modoAT()
		self.serialConnection.readline()
		message = 'AT+LINK={}\r\n'.format(adress)
		self.serialConnection.write(message.encode())
		#time.sleep(2)
		
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		while ret == '':
			ret = self.serialConnection.readline()
			ret = ret.decode().strip('\r\n')
		
		errorMessage = "Comando {0} nao funcionou. Retornou {1}".format('Link', ret)
		successMessage = "Comando {} OK".format('Link')

		if(ret == 'OK'):
			print(successMessage)
			retorno = True
		else:
			print(errorMessage)
			retorno = False

		return retorno
		#retorno = self.sendToSerial(message, "Link", "OK")
		#return retorno
	
	def bind(self,adress):
		self.modoAT()
		self.serialConnection.readline()
		message = 'AT+BIND={}\r\n'.format(adress)
		self.serialConnection.write(message.encode())
		#time.sleep(1)
		
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		while ret == '':
			ret = self.serialConnection.readline()
			ret = ret.decode().strip('\r\n')
		
		errorMessage = "Comando {0} nao funcionou. Retornou {1}".format('Bind', ret)
		successMessage = "Comando {} OK".format('Bind')

		if(ret == 'OK'):
			print(successMessage)
			retorno = True
		else:
			print(errorMessage)
			retorno = False

		return retorno
		
		#retorno = self.sendToSerial(message, 'Bind', 'OK')
		#return retorno
	
	def state(self):
		#self.modoAT()
		self.serialConnection.readline()
		self.serialConnection.write(b'AT+STATE\r\n')
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print (ret,' STATE')
		ret = self.serialConnection.readline()
		ret = ret.decode().strip('\r\n')
		print (ret," OK")
	
	def reset(self): #RESETA
		self.modoAT()
		retorno = self.sendToSerial('AT+RESET\r\n', "Reset", "OK")
		return retorno

class hubParaModulo:
	adaptador=None
	def __init__(self):
		self.adaptador=adaptadorBluetooth()
	def gerenciar(self):
		time.sleep(2)
		self.adaptador.state()
		#self.adaptador.serialConnection.write(b'AT+STATE\r\n')
		#ret = self.adaptador.serialConnection.readline()
		#ret = ret.decode().strip('\r\n')
		#print (ret,' STATE')
		#ret = self.adaptador.serialConnection.readline()
		#ret = ret.decode().strip('\r\n')
		#print (ret," OK")
		
		self.adaptador.inicialize()
		
		#self.adaptador.serialConnection.write(b'AT+INQM=0,5,2\r\n')
		#self.adaptador.serialConnection.write(b'AT+INQM\r\n')
		#time.sleep(2)
		#ret = self.adaptador.serialConnection.readline()
		#ret = ret.decode().strip('\r\n')
		#print (ret,' INQ')
		#ret = self.adaptador.serialConnection.readline()
		#ret = ret.decode().strip('\r\n')
		#print (ret,' INQ')
		
		print('entrando no modo master')
		self.adaptador.master()
		#self.adaptador.adressing(0)
		print('entrando no modo at')
		self.adaptador.modoAT()
		
		print('ESTADO APOS ENTRAR NO MODO MASTER E MODO AT NOVAMENTE')
		self.adaptador.state()
		
		self.adaptador.disconnect()
		print('ESTADO APOS USAR DISCONNECT')
		self.adaptador.state()
		
		self.adaptador.pair('2016,03,042425')
		self.adaptador.bind('2016,03,042425')
		self.adaptador.link('2016,03,042425')
		print('testando conexao')
		#self.adaptador.sendToSerial('AT\r\n','Conexao','OK')
		
		print('Mandando Primeiro Teste')
		self.adaptador.serialConnection.readline()
		self.adaptador.sendToSerial('AT\r\n', 'Teste1','OK')
		
		print('Resposta do Teste')
		#self.adaptador.modoAT()
		self.adaptador.state()
		
		self.adaptador.modoComunicacao()
		self.adaptador.sendToSerial('ping', 'teste', 'OKmod')

Hub=hubParaModulo()
Hub.gerenciar()
