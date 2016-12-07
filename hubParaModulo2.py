# -*- coding: UTF-8 -*-

import time
import serial
import RPi.GPIO as GPIO

class adaptadorBluetooth:
  serialConnection = None
	pinoBT = 15
  
  def __init__(self):
      self.serialConnection = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
      )
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.pinoBT, GPIO.OUT)
      GPIO.output(self.pinoBT,0)
      
  def master(self):  #define o modo de operacao do modulo como MASTER
    GPIO.output(self.pinoBT,1)
		time.sleep(0.5)
		self.serialConnection.write(b'AT+ROLE=1\r\n')
		x=self.serialConnection.readline()
    GPIO.output(self.pinoBT,0)
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando master nao funcionou')
    return False
   
  
  def adressing(self):
    self.serialConnection.write(b'AT+CMODE=1\r\n') #Permite a conexao a qualquer endereco
		x=self.serialConnection.readline()
		print(x);
		print('2')
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando adressing nao funcionou')
			#GPIO.output(self.pinoBT,0)
			return False
     
  def inicialize(self): #inicializar bluetooth
    self.serialConnection.write(b'AT+INIT\r\n')
		x=self.serialConnection.readline()
		if x=='FAIL\r\n':
      print('Comando inicialize nao funcionou')
      return False
    
  def  disconnect(self): #disconecta
    self.serialConnection.write(b'AT+DISC\r\n')
		x=self.serialConnection.readline()
		print(x);
		if(x.decode().strip('\r\n') != '+DISC:SUCESS'):
			print('Comando disconnect nao funcionou')
			#GPIO.output(self.pinoBT,0)
			return False
    
  def password(self,pin):  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
    message = 'AT+PSWD={}\r\n'.format(pin)
		self.serialConnection.write(message.encode()) 
		x=self.serialConnection.readline()
		print(x)
		print('3')
		if(x.decode().strip('\r\n') != 'OK'):
			print('Comando password nao funcionou')
			#GPIO.output(self.pinoBT,0)
			return False
    
  def pair(self,adress):
    
    
		
		
class hubParaModulo:
  
  def __init__(self):
