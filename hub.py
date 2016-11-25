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

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o HUB.
	##
	##             
	##
	def __init__(self):
		super(Hub, self).__init__()
		self.status = "STARTING"
		self.factoryID = "C0Oj2DnuuU2Y"
		self.gerenciadorIO = GerenciadorIO()
		self.hubParaFirebase = HubParaFirebase(self.factoryID)

	#------------------------------------------------------------------------------
	## @brief      Esse é o loop principal do HUB, onde será implementada sua 
	##  máquina de estados. 
	##
	##
	##
	def loopPrincipal(self):
		raise NotImplementedError(" Favor implementar esse metodo. ")


	#------------------------------------------------------------------------------
	## @brief      Método configura o HUB no primeiro acesso.
	##
	##             No primeiro acesso ao HUB, o mesmo não estará cadastrado no
	##             servidor e, portanto, não estará anexado ao usuário.
	##             Espera-se que esse método realize uma coneção com o firebase,
	##             sem utilizar o respectivo objeto de coneção ao firebase. Ou
	##             seja, uma conexão simples ao firebase é realizada aqui.
	##             Espera-se receber através dessa conexão o UID do usuário que
	##             adicionou este HUB.
	##
	## @return     UID do usuário que adicionou este HUB.
	## @warning    Modificar diagrama de blocos para que demonstre o que é
	##             retornado aqui.
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
