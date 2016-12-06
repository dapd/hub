# -*- coding: UTF-8 -*-

from gerenciadorIO import *
from hubParaFirebase import *
from hubParaModulo import *

#-------------------------------------------------------------------------------
## @brief      Classe para o HUB.
##
##
##
class Hub(object):

	status = ""
	factoryID = ""
	pareados = []
	ledManager = None
	hubParaModulo = None
	hubParaFirebase = None
	adaptadorBluetooth = None
	gerenciadorIO = None

	pinoLedRed=3
	pinoLedGreen=5
	pinoLedBlue=7
	pinoBuzzer=13
	pinoBotao=11

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o HUB.
	##
	##             
	##
	def __init__(self):
		super(Hub, self).__init__()
		self.status = "STARTING"
		self.factoryID = "C0Oj2DnuuU2Y"
		self.gerenciadorIO = GerenciadorIO(self.pinoLedRed, self.pinoLedGreen, self.pinoLedBlue, self.pinoBuzzer, self.pinoBotao)
		self.hubParaModulo = HubParaModulo()
		self.hubParaFirebase = HubParaFirebase(self.factoryID)

		self.hubParaFirebase.getIDBluetooth()
		for modulos in self.hubParaFirebase.idsBluetooth:
			print(modulos[2])
			if self.hubParaModulo.parear(modulos[2]) != False:
				self.pareados.append(modulos)
				self.hubParaFirebase.mensagemModuloStatus(modulos[0])
			else:
				self.hubParaFirebase.mensagemModuloStatus(modulos[0], False)

		self.gerenciadorIO.novoStatus("alarme", 255, 0, 0, True)
		self.gerenciadorIO.novoStatus("normal", 0, 255, 0)
		self.gerenciadorIO.novoStatus("sem dono", 255, 255, 0)
	#------------------------------------------------------------------------------
	## @brief      Esse é o loop principal do HUB, onde será implementada sua 
	##  máquina de estados. 
	##
	##
	##
	def loopPrincipal(self):
		if not self.hubParaFirebase.haDono():
			self.hubParaFirebase.atualizarDono()
		
		if not self.hubParaFirebase.haDono():
			self.gerenciadorIO.mudarStatus("sem dono")
			self.status = "sem dono"
		else:
			if self.status != "alarme":
				self.status = "normal"
				self.gerenciadorIO.mudarStatus("normal")
			else:
				if self.gerenciadorIO.getBotao == True:
					self.gerenciadorIO.mudarStatus("normal")

			# Verifica a coneccao dos modulos
			self.hubParaFirebase.getIDBluetooth()
			for modulos in self.hubParaFirebase.idsBluetooth:
				#print (modulos[2])
				if not modulos in self.pareados:
					if  self.hubParaModulo.parear(modulos[2]) != False:
						self.pareados.append(modulos)
						self.hubParaFirebase.mensagemModuloStatus(modulos[0])
					else:
						if modulos in self.pareados:
							self.hubParaModulo.mandarModulo("ping")
							(x, msg) = self.hubParaModulo.receberModulo()
							if msg != "OK":
								self.pareados = [i for i  in self.pareados if i != modulos]
								self.hubParaFirebase.mensagemModuloStatus(modulos[0], False)

			print(self.pareados)

			# recebe e trata as mensagens
			# for modulo in self.pareados:
			# 	if self.hubParaModulo.conectarModulo(modulo[2]) == True:
			# 		(x, msg) = self.hubParaModulo.receberModulo()
			# 		if not x:
			# 			self.hubParaModulo.mandarModulo("falha\r\n")
			# 		else:
			# 			mensagem = msg.split(":")
			# 			if msg[0] == "alarme":
			# 				self.hubParaFirebase.mensagemAlarme(modulo[0], msg[1])
			# 				self.gerenciadorIO.mudarStatus("alarme")
			# 				self.status = "alarme"



hubs = Hub()
hubs.loopPrincipal()
