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
import RPi.GPIO as GPIO

pinoLedRed=0
pinoLedGreen=0
pinoLedBlue=0
pinoButao=0
pinoBuzzer=0

class GerenciadorIO(object):

	dicionario = []

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o LedManager.
	## 
	## Inicia-se os componentes do GerenciadorIO e de Hardware
	## Adiciona-se objetos RGB essenciais aqui
	## 
	## @warning    Possível melhoria: pegar cores de arquivo de configuração.
	##
	def __init__(self):
		self.dicionario=[]
		self.inicializarGPIO()
		self.inicializarLed()
		self.inicializarButao()
		self.inicializarBuzzer()
		self.adicionarRGBsemInteracao('Gas presente',0,0,225)
		self.adicionarRGBsemInteracao('Item esquecido',0,255,255)
	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o GPIO.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de indicar o modo de operação para uma 
	## board
	##
	def inicializarGPIO(self):
		GPIO.setmode(GPIO.BOARD)
		print ("inicialização da protoboard bem sucedida")

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o Led.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de indicar o modo de operação para um
	## LED RGB
	## 
	## @warning    Possível melhoria: pegar cores de arquivo de configuração.
	##
	def inicializarLed(self):
		GPIO.setup(pinoLedRed, GPIO.OUT)
		GPIO.setup(pinoLedGreen, GPIO.OUT)
		GPIO.setup(pinoLedBlue, GPIO.OUT)
		LedRed= GPIO.PWM(pinoLedRed,frequencia)
		LedGreen= GPIO.PWM(pinoLedGreen,frequencia)
		LedBlue= GPIO.PWM(pinoLedBlue,frequencia)
		LedRed.start(0)
		LedGreen.start(0)
		LedBlue.start(0)

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o Butão.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de indicar o modo de operação para um
	## butão
	##
	def inicializarButao(self):
		GPIO.setup(but_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	#------------------------------------------------------------------------------
	## @brief      Método para alarme.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de chamar os outros métodos que servem para 
	## alarmar (led, buzzer)
	##
	def alarmar(self,status):
		cor=self.procurarSignificado(status)
		self.ligarLed(cor)
		self.ligarBuzzer()
		self.esperarDezarmar()

	#------------------------------------------------------------------------------
	## @brief      Método para esperar pelo desarmamento do HUB.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de esperar o butão ser precionado ou receber o comando 
	## do app e chamar o metodo de desarmar
	##
	def esperarPrecionar(self):
		while GPIO.input(but_pin) == GPIO.HIGH:
			pass
		self.desarmar()
	#------------------------------------------------------------------------------
	## @brief      Método para desarme do alarme.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de chamar os outros métodos que servem para 
	## silenciar led e buzzer
	##
	def desarmar(self):
		self.desligarLed()
		self.desligarBuzzer()

	#------------------------------------------------------------------------------
	## @brief      Método de inicialização para o Buzzer.
	## 
	## Tão simples quanto a descrição resumida, esse metodo 
	## tem a finalidade de indicar o modo de operação para um
	## buzzer
	##
	def inicializarBuzzer(self):
		GPIO.setup(buz_pin, GPIO.OUT)

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
	## igual ao passado no parâmetro. Caso ache, retora as cores 
	##
	def procurarSignificado(self,status):
		if len(self.dicionario)>0:
			for objetoRGB in self.dicionario:
				#print (objetoRGB.Status)
				#print (objetoRGB.Status==status)
				if objetoRGB.status==status:
					#print(status)
					return(objetoRGB.red,objetoRGB.green,objetoRGB.blue)
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
	def ligarLed(self,red,green,blue):
		LedRed.ChangeDutyCycle ((1-red/255.0)*100)
		LedGreen.ChangeDutyCycle ((1-green/255.0)*100)
		LedBlue.ChangeDutyCycle ((1-blue/255.0)*100)

	#------------------------------------------------------------------------------
	## @brief      Desliga o led. Simples assim.
	##
	##	O método deve usar uma biblioteca para manipulação de hardware da raspberry
	## e enviar para o led um comando que apropriadamente o desliga.
	##
	## @return     O valor de retorno sempre será @c NULL.
	##
	def desligarLed(self):
		LedRed.ChangeDutyCycle(100)
		LedGreen.ChangeDutyCycle(100)
		LedBlue.ChangeDutyCycle(100)
		
	#------------------------------------------------------------------------------
	## @brief      Liga o Buzzer. Simples assim.
	##
	##	O método deve usar uma biblioteca para manipulação de hardware da raspberry
	## e enviar para o led um comando que apropriadamente o liga.
	##
	## @return     O valor de retorno sempre será @c NULL.
	##	
	def ligarBuzzer(self):
		GPIO.output(buz_pin,1)

	#------------------------------------------------------------------------------
	## @brief      Desliga o Buzzer. Simples assim.
	##
	##	O método deve usar uma biblioteca para manipulação de hardware da raspberry
	## e enviar para o buzzer um comando que apropriadamente o desliga.
	##
	def desligarBuzzer(self):
		GPIO.output(buz_pin,0)

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
		self.status = status
