# -*- coding: UTF-8 -*-
from pyrebase import *
from threading import *
import urllib.request
import urllib.error
import collections
from socket import gaierror
from httplib2 import ServerNotFoundError
import random
from ledManager import *

##
## @brief      Esta classe é responsável pela comunicação entre o HUB e o banco
##             de dados firebase.
##
##  Este módulo provem funções básicas de comunição, entretando não é
## responsável pela lógica usada de acordo com as mensagens. Isso
## significa que é de responsabilidade da classe Hub interpretar as
## mensagens e fazer as devidas ações em sua máquina de estados. As
## ações que podem ser realizadas com esse módulo são descritas a
## seguir, além de acompanharem um exemplo de código:
##
##  **Conectar-se ao firebase**
##
##  Para conectar-se ao firebase, basta criar uma nova instância
## dessa classe. Na inicialização dessa instãncia, a coneção será
## efetuada. Para mais informações, ver __init__().
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
## @endcode
##
##  **Notificar que um módulo está ligado**
##
##  Ao se desconectar, o Hub seta o estado de todos os módulos para
## DISCONECTED no Banco de dados firebase. Ao se reconectar, isto é,
## logo após chamar o construtor, é imprescindível que o Hub
## notifique o servidor dos módulos conectados a ele. Para mais
## informações, ver
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
##  foo.mensagemModuloStatus("modulo_1_id", True)
##  foo.mensagemModuloStatus("modulo_2_id", True)
##  foo.mensagemModuloStatus("modulo_3_id")
##  #  Aqui os módulos de id modulo_1_id, modulo_2_id e modulo_3_id têm seu
##  # status setado para ON. Perceba que para o módulo 3 não passamos True
##  # como parâmatro. Isso porque esse segundo parâmetro é True por padrão, logo
##  # as duas formas são válidas, tando com ou sem o True.
##  #  É importante ressaltar que o id do módulo deve ser válido.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/hubID/modulos do JSON
##  # do Banco de dados firebase, em que hubID é o id do hub, por exemplo, poderia
##  # ser hubs/kasldjlasjdl/modulos.
## @endcode
##
##  Para notificar que um módulo está desligado, deve-se proceder
## usando a mesma função, mas com o atributo originalmente setado
## para True como False. O False é obrigatório nesse caso, caso
## contrário, será enviada uma mensagem como True.
##
## @code
##   import hubParaFirebase
##
##   foo = HubParaFirebase("kasldjlasjdl")
##   #  Qualquer nome pode ser usado, nao precisa ser foo
##   #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##   # esperado que ele seja estático e único para o HUB atual.
##   #  Por válido, quero dizer que ele precisa estar cadastrado
##   # no Banco de dados e deve constar no diretório /hubs/ do JSON
##   # do Banco de dados firebase.
##   foo.mensagemModuloStatus("modulo_1_id", False)
##   foo.mensagemModuloStatus("modulo_2_id", False)
##   #  O parâmetro False é obrigatório para este caso.
##   #  É importante ressaltar que o id do módulo deve ser válido.
##   #  Por válido, quero dizer que ele precisa estar cadastrado
##   # no Banco de dados e deve constar no diretório /hubs/hubID/modulos do JSON
##   # do Banco de dados firebase, em que hubID é o id do hub, por exemplo, poderia
##   # ser hubs/kasldjlasjdl/modulos.
## @endcode
##
##  **Enviar um alarme**
##
##  Para enviar um alarme é preciso que o hub esteja conectado ao
## firebase, e que o módulo em questão exista e esteja ativo. O
## conteúdo da mensagem deverá ser a mensagem de alerta que vem por
## padrão do módulo. Para mais informaçães, ver função
## mensagemAlarme().
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
##  foo.mensagemModuloStatus("modulo_1_id")
##  #  Aqui o módulo de id modulo_1_id tem seu status setado para ON.
##  #  É importante ressaltar que o id do módulo deve ser válido.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/hubID/modulos do JSON
##  # do Banco de dados firebase, em que hubID é o id do hub, por exemplo, poderia
##  # ser hubs/kasldjlasjdl/modulos.
##  foo.mensagemAlarme("modulo_1_id", "Nivel de xpto 50% acima do maximo.")
##  # A mensagem é enviada para o servidor. Para mais informações sobre o formato
##  # da mensagem, ver função mensagemAlarme()
## @endcode
##
##  **Pegar mensagem mais antiga não tratada recebida que o app enviou**
##
##  Apenas a mensagem mais antiga não tratada pode ser recuperada,
## uma de cada vez, até a mais nova, num formato de fila. Se não há
## mensagens, a função utilizada retorna None. A mensagem é uma
## string.
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
##  mensagem = foo.getUltimaMensagem()
##  if mensagem == None:
##   print("Nao ha mensagens")
##  else:
##   print(mensagem)
## @endcode
##
##  **Como se desconectar do firebase**
##
##  Por desconexão quero dizer que a instância da classe irá parar de
## escutar as mensagens que vem do App, além disso, o status de
## todos os módulos conectados ao hub serão setados para DISCONECTED
## no banco de dados firebase, e o status do Hub será setado para
## OFF. Entretando, ainda será possível usar esta instância. Mas é
## imprescindível que não use ela após se desconectar.
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
##  foo.desconectarFirebase()
##  foo = None
## @endcode
##
##  **Como limpar do servidor todas as mensagens enviadas pelo hub**
##
##  O app poderá enviar uma mensagem que seja interpretada pelo hub
## como: já li tudo, pode excluir tudo agora. Nesse caso, a máquina
## de estados do hub deve interpretar e chamar a função
## apagarMensagensHub() para concretizar o comando.
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
##  foo.apagarMensagensHub()
## @endcode
##
##  **Como anexar este hub a um novo dono na primeira conexão?**
##
##  Na primeira conexão, uma instância dessa classe será criada e um
## warning informará que este hub não tem um dono. A função de pegar
## as mensagens não lidas que vieram do app não funcionará, e será
## esperado que se anexe um dono. Isso será feito do lado do app,
## assim que for digitado o id do hub no app, na hora de adicionar o
## hub. Ao chamar a função atualizarDono(), esta classe verifica se
## um novo dono foi anexado ao hub atual, se sim, ela passa a se
## comportar normalmente, se não, outro warning é lançado, e deve-se
## tentar de novo depois. Para mais informações, ver atualizarDono()
## Função haDono verifica se hub atual tem dono, se tiver, retorna
## True. Para mais informações, ver haDono()
##
## @code
##  import hubParaFirebase
##
##  foo = HubParaFirebase("kasldjlasjdl")
##  #  Qualquer nome pode ser usado, nao precisa ser foo
##  #  "kasldjlasjdl" deve ser um id válido para um HUB, e é
##  # esperado que ele seja estático e único para o HUB atual.
##  #  Por válido, quero dizer que ele precisa estar cadastrado
##  # no Banco de dados e deve constar no diretório /hubs/ do JSON
##  # do Banco de dados firebase.
##  while not foo.haDono():
##   foo.atualizarDono()
## @endcode
##
## @param      hubID               O id do hub cadastrado no banco de dados
##                                 firebase. Deve ser válido antes de usá-lo aqui.
## @param      appID               O id do app/do usuário do app no banco de dados
##                                 firebase que possui o hub. Não precisa existir
##                                 no início, quando essa classe é instanciada.
## @param      __firebase          Objeto da classe pyrebase, responsável pela
##                                 conexão com o servidor. Privado.
## @param      __config            O JSON de conexão que é dado pelo site do firebase.
##                                 Privado. Não mexer.
## @param      database            Objeto da classe pyrebase, responsável por
##                                 recuperar dados do banco de dados firebase.
##                                 Privado.
## @param      mensagensRecebidas  As mensagens recebidas pelo módulo, guardadas
##                                 como uma fila, implementada como um deque.
##                                 Privado. Para acessar as mensagens use o método
##                                 apropriado, getUltimaMensagem()
##
class HubParaFirebase(object):
	hubID = ""
	appID = ""
	__config = None
	__firebase = None
	database = None
	stream = None
	gerenciadorMensagensRecebidas = None
	mensagensRecebidas = None

	##
	## @brief      Inicializa a instância da classe e se conecta ao firebase.
	## 
	##  Altere a inicialização self.__config apropriadamente.
	##  Esse método conecta-se com o firebase, seta o status do hub atual para
	## ON, e, caso o hub já tenha um dono, começa a escutar as mensagens do app. 
	##
	## Exemplo de uso:
	## 
	## @code
	##  foo = HubParaFirebase("kasldjlasjdl")
	## @endcode
	##
	## @param      self   O objeto
	## @param      hubID  O id do hub. É esperado que seja válido. Ver HubParaFirebase
	##                    para mais detalhes.
	##
	def __init__(self, hubID):
		super(HubParaFirebase, self).__init__()

		self.__config = {
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
		if self.mensagensRecebidas == None:
			raise RuntimeError(" Nao foi possivel criar o deque")		

		try:
			self.__firebase = pyrebase.initialize_app(self.__config)
			if self.__firebase == None:
				print(" #warning: Nao foi possivel criar a instancia do firebase")

			self.database = self.__firebase.database()
			if self.database == None:
				print(" #warning: Nao foi possivel criar a instancia de database")
		except:
			self.__reconectar()

		try:
			query = self.database.child("hubs").get()
		except:
			self.__reconectar()
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
				self.stream = self.database.child("msgs_app").child(self.appID).stream(self.__receberFirebase, stream_id="mensagens_app")
			except:
				self.__reconectar()
				self.stream = self.database.child("msgs_app").child(self.appID).stream(self.__receberFirebase, stream_id="mensagens_app")
			if self.stream == None:
				raise RuntimeError(" Nao foi possivel criar o stream de dados com o firebase")
		else:
			print("#Warning: Nao eh possivel escutar mensagens do app. Defina um dono para este hub")
		try:
			self.database.child("hubs").child(self.hubID).update({"status" : "ON"})
		except:
			self.__reconectar()
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
		
		if self.appID != None and self.stream != None:
			try:
				self.stream.close()
			except AttributeError as e:
				print(" Erro ao se desconectar do firebase. Favor, reportar issue")
				raise e

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
			self.__reconectar()
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
					self.__reconectar()
					self.database.child("msgs_hub").child(self.hubID).push("alarme:" + moduloID)
					self.database.child("msgs_hub").child(self.hubID).push(mensagem)
			else:
				raise ValueError(" Mensagem vazia")

	##
	## @brief      { function_description }
	##
	## @param      self       The object
	## @param      moduloID   The modulo id
	## @param      status_on  The status_on
	##
	## @return     { description_of_the_return_value }
	##
	def mensagemModuloStatus(self, moduloID, status_on = True):
		if status_on == True:
			mensagem = "ON"
		else:
			mensagem = "DISCONECTED"

		try:
			query = self.database.child("hubs").child(self.hubID).child("modulos").get()
		except:
			self.__reconectar()
			query = self.database.child("hubs").child(self.hubID).child("modulos").get()

		modulos = query.val()

		if not moduloID in modulos:
			raise ValueError(" Modulo nao encontrado para o hub atual") 
		else:
			try:
				self.database.child("hubs").child(self.hubID).child("modulos").update({moduloID : mensagem})
			except:
				self.__reconectar()
				self.database.child("hubs").child(self.hubID).child("modulos").update({moduloID : mensagem})

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def __internet_on(self):
	    try:
	        urllib.request.urlopen('http://216.58.192.142', timeout=1)
	        return True
	    except urllib.error.URLError as err: 
	        return False

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def __reconectar(self):
		while not self.__internet_on():
			print("Reconectando ao servidor...\n\n\n")
		print("Reconectado.")

		self.__firebase = pyrebase.initialize_app(self.__config)
		if self.__firebase == None:
			print(" #warning: Nao foi possivel criar a instancia do firebase")

		self.database = self.__firebase.database()
		if self.database == None:
			print(" #warning: Nao foi possivel criar a instancia de database")

		if self.appID != None:
			try:
				self.stream.close()
			except:
				pass

			self.gerenciadorMensagensRecebidas.acquire()
			try:
				self.mensagensRecebidas = collections.deque()
				if self.mensagensRecebidas == None:
					raise RuntimeError(" Nao foi possivel criar o deque")
			finally:
				self.gerenciadorMensagensRecebidas.release()

			self.stream = self.database.child("msgs_app").child(self.appID).stream(self.__receberFirebase, stream_id="mensagens_app")
			if self.stream == None:
				print(" #warning: Nao foi possivel criar o stream de dados com o firebase")

			print(self.database.child("hubs").get().val())
		print("Coneccao restabelecida.		")
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
	def __receberFirebase(self, mensagem):
		print("Recebendo mensagens..")
		if mensagem == None:
			raise ValueError(" Erro inesperado ao receber mensagem do stream de dados")
		else:
			if mensagem["path"] == "/" and mensagem["data"] != None:
				dados = sorted(mensagem["data"].items())
				for chaves, valor in dados:
					if chaves != self.appID:
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
			self.__reconectar()
			self.database.child("msgs_hub").remove()

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def atualizarDono(self):
		if self.appID != None:
			print(" #Warning: Dono ja foi definido")
		else:
			try:
				query = self.database.child("hubs").get()
			except:
				self.__reconectar()
				query = self.database.child("hubs").get()
			hubs = query.val()
			hubAtual = hubs[self.hubID]
			print(hubAtual.keys())
			if "dono" in hubAtual.keys():
				self.appID = hubAtual["dono"]
			else:
				print(" #Warning: Hub nao tem dono ainda")
				self.appID = None
			if self.stream != None:
				raise RuntimeError(" Programa ja esta escutando por um stream")
			else:
				if self.appID != None:
					self.stream = self.database.child("msgs_app").child(self.appID).stream(self.__receberFirebase, stream_id="mensagens_app")
					if self.stream == None:
						raise RuntimeError(" Nao foi possivel criar o stream de dados com o firebase")
				else:
					print("#Warning: Nao eh possivel escutar mensagens do app. Defina um dono para este hub")

	##
	## @brief      { function_description }
	##
	## @param      self  The object
	##
	## @return     { description_of_the_return_value }
	##
	def haDono(self):
		try:
				query = self.database.child("hubs").get()
		except:
			self.__reconectar()
			query = self.database.child("hubs").get()
		hubs = query.val()
		hubAtual = hubs[self.hubID]
		print(hubAtual.keys())
		if "dono" in hubAtual.keys():
			return True
		else:
			return False

led = LedManager()
but_pin=11
buz_pin=13
GPIO.setup(but_pin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buz_pin,GPIO.OUT)
led.ligarLed(255,255,0)	
asd = HubParaFirebase("auhdasudad")
asd.mensagemModuloStatus("objetos")
asd.mensagemModuloStatus("gas")

msg = ""
alarm1 = 0
alarm2 = 0
alarm3 = 0
alarm4 = 0
alarm5 = 0
alarm6 = 0
alarm7 = 0

led.ligarLed(0,0,255)

while msg != "sair":
	led.ligarLed(255,100,0)
	while not asd.haDono():
		print("Esperando dono do hub ser definido..")
	
	led.ligarLed(0,255,0)

	if asd.appID == None:
		asd.atualizarDono()

	if random.uniform(0,1) > 0.50:
		if random.uniform(0,1) > 0.7 and alarm1 != 1:	
			asd.mensagemAlarme("gas", "Há gás no ambiente")
			alarm1 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)

		if random.uniform(0,1) > 0.8 and alarm2 != 1:	
			asd.mensagemAlarme("gas", "Gás perto de valor crítico.")
			alarm2 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)

		if random.uniform(0,1) > 0.95 and alarm3 != 1:	
			asd.mensagemAlarme("gas", "Gás acima do valor crítico.")
			alarm3 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)

		if random.uniform(0,1) > 0.99 and alarm4 != 1:	
			asd.mensagemAlarme("gas", "Risco de explosão.")
			alarm4 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)

		if random.uniform(0,1) > 0.92 and alarm5 != 1:
			asd.mensagemAlarme("objetos", "Objeto 'Chaves' foi esquecido.")
			alarm5 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)

		if random.uniform(0,1) > 0.6 and alarm6 != 1:
			asd.mensagemAlarme("objetos", "Objeto 'Cartão do CIn' foi esquecido.")
			alarm6 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)

		if random.uniform(0,1) > 0.7 and alarm7 != 1:
			asd.mensagemAlarme("objetos", "Objeto 'Dinheiro' foi esquecido.")
			alarm7 = 1
			led.ligarLed(255,0,0)
			GPIO.output(buz_pin,1)
	
	if GPIO.input(but_pin) == GPIO.LOW:
		GPIO.output(buz_pin,0)

	msg = asd.getUltimaMensagem()
	print(msg)
asd.desconectarFirebase()
led.desligarLed()
