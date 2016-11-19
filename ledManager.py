# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
## @brief      Classe para o LedManager.
##
##  O LedManager tem seus métodos chamados pelo método acionarLed do HUB. Esta
## classe deve servir de apoio para a classe correspondente no HUB. Não há um
## loop principal.Esta classe utiliza a classe RGB
##
## @param      dicionario    Lista que contém os status e cores, onde para cada
##                      status há uma cor correspondente
## @warning    Adicionar os atributos dessa classe correspondentes a classes
##             necessárias para de fato acionar o led em hardware, e inicializar
##             os mesmos em init. 

import RGB

class LedManager(object):

	dicionario = []

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o LedManager.
	## 
	## Deve-se adicionar objetos RGB essenciais aqui
	## 
	## @warning    Inicializar instâncias de classes necessárias depois aqui.
	## @warning    Possível melhoria: pegar cores de arquivo de configuração.
	##
	def __init__(self):
		self.dicionario=[]
		self.adicionarRGBsemInteracao('Gas presente',0,0,225)
		self.adicionarRGBsemInteracao('Item esquecido',0,255,255)
	
	#------------------------------------------------------------------------------
	## @brief      Método de adção de objetos RGB ao dicionário.
	## 
	## Metodo responsável por criar o objeto RGB com os dados que foram
	## passados via parametros
	## 
	## @warning    Inicializar instâncias de classes necessárias depois aqui.
	## @warning    Possível melhoria: pegar cores de arquivo de configuração.
	##
	def adicionarRGBsemInteracao(self,status,red,green,blue):
	if self.procurarSignificado(status)==0:
		objetoRGB= RGB.RGB(status,red,green,blue)
		self.dicionario.append(objetoRGB)
	#------------------------------------------------------------------------------
	## @brief      Dado um @c status, método acende led com cor especificada anteriormente
	##
	##  Tão simples quanto na descrição resumida. O método deve receber um
	## status e procurar no dicionário se existe algum objeto RGB cujo status foi 
	## igual ao passado no parâmetro. Caso ache, ele chama o método para acender 
	## o led com as devidas cores, caso cotrário ele não faz nada.
	##
	def procurarSignificado(self,status):
		if len(self.dicionario)>0:
			for objetoRGB in self.dicionario:
				#print (objetoRGB.Status)
				#print (objetoRGB.Status==status)
				if objetoRGB.Status==status:
					#print(status)
					self.ligarLed((objetoRGB.red,objetoRGB.green,objetoRGB.blue))
					return 1

			#print('dicionario nao conhece esse status -',status)
			return 0

		else:
			#print ('dicionario vazio -',status)
			return 0

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
## @param      Status status possivel do HUB armazenados, String
## @param      red    Cor vermelha armazenada, inteiro, com valores indo de 0 a 255
## @param      green  Cor verde armazenada, inteiro, com valores indo de 0 a 255
## @param      blue   Cor azul armazenada, inteiro, com valores indo de 0 a 255
class RGB(object):
	status=''
	red = 0
	green = 0
	blue = 0

	#------------------------------------------------------------------------------
	## @brief      Inicializa uma cor.
	## 
	##  Ao chamar essa função, a cor é inicializada e utilizada nessa instância.
	##
	## @param      Status status possivel do HUB armazenados, String
	## @param      self   O objeto
	## @param      red    Cor vermelha, inteiro, com valores indo de 0 a 255
	## @param      green  Cor verde, inteiro, com valores indo de 0 a 255
	## @param      blue   Cor Azul, inteiro, com valores indo de 0 a 255
	##
	def __init__(self, status, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue
		self.Status = status
