# -*- coding: UTF-8 -*-
from pyrebase import *
from threading import *
import collections
from socket import gaierror
from httplib2 import ServerNotFoundError

##
## @brief      Esta classe é responsável pela comunicação entre o HUB e o banco
##             de dados firebase.
##
##             Este módulo provem funções básicas de comunição, entretando não é
##             responsável pela lógica usada de acordo com as mensagens.
##
## @param      hubID               O id do hub cadastrado no banco de dados
##                                 firebase
## @param      appID               O id do app/do usuário do app no banco de dados
##                                 firebase que possui o hub.
## @param      firebase            Objeto da classe pyrebase, responsável pela
##                                 conexão com o servidor
## @param      database            Objeto da classe pyrebase, responsável por
##                                 recuperar dados do banco de dados firebase.
## @param      mensagensRecebidas  As mensagens recebidas pelo módulo, guardadas
##                                 como uma lista ordenada.
##
class HubParaFirebase(object):
	hubID = ""
	appID = ""
	config = None
	firebase = None
	database = None
	gerenciadorMensagensRecebidas = None
	mensagensRecebidas = None

	##
	## @brief      Constructs the object.
	##
	## @param      self   O objeto
	## @param      hubID  The hub id
	##
	def __init__(self, hubID):
		super(HubParaFirebase, self).__init__()

		self.config = {
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

		try:
			self.firebase = pyrebase.initialize_app(self.config)
			if self.firebase == None:
				print(" #warning: Nao foi possivel criar a instancia do firebase")

			self.database = self.firebase.database()
			if self.database == None:
				print(" #warning: Nao foi possivel criar a instancia de database")
		except:
			self.reconectar()

		try:
			query = self.database.child("hubs").get()
		except:
			self.reconectar()
			query = self.database.child("hubs").get()

		hubs = query.val()
		if not hubID in hubs.keys():
			raise ValueError(" HUB com id dado nao existe")
		else:
			self.hubID = hubID

			hubAtual = hubs[hubID]
			if "dono" in hubAtual.keys():
				self.appID = hubAtual["dono"]
			else:
				print(" #Warning: Hub nao tem dono ainda")
				self.appID = None

		if self.appID != None:
			try:
				self.stream = self.database.child("msgs_app").child(self.appID).stream(self.receberFirebase, stream_id="mensagens_app")
			except:
				self.reconectar()
				self.stream = self.database.child("msgs_app").child(self.appID).stream(self.receberFirebase, stream_id="mensagens_app")
			if self.stream == None:
				raise RuntimeError(" Nao foi possivel criar o stream de dados com o firebase")
		else:
			print("#Warning: Nao eh possivel escutar mensagens do app. Defina um dono para este hub")
		try:
			self.database.child("hubs").child(self.hubID).update({"status" : "ON"})
		except:
			self.reconectar()
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
		
		try:
			self.stream.close()
		except AttributeError as e:
			raise e
			print(" Erro ao se desconectar do firebase. Favor, reportar issue")

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
		try:
			query = self.database.child("hubs").child(self.hubID).child("modulos").get()
		except:
			self.reconectar()
			query = self.database.child("hubs").child(self.hubID).child("modulos").get()

		modulos = query.val()

		if not moduloID in modulos:
			raise ValueError(" Modulo nao encontrado para o hub atual") 
		else:
			if len(mensagem) > 0:
				try:
					self.database.child("msgs_hub").child(self.hubID).push("alarme:" + moduloID)
					self.database.child("msgs_hub").child(self.hubID).push(mensagem)
				except:
					self.reconectar()
					self.database.child("msgs_hub").child(self.hubID).push("alarme:" + moduloID)
					self.database.child("msgs_hub").child(self.hubID).push(mensagem)
			else:
				raise ValueError(" Mensagem vazia")

	##
	## @brief      { function_description }
	##
	## @param      self      The object
	## @param      moduloID  The modulo id
	##
	## @return     { description_of_the_return_value }
	##
	def mensagemModuloON(self, moduloID):
		try:
			query = self.database.child("hubs").child(self.hubID).child("modulos").get()
		except:
			self.reconectar()
			query = self.database.child("hubs").child(self.hubID).child("modulos").get()

		modulos = query.val()

		if not moduloID in modulos:
			raise ValueError(" Modulo nao encontrado para o hub atual") 
		else:
			try:
				self.database.child("hubs").child(self.hubID).child("modulos").update({moduloID : "ON"})
			except:
				self.reconectar()
				self.database.child("hubs").child(self.hubID).child("modulos").update({moduloID : "ON"})
	
	def reconectar(self):
		conectado = False
		while conectado == False:
			try:
				self.firebase = pyrebase.initialize_app(self.config)
				if self.firebase == None:
					print(" #warning: Nao foi possivel criar a instancia do firebase")

				self.database = self.firebase.database()
				if self.database == None:
					print(" #warning: Nao foi possivel criar a instancia de database")

				if self.appID != None:
					try:
						self.stream.close()
					except:
						pass
					self.mensagensRecebidas = None
					self.stream = self.database.child("msgs_app").child(self.appID).stream(self.receberFirebase, stream_id="mensagens_app")
					if self.stream == None:
						print(" #warning: Nao foi possivel criar o stream de dados com o firebase")

				self.database.child("hubs").get()
			except ServerNotFoundError:
				print("Reconectando ao servidor...")
			except gaierror:
				print("Reconectando ao servidor...")
			else:
				conectado = True
		print("Coneccao restabelecida.")
	##
	## @brief      { function_description }
	##
	## @param      self      The object
	## @param      mensagem  The mensagem
	##
	## @return     { description_of_the_return_value }
	## @warning    Não chamar essa função. Esta função é chamada internamente
	##             pela classe.
	##
	def receberFirebase(self, mensagem):
		if mensagem == None:
			raise ValueError(" Erro inesperado ao receber mensagem do stream de dados")
		else:
			if mensagem["path"] == "/" and mensagem["data"] != None:
				dados = sorted(mensagem["data"].items())
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
			else:
				print("#Warning: Mensagem de conteudo enigmatico recuperada do servidor")

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
		try:
			self.database.child("msgs_hub").remove()
		except:
			self.reconectar()
			self.database.child("msgs_hub").remove()

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def atualizarDono(self):
		if self.appID != "":
			print(" #Warning: Dono ja foi definido")
		else:
			try:
				query = self.database.child("hubs").get()
			except:
				self.reconectar()
				query = self.database.child("hubs").get()
			hubs = query.val()
			hubAtual = hubs[hubID]

			if "dono" in hubAtual.keys():
				self.appID = hubAtual["dono"]
			else:
				print(" #Warning: Hub nao tem dono ainda")
				self.appID = None
			if self.stream != None:
				raise RuntimeError(" Programa ja esta escutando por um stream")
			else:
				if self.appID != None:
					self.stream = self.database.child("msgs_app").child(self.appID).stream(self.receberFirebase, stream_id="mensagens_app")
					if self.stream == None:
						raise RuntimeError(" Nao foi possivel criar o stream de dados com o firebase")
				else:
					print("#Warning: Nao eh possivel escutar mensagens do app. Defina um dono para este hub")

asd = HubParaFirebase("auhdasudad")
asd.mensagemModuloON("objetos")
asd.mensagemModuloON("gas")
asd.mensagemAlarme("objetos", "Objeto 'celular' esta faltando.")
asd.apagarMensagensHub()
# asd.atualizarDono()
print(asd.mensagensRecebidas)
print(asd.getUltimaMensagem())
print(asd.getUltimaMensagem())
t = Timer(10, asd.desconectarFirebase)
t.start()