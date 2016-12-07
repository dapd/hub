# -*- coding: UTF-8 -*-

import time
import serial
import RPi.GPIO as GPIO

class HubParaModulo(object):
	
	serialConnection = None
	pinoBT = 15
	
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
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pinoBT, GPIO.OUT)
		GPIO.output(self.pinoBT,0)
	
	def parear(self,idt,pin=1234):
		GPIO.output(self.pinoBT,1)
		time.sleep(0.5)
		self.serialConnection.write(b'AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=self.serialConnection.readline()
		print(x)
		print('1')
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou')
			#GPIO.output(self.pinoBT,0)
			#return False
		
		self.serialConnection.write(b'AT+CMODE=1\r\n') #Permite a conexao a qualquer endereco
		x=self.serialConnection.readline()
		print(x);
		print('2')
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 2')
			#GPIO.output(self.pinoBT,0)
			#return False
		
		self.serialConnection.write(b'AT+INIT\r\n')
		x=self.serialConnection.readline()
		print(x);
		
		self.serialConnection.write(b'AT+DISC\r\n')
		x=self.serialConnection.readline()
		print(x);
		#if(x.decode().strip('\r\n') != 'OK'):
			#print('Comando AT nao funcionou 1')
			#GPIO.output(self.pinoBT,0)
			#return False
		
		message = 'AT+PSWD={}\r\n'.format(pin)
		self.serialConnection.write(message.encode())  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		x=self.serialConnection.readline()
		print(x)
		print('3')
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 3')
			#GPIO.output(self.pinoBT,0)
			#return False
		#print(x)
		
		self.serialConnection.write(b'AT+INQM=0,5,10\r\n')
		
		message2 = 'AT+PAIR={},10\r\n'.format(idt)
		self.serialConnection.write(message2.encode())  #PAREAR COM O DISPOSITIVO
		x=self.serialConnection.readline()
		#print(x)
		
		#message3 = 'AT+LINK={}\r\n'.format(idt)
		#self.serialConnection.write(message3.encode())  #CONECTAR AO DISPOSITIVO
		
		self.serialConnection.write(b'AT+RESET\r\n') #define o modo de operacao do modulo como SLAVE
		x=self.serialConnection.readline()
		print(x)
		print('4')
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 4')
			#GPIO.output(self.pinoBT,0)
			#return False
		
		GPIO.output(self.pinoBT,0)
		return True
	
	def conectarModulo(self, modulo):
		GPIO.output(self.pinoBT,1)
		
		self.serialConnection.write(b'AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando AT nao funcionou 5')
			#GPIO.output(self.pinoBT,0)
			#return False
		
		self.serialConnection.write(b'AT+DISC\r\n')
		x=self.serialConnection.readline()
		#if(x.decode().strip('\r\n') != 'OK'):
		#	print('Comando AT nao funcionou')
		#	GPIO.output(self.pinoBT,0)
		#	return False
		
		message = 'AT+LINK={}\r\n'.format(modulo)
		self.serialConnection.write(message.encode())  #CONECTAR AO DISPOSITIVO
		
		GPIO.output(self.pinoBT,0)
		return True

	def receberModulo(self):
		msg=self.serialConnection.readline()
		print(msg)
		msg=msg.decode().strip('\r\n')
		print(msg)
		print('aqui î')
		if(msg and (ord(msg[0])!=48 | ord(msg[0])!=49 | ord(msg[0])!=32 | ord(msg[0])!=79)):
			return (True, msg)
		else:
			return (False, msg)

	def mandarModulo(self, mensagem):
		message2 = '{}'.format(mensagem)
		self.serialConnection.write(message2.encode())
		x=self.serialConnection.readline()
		if(x.decode().strip('\r\n') != 'OK'):
			print('Mandar modulo falhou')
			#return False
		return True
