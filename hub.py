# -*- coding: UTF-8 -*-

#-------------------------------------------------------------------------------
## @brief      Classe para o HUB.
##
##              Nesta classe, espera-se que todos os métodos principais do HUB
##             sejam devidamente escritos. O comportamento do HUB por enquanto
##             se limita a um método que fica rodando em loop infinito, e de
##             acordo com os estímulos recebidos das threads de *escutar*, 
##             executa ações, ou seja, é uma máquina de estados.
##              É importante que os métodos de escutar das instâncias
##             @c hubParaMódulo e @c hubParaFirebase rodem em paralelo como
##             threads, e que haja um comportamento de produtor-consumidor
##             quanto às informações obtidas e enviadas.
##             
##             A convenção será: nome minúsculo para instâncias, variáveis e
##             métodos, e nome maiúsculo para classes.
##             
##             @warning Colocar verificações e erros caso algo aconteça, mas
##             nunca paralizar ou fechar o programa. É importante que os erros
##             sejam tratados.
##             
##             @param status              O status do HUB. Uma string pré-definida.
##             @param UID                 O ID do usuário que cadastrou o HUB. Uma String.
##             @param ledManager          Instância da classe LedManager.
##             @param hubParaModulo       Instância da classe HubParaModulo.
##             @param hubParaFirebase     Instância da classe HubParaFirebase.
##             @param adaptadorBluetooth  Instância da classe AdaptadorBluetooth.
##
class Hub(object):

	status = ""
	UID = ""
	ledManager = None
	hubParaModulo = None
	hubParaFirebase = None
	adaptadorBluetooth = None

	#------------------------------------------------------------------------------
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
	##             Por exemplo, para adicionar o parâmetro aux (cujo nome não é
	##             recomendável de ser usado), deve-se fazer o seguinte:
	##
	## @code
	##  def __init__(self, status, aux):
	##   super(Hub, self).__init__()
	##   self.status = status
	##   self.aux = xpto
	## @endcode
	##
	##             Onde xpto é o valor inicial desejado.
	##
	## @warning    Inicializar instâncias de classes depois.
	##
	## @param      self    O objeto
	## @param      status  O status do HUB. Uma string pré-definida.
	##
	def __init__(self, status):
		super(Hub, self).__init__()
		self.status = status

	#------------------------------------------------------------------------------
	## @brief      Esse é o loop principal do HUB, onde será implementada sua 
	##  máquina de estados. 
	##
	##  Este será o segundo método a ser chamado do HUB. Ele deverá ficar em
	## loop e se comportar como uma máquina de estados, chamando os outros métodos
	## de acordo com a situação.
	## 
	## @warning É possível adicionar o comportamento de parar como uma feature: botão
	## de desligar.
	## @return     Essa função nunca para.
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
	##
	##
	## @return O valor de retorno sempre será @c NULL.
	##

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
	