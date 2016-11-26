# -*- coding: UTF-8 -*-

import gerenciadorIO
import hubParaFirebase

#-------------------------------------------------------------------------------
## @brief      Classe para o HUB.
##
##
##
class Hub(object):

	status = ""
	factoryID = ""
	ledManager = None
	hubParaModulo = None
	hubParaFirebase = None
	adaptadorBluetooth = None

	pinoLedRed=3
	pinoLedGreen=5
	pinoLedBlue=7
	pinoBuzzer=0
	pinoBotao=0

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

	#------------------------------------------------------------------------------
	## @brief      Esse é o loop principal do HUB, onde será implementada sua 
	##  máquina de estados. 
	##
	##
	##
	def loopPrincipal(self):
		


	#------------------------------------------------------------------------------
	## @brief      Método configura o HUB no primeiro acesso.
	##
	##
	##
	def configurarPrimeiraVez(self):
		raise NotImplementedError(" Favor implementar esse metodo. ")
	#------------------------------------------------------------------------------
	## @brief      Método aciona o Buzzer.
	##
	##             Espera-se que ao chamar esse método, caso o estado atual @c
	##             status da classe atual remeta à ideia de @c alerta, ou seja,
	##             caso seja necessário sinalizar algo para o usuário, ao chamar
	##             essa função, o buzzer irá ser acionado em volume máximo. Caso
	##             o buzzer esteja acionado e o estado atual @c status da classe
	##             atual remeta à ideia de que não há alerta, ou seja, caso o @c
	##             status seja normal, ao chamar essa função, o buzzer será
	##             desligado. De forma simples, essa função funciona como um
	##             interruptor e acessa o parâmetro da própria classe @c status
	##             para decidir o que fazer.
	##
	## @return     O valor de retorno sempre será @c NULL.
	##
	def tocarBuzzer(self):
		raise NotImplementedError(" Favor implementar esse metodo. ")

	#------------------------------------------------------------------------------
	## @brief      Método aciona o Led.
	##
	##             Este método utiliza a instância @c ledManager que é atributo
	##             desta classe, e deve se comportar, utilizando o atributo @c
	##             status e chamando os métodos de ligarLed, desligarLed e
	##             procurarSignificado da classe ledManager. Em resumo, ao
	##             chamar essa classe, é esperado que ela atualize o
	##             comportamento do led de acordo com o status atual.
	##
	## @return     O valor de retorno sempre será @c NULL.
	##
	def acionarLed(self):
		raise NotImplementedError(" Favor implementar esse metodo. ")

hubs = Hub("normal")
hubs.loopPrincipal()
