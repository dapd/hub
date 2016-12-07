# -*- coding: UTF-8 -*-

import time
import serial
import RPi.GPIO as GPIO

class adaptadorBluetooth:
	serialConnection = None
	PIO11  = 0#?
	PIN34  = 0#?
	SUPPLY = 0#? 
  
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
		GPIO.setup(self.PIO11, GPIO.OUT)
		GPIO.setup(self.PIN34, GPIO.OUT)
		GPIO.setup(self.SUPPLY, GPIO.OUT)

		GPIO.output(self.SUPPLY,0)
		GPIO.output(self.PIN34,0)
		GPIO.output(self.PIO11,0)
    
    def modoComunicacao(self):
		GPIO.output(self.SUPPLY,0)
		GPIO.output(self.PIN34,0)
		GPIO.output(self.SUPPLY,1)
		self.serialConnection.setBaudrate(9600)

	def modoAT(self):
		
		GPIO.output(self.PIN34,0)
		GPIO.output(self.SUPPLY,1)
		time.sleep(0.5)
		GPIO.output(self.PIN34,1)
		time.sleep(0.5)
		self.serialConnection.setBaudrate(9600)

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

	def receiveFromSerial(self)
		message=self.serialConnection.readline()
		message=message.decode().strip('\r\n')
		if(not message in ['', '1', '0', 'o']):
			return (True, message)
		else:
			return (False, message)	

	def master(self):  #define o modo de operacao do modulo como MASTER

		GPIO.output(self.PIO11,1)
		GPIO.output(self.SUPPLY,1)
		
		if self.serialConnection.baudrate != 38400:
			self.serialConnection.setBaudrate(38400)
		
		retorno = self.sendToSerial('AT+ROLE=1\r\n', 'Master', 'OK')

   		GPIO.output(self.PIO11,0)
		GPIO.output(self.SUPPLY,1)

		return retorno
	
	def adressing(self, param):
		message = 'AT+CMODE={}\r\n'.format(param)
		retorno = self.sendToSerial(message, "Adressing", "OK")
		return retorno
     
	def inicialize(self): #inicializar bluetooth
		retorno = self.sendToSerial('AT+INIT\r\n', "Inicialize", "OK")
    	return retorno

	def  disconnect(self): #disconecta
		retorno = self.sendToSerial('AT+DISC\r\n', "Disconect", "+DISC:SUCESS")
    	return retorno

	def password(self,pin):  #define a senha do modulo mestre, que deve ser a mesma do modulo slave/escravo
		message = 'AT+PSWD={}\r\n'.format(pin)
		retorno = self.sendToSerial(message, "Password", "OK")
    	return retorno

	def pair(self,adress):  #PAREAR COM O DISPOSITIVO
		message = 'AT+PAIR={},10\r\n'.format(adress)
		retorno = self.sendToSerial(message, "Pair", "OK")
    	return retorno

	def link(self,adress): #CONECTAR AO DISPOSITIVO
		message = 'AT+LINK={}\r\n'.format(adress)
		retorno = self.sendToSerial(message, "Link", "OK")
    	return retorno
	
	def reset(self): #RESETA
		retorno = self.sendToSerial('AT+RESET\r\n', "Reset", "OK")
    	return retorno

class hubParaModulo:
  
  def __init__(self):
