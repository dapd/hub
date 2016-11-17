# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
## @brief      Classe para o LedManager.
##
##  O LedManager tem seus métodos chamados pelo método acionarLed do HUB. Esta
## classe deve servir de apoio para a classe correspondente no HUB. Não há um
## loop principal.
##
## @param      cores    Dicionário que contém os status e cores, onde para cada
##                      status há uma cor correspondente
## @warning    Adicionar os atributos dessa classe correspondentes a classes
##             necessárias para de fato acionar o led em hardware, e inicializar
##             os mesmos em init.                       
class LedManager(object):

	cores = {}

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o LedManager.
	## 
	##  O atributo cores deve ser inicializado aqui, de modo que cada status tenha
	## uma cor correspondente. Levando em conta que @c cores é um dicionário.
	##
	## @warning    Inicializar instâncias de classes necessárias depois aqui.
	## @warning    Possível melhoria: pegar cores de arquivo de configuração.
	##
	def __init__(self):
		super(LedManager, self).__init__()
		raise NotImplementedError(" Favor implementar esse metodo. ")
	
	#------------------------------------------------------------------------------
	## @brief      Dado um @c status, método retorna uma cor
	##
	##  Tão simples quanto na descrição resumida. O método deve receber um
	## status e devolver uma cor. Nada mais é do que a aplicação do dicionário
	## desta classe.
	##
	## @param      status  O Estado que deseja-se saber a cor.
	##
	## @return     Retorna a cor, do tipo RGB.
	##
	def procuraSignificado(status):
		raise NotImplementedError(" Favor implementar esse metodo. ")
		
	#------------------------------------------------------------------------------
	## @brief      Método usa biblioteca de manipulação de hardware da raspberry
	##             para acionar led.
	## 
	##  O método deve usar uma biblioteca para manipulação de hardware da raspberry
	## e enviar para o led um comando que apropriadamente o coloque na cor indicada.
	##
	## @param      rgb   O valor de rbg para o led. É uma intância da classe RGB.
	##
	## @return     O valor de retorno sempre será @c NULL.
	##
	def ligarLed(rgb):
		raise NotImplementedError(" Favor implementar esse metodo. ")

	#------------------------------------------------------------------------------
	## @brief      Desliga o led. Simples assim.
	##
	##	O método deve usar uma biblioteca para manipulação de hardware da raspberry
	## e enviar para o led um comando que apropriadamente o desliga.
	##
	## @return     O valor de retorno sempre será @c NULL.
	##
	def desligarLed():
		raise NotImplementedError(" Favor implementar esse metodo. ")

#-------------------------------------------------------------------------------
## @brief      Classe para rgb.
##
##  Essa classe nada mais é do que o equivalente a uma struct em c. Só armazena
## de forma rezumida uma cor RGB.
##
## @param      red    Cor vermelha armazenada, inteiro, com valores indo de 0 a 255
## @param      green  Cor verde armazenada, inteiro, com valores indo de 0 a 255
## @param      blue   Cor azul armazenada, inteiro, com valores indo de 0 a 255
class RGB(object):

	red = 0
	green = 0
	blue = 0

	#------------------------------------------------------------------------------
	## @brief      Inicializa uma cor.
	## 
	##  Ao chamar essa função, a cor é inicializada e utilizada nessa instância.
	##
	## @param      self   O objeto
	## @param      red    Cor vermelha, inteiro, com valores indo de 0 a 255
	## @param      green  Cor verde, inteiro, com valores indo de 0 a 255
	## @param      blue   Cor Azul, inteiro, com valores indo de 0 a 255
	##
	def __init__(self, red, green, blue):
		super(RGB, self).__init__()
		self.red = red
		self.green = green
		self.blue = blue