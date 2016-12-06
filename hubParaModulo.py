# -*- coding: UTF-8 -*-

##
## @brief      Class for hub para modulo.
##
import time
import serial

class HubParaModulo(object):
	
	status = ""
	ok='OK\r\n'

	##
	## @brief      Constructs the object.
	##
	## @param      self  The object
	## @param      arg   The argument
	##
	def __init__(self, arg):
		super(HubParaModulo, self).__init__()
		self.arg = arg
		ser = serial.Serial(
		  port='/dev/ttyAMA0',
		  baudrate=9600,
		  parity=serial.PARITY_NONE,
		  stopbits=serial.STOPBITS_ONE,
		  bytesize=serial.EIGHTBITS,
		  timeout=1
		)
	
	##
	## @brief      { function_description }
	##
	## @param      modulo  The modulo
	##
	## @return     { description_of_the_return_value }
	##
	def parear(self,idt,pin=1234):
		#print('Pressione o botao do bluetooth')
		time.sleep(5)
		
		ser.write('AT+ORGL\r\n')
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		
		ser.write('AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		ser.write('AT+CMODE=1\r\n') #Permite a conexao a qualquer endereco
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		ser.write('AT+PSWD=%d\r\n'%(pin))  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		ser.write('AT+INIT\r\n')
		
		ser.write('AT+INQM=0,5,10\r\n')
		
		ser.write('AT+PAIR=%s,10\r\n'%(idt))  #PAREAR COM O DISPOSITIVO
		time.sleep(5)
		#x=ser.readline()
		#print(x)
		
		ser.write('AT+LINK=%s\r\n'%(idt))  #CONECTAR AO DISPOSITIVO
		#x=ser.readline()
		#print(x)
		
		ser.write('AT+ROLE=0\r\n') #define o modo de operacao do modulo como SLAVE
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		#ser.write('OK')
		#time.sleep(1)
		#x=ser.readline()
		#if(x!=ok):
			#print('Pareamento falhou')
			#return False
		
		return True
	
	def conectarModulo(modulo):
		ser.write('AT+ROLE=1\r\n') #define o modo de operacao do modulo como MASTER
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		
		ser.write('AT+LINK=%s\r\n'%(modulo))  #CONECTAR AO DISPOSITIVO
		
		ser.write('AT+ROLE=0\r\n') #define o modo de operacao do modulo como SLAVE
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		return True

	##
	## @brief      { function_description }
	##
	## @return     { description_of_the_return_value }
	##
	def receberModulo():
		x=ser.readline()
		if(x[0]!=48 | x[0]!=49):
			return (False,x)
		else:
			return (True,x)

	##
	## @brief      { function_description }
	##
	## @param      mensagem  The mensagem
	##
	## @return     { description_of_the_return_value }
	##
	def mandarModulo(mensagem):
		ser.write(mensagem)
		x=ser.readline()
		if(x!=ok):
			print('Comando AT nao funcionou')
			return False
		#print(x)
		return True
