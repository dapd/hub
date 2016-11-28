# -*- coding: UTF-8 -*-

import time
import serial

class HubParaModulo(object):
	
	serialConnection = None
	ok='ok\r\n'

	def __init__(self):
		super(HubParaModulo, self).__init__()
		self.serialConnection = serial.Serial(
		  port='/dev/ttyAMA0',
		  baudrate=9600,
		  parity=serial.PARITY_NONE,
		  stopbits=serial.STOPBITS_ONE,
		  bytesize=serial.EIGHTBITS,
		  timeout=1
		)
	

	def parear(self,idt,pin):
		#print('Pressione o botao do bluetooth')
		time.sleep(5)
		
		self.serialConnection.write('AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=self.serialConnection.readline()
		if(x!=selfok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		self.serialConnection.write('AT+CMODE=1\r\n') #Permite a conexao a qualquer endereco
		x=self.serialConnection.readline()
		if(x!=self.ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		self.serialConnection.write('AT+PSWD=%d\r\n'%(pin))  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		x=self.serialConnection.readline()
		if(x!=self.ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		self.serialConnection.write('AT+PAIR=%s,10\r\n'%(idt))  #PAREAR COM O DISPOSITIVO
		#time.sleep(5)
		x=self.serialConnection.readline()
		#print(x)
		
		self.serialConnection.write('AT+LINK=%s\r\n'%(idt))  #CONECTAR AO DISPOSITIVO
		x=self.serialConnection.readline()
		#print(x)
		
		self.serialConnection.write('AT+ROLE=0\r\n') #define o modo de operacao do modulo como SLAVE
		x=self.serialConnection.readline()
		if(x!=self.ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		self.serialConnection.write('OK\r\n')
		time.sleep(1)
		#x=self.serialConnection.readline()
		#if(x!=self.ok):
			#print('Pareamento falhou')
			#return False
		
		return True
	
	def conectarModulo(modulo):
		self.serialConnection.write('AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=self.serialConnection.readline()
		if(x!=self.ok):
			print('Comando AT nao funcionou')
			return False
		
		self.serialConnection.write('AT+LINK=%s\r\n'%(modulo))  #CONECTAR AO DISPOSITIVO
		
		self.serialConnection.write('AT+ROLE=0\r\n')
		x=self.serialConnection.readline()
		if(x!=self.ok):
			print('Comando AT nao funcionou')
			return False
		return True

	def receberModulo():
		x=self.serialConnection.readline()
		#return x
		if(x[0]!=48 | x[0]!=49):
			return (False,x)
		else:
			return (True,x)

	def mandarModulo(mensagem):
		self.serialConnection.write(mensagem)
		x=self.serialConnection.readline()
		if(x!=self.ok):
			print('Comando AT nao funcionou')
			return False
		return True
