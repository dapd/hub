# -*- coding: UTF-8 -*-

import time
import serial

class HubParaModulo(object):
	
	serialConnection = None

	def __init__(self):
		super(HubParaModulo, self).__init__()
		self.serialConnection = serial.Serial(
		  port='/dev/ttyAMA0',
		  baudrate=38400,
		  parity=serial.PARITY_NONE,
		  stopbits=serial.STOPBITS_ONE,
		  bytesize=serial.EIGHTBITS,
		  timeout=1
		)
	

	def parear(self,idt,pin=1234):
		#print('Pressione o botao do bluetooth')
		time.sleep(5)

		# self.serialConnection.write(b'AT+ORGL\r\n')
		# x=self.serialConnection.readline()
		# print(x.decode().strip('\r\n'))
		# if(x.decode().strip('\r\n') != 'OK'):
		# 	print('Comando AT nao funcionou')
		#	return False
		
		self.serialConnection.write(b'AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 1')
			return False
	
		
		self.serialConnection.write(b'AT+CMODE=1\r\n') #Permite a conexao a qualquer endereco
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 2')
			return False
		#print(x)
		
		message = 'AT+PSWD={}\r\n'.format(pin)
		self.serialConnection.write(message.encode())  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 3')
			return False
		#print(x)
		
		self.serialConnection.write(b'AT+INIT\r\n')
		
		self.serialConnection.write(b'AT+INQM=0,5,10\r\n')
		
		message2 = 'AT+PAIR={},10\r\n'.format(idt)
		self.serialConnection.write(message2.encode())  #PAREAR COM O DISPOSITIVO
		#time.sleep(5)
		x=self.serialConnection.readline()
		#print(x)
		
		message3 = 'AT+LINK={}\r\n'.format(idt)
		self.serialConnection.write(message3.encode())  #CONECTAR AO DISPOSITIVO
		x=self.serialConnection.readline()
		#print(x)
		
		self.serialConnection.write(b'AT+ROLE=0\r\n') #define o modo de operacao do modulo como SLAVE
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 4')
			return False
		#print(x)
		
		#self.serialConnection.write(b'OK\r\n')
		#time.sleep(1)
		#x=self.serialConnection.readline()
		#if(x!=self.OK):
			#print('Pareamento falhou')
			#return False
		
		return True
	
	def conectarModulo(self, modulo):
		self.serialConnection.write(b'AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 5')
			#return False
		
		message = 'AT+LINK={}\r\n'.format(modulo)
		self.serialConnection.write(message.encode())  #CONECTAR AO DISPOSITIVO
		
		self.serialConnection.write(b'AT+ROLE=0\r\n')
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 6')
			#return False
		return True

	def receberModulo(self):
		x=self.serialConnection.readline()
		#return x
		if(x and (x[0]!=48 | x[0]!=49)):
			return (False, x.decode())
		else:
			return (True, x.decode())

	def mandarModulo(self, mensagem):
		message2 = '{}'.format(mensagem)
		self.serialConnection.write(message2.encode())
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 7')
			#return False
		return True
