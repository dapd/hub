# -*- coding: UTF-8 -*-

##
## @brief      Classe para o HUB.
##
##  Nesta classe, espera-se que todos os métodos principais do HUB sejam
## devidamente escritos. O comportamento do HUB por enquanto
##
class Hub(object):

	status = ""

	##
	## @brief      Método de inicialização para o HUB.
	##
	##             O método de inicialização para o HUB recebe como entrada o
	##             valor inicial do status do HUB e retorna um booleano, que
	##             informa se a operação foi concluída com sucesso. Espera-se
	##             que após chamar essa função, todos os parâmetros do HUB
	##             estejam devidamente inicializados. Isso inclui parâmetros
	##             adicionados posteriormente por necessidade, ou seja,
	##             parâmetros auxiliares.
	##
	##             Para adicionar parâmetros auxiliares, adicione o mesmo em:
	##
	## @code
	##  def __init__(self, status):
	## @endcode
	## 
	## Por exemplo, para adicionar o parâmetro aux (cujo nome não é
	## recomendável de ser usado), deve-se fazer o seguinte:
	##
	## @code
	##  def __init__(self, status, aux):
	##  	super(Hub, self).__init__()
	##		self.status = status
	##  	self.aux = xpto
	## @endcode
	##
	##  Onde xpto é o valor inicial desejado.
	##
	## @param      self    O objeto
	## @param      status  O status do HUB. Uma string pré-definida.
	##
	def __init__(self, status):
		super(Hub, self).__init__()
		self.status = status

	##
	## @brief      Método configura o HUB no primeiro acesso.
	## 
	##  No primeiro acesso ao HUB, o mesmo não estará cadastrado no servidor
	## e, portanto, não estará anexado ao usuário. Espera-se que esse método
	## realize uma coneção com o firebase, sem utilizar o respectivo objeto
	## de coneção ao firebase. Ou seja, uma conexão simples ao firebase é
	## realizada aqui. Espera-se receber através dessa conexão o UID do
	## usuário que adicionou este HUB.
	##
	## @return     UID do usuário que adicionou este HUB.
	## @warning    Modificar diagrama de bloco para que demonstre o que é retornado aqui.
	##
	def configurarPrimeiraVez():
		pass

	##
	## @brief      Método aciona o Buzzer.
	##
	## @return O valor de retorno sempre será @c NULL.
	##
	def tocarBuzzer():
		pass

	##
	## @brief      Método aciona o Led.
	##
	## @return O valor de retorno sempre será @c NULL.
	##
	def acionarLed():
		pass