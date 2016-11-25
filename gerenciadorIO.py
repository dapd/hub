# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
from threading import *

#-------------------------------------------------------------------------------
## @brief      Classe para o GerenciadorIO.
##
##  
##  
class GerenciadorIO(object):

	pinoLedRed=0
	pinoLedGreen=0
	pinoLedBlue=0
	pinoBuzzer=0
	pinoBotao=0

	ledRed = None
	ledGreen = None
	ledBlue = None

	frequencia=0

	informacaoVisual = {}

	mutexBotao = None
	threadBotao = None
	botaoClicked = False

	def __init__(self, pinoLedRed, pinoLedGreen, pinoLedBlue, pinoBuzzer, pinoBotao):
		super(GerenciadorIO, self).__init__()
		
		self.mutexBotao = Lock()
		self.threadBotao = Thread(name="Botao", target=self.setBotao)

		self.pinoLedRed = pinoLedRed
		self.pinoLedGreen = pinoLedGreen
		self.pinoLedBlue = pinoLedBlue
		self.pinoBuzzer = pinoBuzzer
		self.pinoBotao = pinoBotao
		self.frequencia = 50

		GPIO.setmode(GPIO.BOARD)

		GPIO.setup(self.pinoLedRed, GPIO.OUT)
		GPIO.setup(self.pinoLedGreen, GPIO.OUT)
		GPIO.setup(self.pinoLedBlue, GPIO.OUT)
		GPIO.setup(self.pinoBuzzer,GPIO.IN,pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.pinoBotao,GPIO.OUT)
		
		self.LedRed= GPIO.PWM(self.pinoLedRed,self.frequencia)
		self.LedGreen= GPIO.PWM(self.pinoLedGreen,self.frequencia)
		self.LedBlue= GPIO.PWM(self.pinoLedBlue,self.frequencia)

		self.ledRed.start(0)
		self.ledGreen.start(0)
		self.ledBlue.start(0)
		self.threadBotao.start()

	def setBotao(self):
		while True:
			self.mutexBotao.acquire()
			try:
				if GPIO.input(but_pin) == GPIO.HIGH:
					self.botaoClicked = True
				else if 
					self.botaoClicked = False
			finally:
				self.mutexBotao.release()

	def getBotao(self):

		botao = False

		self.mutexBotao.acquire()
			try:
				botao = self.botaoClicked
			finally:
				self.mutexBotao.release()

		return botao

	def mudarStatus(self,status):
		self.status = status
		info = self.informacaoVisual[status]

		if info["ledLigado"] != False:
			self.ligarLed(info["red"], info["green"], infor["blue"])
		else:
			self.desligarLed()

		if info["buzzerLigado"] != False:
			GPIO.output(self.pinoBuzzer,1)
		else:
			GPIO.output(self.pinoBuzzer,0)

	def novoStatus(self, status, red, green, blue, buzzer=False):

		temp = {}

		if red == 0 and green == 0 and blue == 0:
			temp["ledLigado"] = False
		else:
			temp["ledLigado"] = True
		
		temp["red"] = red
		temp["green"] = green
		temp["blue"] = blue
		temp["buzzerLigado"] = buzzer

		self.informacaoVisual[staus] = temp

	def ligarLed(self,red,green,blue):
		self.LedRed.ChangeDutyCycle ((1-red/255.0)*100)
		self.LedGreen.ChangeDutyCycle ((1-green/255.0)*100)
		self.LedBlue.ChangeDutyCycle ((1-blue/255.0)*100)

	def desligarLed(self):
		self.LedRed.ChangeDutyCycle(100)
		self.LedGreen.ChangeDutyCycle(100)
		self.LedBlue.ChangeDutyCycle(100)