# -*- coding: UTF-8 -*-
from pyrebase import *
from threading import *
import collections

##
## @brief      Class for hub para firebase.
##
## @param      status              O status
## @param      hubID               O id do hub
## @param      appID               O id do app
## @param      firebase            Objeto do firebase
## @param      mensagensRecebidas  As mensagens recebidas
## 
class HubParaFirebase(object):
	status = ""
	hubID = ""
	appID = ""
	firebase = None
	database = None
	gerenciadorMensagensRecebidas = Lock()
	mensagensRecebidas = []

	##
	## @brief      Constructs the object.
	##
	## @param      self   The object
	## @param      hubID  The hub id
	## @param      appID  The application id
	##
	def __init__(self, hubID, appID):
		super(HubParaFirebase, self).__init__()

		config = {
		    "apiKey": "AIzaSyCOWXGPfIStUYJFXSceSnuuZlZGg-zRcEg",
		    "authDomain": "lembrol-be0b6.firebaseapp.com",
		    "databaseURL": "https://lembrol-be0b6.firebaseio.com",
		    "storageBucket": "lembrol-be0b6.appspot.com",
		    "messagingSenderId": "1041897087083",
		    "serviceAccount": "lembrol-be0b6-firebase-adminsdk-1a3ov-55e9f39567.json"
  		}

		self.hubID = hubID
		self.appID = appID
		self.mensagensRecebidas = collections.deque()
		self.firebase = pyrebase.initialize_app(config)
		self.database = self.firebase.database()
		self.stream = self.database.child("msgs_app").child(self.appID).stream(self.receberFirebase, stream_id="mensagens_app")
		self.database.child("hubs").child(self.hubID).update({"status" : "ON"})

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def desconectarFirebase(self):
		modulos = self.database.child("hubs").child(self.hubID).child("modulos").get()
		for modulo in modulos.each():
			self.database.child("hubs").child(self.hubID).child("modulos").update({modulo.key() : "DISCONECTED"})
		self.database.child("hubs").child(self.hubID).update({"status" : "OFF"})
		self.stream.close()

	##
	## @brief      { function_description }
	##
	## @param      self      The object
	## @param      moduloID  The modulo id
	## @param      mensagem  The mensagem
	##
	## @return     { description_of_the_return_value }
	##
	def mensagemAlarme(self, moduloID, mensagem):
		self.database.child("msgs_hub").child(self.hubID).push("alarme:" + moduloID)
		self.database.child("msgs_hub").child(self.hubID).push(mensagem)

	##
	## @brief      { function_description }
	##
	## @param      self      The object
	## @param      moduloID  The modulo id
	##
	## @return     { description_of_the_return_value }
	##
	def mensagemModuloON(self, moduloID):
		self.database.child("hubs").child(self.hubID).child("modulos").update({moduloID : "ON"})
		
	##
	## @brief      { function_description }
	##
	## @param      self      The object
	## @param      mensagem  The mensagem
	##
	## @return     { description_of_the_return_value }
	##
	def receberFirebase(self, mensagem):
		if mensagem["path"] == "/" and mensagem["data"] != None:
			dados = sorted(mensagem["data"].items())
			print(dados)
			for chaves, valor in dados:
				self.gerenciadorMensagensRecebidas.acquire()
				try:
					self.mensagensRecebidas.append(valor)
				finally:
					self.gerenciadorMensagensRecebidas.release()
		elif mensagem["data"] != None:
			self.mensagensRecebidas.append(mensagem["data"])

	##
	## @brief      Gets the ultima mensagem.
	##
	## @param      self  The object
	##
	## @return     The ultima mensagem.
	##
	def getUltimaMensagem(self):
		retorno = None

		self.gerenciadorMensagensRecebidas.acquire()
		try:
			if len(self.mensagensRecebidas) > 0:
				retorno = self.mensagensRecebidas.popleft()
		finally:
			self.gerenciadorMensagensRecebidas.release()
		return retorno

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def apagarMensagensHub(self):
		self.database.child("msgs_hub").remove()

# asd = HubParaFirebase("auhdasudad", "RvCaTZtCPrhjUM92AMA5ReEDfhH2")
# asd.mensagemModuloON("objetos")
# asd.mensagemModuloON("gas")
# asd.mensagemAlarme("objetos", "Objeto 'celular' esta faltando.")
# asd.apagarMensagensHub()
# print(asd.mensagensRecebidas)
# print(asd.getUltimaMensagem())
# print(asd.getUltimaMensagem())
# t = Timer(3, asd.desconectarFirebase)
# t.start()