# -*- coding: UTF-8 -*-
from pyrebase import *
from threading import *
import collections

##
## @brief      Esta classe é responsável pela comunicação entre o HUB e o banco de dados firebase.
##  
##  Este módulo provem funções básicas de comunição, entretando não é responsável
## pela lógica usada de acordo com as mensagens.
##
## @param      hubID               O id do hub cadastrado no banco de dados firebase
## @param      appID               O id do app/do usuário do app no banco de dados firebase
## @param      firebase            Objeto da classe pyrebase, responsável pela conexão com o servidor
## @param      database            Objeto da classe pyrebase, responsável por recuperar dados do banco
##                                 de dados firebase.
## @param      mensagensRecebidas  As mensagens recebidas pelo módulo, guardadas como uma lista ordenada.
## 
class HubParaFirebase(object):
	hubID = ""
	appID = ""
	firebase = None
	database = None
	gerenciadorMensagensRecebidas = None
	mensagensRecebidas = None

	##
	## @brief      Constructs the object.
	##
	## @param      self   O objeto
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

		self.gerenciadorMensagensRecebidas = Lock()
		if self.gerenciadorMensagensRecebidas == None:
			raise RuntimeError(" Nao foi possivel criar o objeto Lock")

		self.mensagensRecebidas = collections.deque()
		if self.gerenciadorMensagensRecebidas == None:
			raise RuntimeError(" Nao foi possivel criar o deque")		

		self.firebase = pyrebase.initialize_app(config)
		if self.firebase == None:
			raise RuntimeError(" Nao foi possivel criar a instancia do firebase")

		self.database = self.firebase.database()
			if self.database == None:
				raise RuntimeError(" Nao foi possivel criar a instancia de database")

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


		if len(mensagem) > 0:
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
			self.gerenciadorMensagensRecebidas.acquire()
				try:
					self.mensagensRecebidas.append(mensagem["data"])
				finally:
					self.gerenciadorMensagensRecebidas.release()

	##
	## @brief      Gets the ultima mensagem.
	##
	## @param      self  The object
	##
	## @return     The ultima mensagem.
	##
	def getUltimaMensagem(self):
		retorno = None

		if len(self.mensagensRecebidas) > 0:
			self.gerenciadorMensagensRecebidas.acquire()
			try:
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