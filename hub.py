# -*- coding: UTF-8 -*-

from gerenciadorIO import *
from hubParaFirebase import *
from hubParaModulo2 import *

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
		self.factoryID = "ahuha"
		self.gerenciadorIO = GerenciadorIO(self.pinoLedRed, self.pinoLedGreen, self.pinoLedBlue, self.pinoBuzzer, self.pinoBotao)
		self.hubParaModulo = hubParaModulo()
		self.hubParaFirebase = HubParaFirebase(self.factoryID)

		self.hubParaFirebase.getIDBluetooth()
		a = self.hubParaFirebase.idsBluetooth[1];
		self.hubParaModulo.gerenciar(a[2])

		if self.hubParaModulo.adaptador.sendToSerial('ping', 'ping', 'OKmod'):
			self.hubParaFirebase.mensagemModuloStatus(a[0])
		else:
			self.hubParaFirebase.mensagemModuloStatus(a[0], False)
		# for modulos in self.hubParaFirebase.idsBluetooth:
		# 	print(modulos[2])
		# 	if self.hubParaModulo.parear(modulos[2]) != False:
		# 		self.pareados.append(modulos)
		# 		self.hubParaFirebase.mensagemModuloStatus(modulos[0])
		# 	else:
		# 		self.hubParaFirebase.mensagemModuloStatus(modulos[0], False)

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
					self.gerenciadorIO.mutexBotao.Lock()
					try:
						self.gerenciadorIO.botaoClicked = False
					finally:
						self.gerenciadorIO.mutexBotao.release()
					self.gerenciadorIO.GPIO.output(self.pinoBuzzer,0)
					

			# # Verifica a coneccao dos modulos
			# self.hubParaFirebase.getIDBluetooth()
			# for modulos in self.hubParaFirebase.idsBluetooth:
			# 	#print (modulos[2])
			# 		if  not modulos in self.pareados:
			# 			if self.hubParaModulo.parear(modulos[2]) != False:
			# 				self.pareados.append(modulos)
			# 				self.hubParaFirebase.mensagemModuloStatus(modulos[0])
			# 			#else:
			# 			#	print("pingando...")
			# 			#	self.hubParaModulo.conectarModulo(modulos[2])
			# 			#	self.hubParaModulo.mandarModulo("ping")
			# 			#	(x, msg) = self.hubParaModulo.receberModulo()
			# 			#	if msg == "OK":
			# 			#		self.pareados.append(modulos)
			# 			#		self.hubParaFirebase.mensagemModuloStatus(modulos[0])
			# 		else:
			# 			print(self.pareados)
			# 			print(modulos)
			# 			print("pingando...")
			# 			self.hubParaModulo.conectarModulo(modulos[2])
						
			# 			#(x, msg) = self.hubParaModulo.receberModulo()
			# 			#print(msg,x)
			# 			if not self.hubParaModulo.mandarModulo("ping"):
			# 				self.pareados = [i for i  in self.pareados if i != modulos]
			# 				self.hubParaFirebase.mensagemModuloStatus(modulos[0], False)

			# # recebe e trata as mensagens
			# print(self.pareados)
			# for modulo in self.pareados:
			# 	if self.hubParaModulo.conectarModulo(modulo[2]) == True:
			# 		self.hubParaModulo.mandarModulo("ping")
			# 		(x, msg) = self.hubParaModulo.receberModulo()
			# 		print(msg)
			# 		if not x:
			# 			#self.hubParaModulo.mandarModulo("falha\r\n")
			# 			pass
			# 		else:
			# 			mensagem = msg.split(":")
			# 			if mensagem[0] == "1Alerta" and mensagem[1] == "gas":
			# 				self.hubParaFirebase.mensagemAlarme(modulo[0], mensagem[1])
			# 				self.gerenciadorIO.mudarStatus("alarme")
			# 				self.status = "alarme"
			# 			elif mensagem[1] == "objetos":
			# 				self.hubParaFirebase.mensagemAlarme(modulo[0], mensagem[1])
			
			if not self.hubParaModulo.adaptador.sendToSerial('ping', 'ping', 'OKmod'):
				#self.hubParaModulo.mandarModulo("falha\r\n")
				pass
			else:
				(x, msg) = self.hubParaModulo.adaptador.receiveFromSerial()
				if msg!='':
					mensagem = msg.split(":")
					print(mensagem)
					if mensagem[0] == "1Alerta" and mensagem[1] == "gas":
						self.hubParaFirebase.mensagemAlarme('X81k9AeCPFQh', mensagem[1])
						self.gerenciadorIO.mudarStatus("alarme")
						self.status = "alarme"
					elif mensagem[1] == "objetos":
						print("OBJETOS VINDO")
						query = self.hubParaFirebase.database.child("modulos").child("X81k9AeCPFQh").child("componentes").get()
						vals = query.val()
						for asd in vals.keys():
							self.hubParaFirebase.database.child("modulos").child("X81k9AeCPFQh").child("componentes").child(asd).update({"status": "Ausente"})
						messages = mensagem[0].split(",")
						for memb in messages:
							self.hubParaFirebase.enviarObjeto(memb, 'j7TEhFJVTx7H')
						
						query = self.hubParaFirebase.database.child("modulos").child("X81k9AeCPFQh").child("componentes").get()
						vals = query.vals()
						for asd in vals:
							if vals["status"] == "Ausente":
								self.hubParaFirebase.mensagemAlarme('X81k9AeCPFQh', asd["nome"])
								self.gerenciadorIO.mudarStatus("alarme")
								self.status = "alarme"
			msg = self.hubParaFirebase.getUltimaMensagem()
			while msg != None:
				if msg == "ativaralerta":
					self.status = "alarme"
					self.gerenciadorIO.mudarStatus("alarme")
				elif msg == "desativaralerta":
					self.status = "normal"
					self.gerenciadorIO.mudarStatus("normal")
				msg = self.hubParaFirebase.getUltimaMensagem()


hubs = Hub()
while True:
	hubs.loopPrincipal()
