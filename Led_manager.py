import RGB
#dgdg
class LedManager:
	dicionario=[]

	"""docstring for LedManeger"""
	def __init__(self):
		self.dicionario=[]
		self.adicionarRGBsemInteracao('Gas presente',0,0,225)
		self.adicionarRGBsemInteracao('Item esquecido',0,255,255)

	def adicionarRGBsemInteracao(self,status,red,green,blue):
		if self.procurarSignificado(status)==0:
			objetoRGB= RGB.RGB(status,red,green,blue)
			self.dicionario.append(objetoRGB)

	def adicionarRGB(self):
		status=input('Status para adicionar:')
		if self.procurarSignificado(status)==0:
			red=int( input('Vermelho(0 ate 255):') )
			green=int( input('Verde(0 ate 255):') )
			blue=int( input('Vermelho(0 ate 255):') )
			objetoRGB= RGB.RGB(status,red,green,blue)
			self.dicionario.append(objetoRGB)

	def procurarSignificado(self,status):
		if len(self.dicionario)>0:
			for objetoRGB in self.dicionario:
				#print (objetoRGB.Status)
				#print (objetoRGB.Status==status)
				if objetoRGB.Status==status:
					print(status)
					self.ligarLed((objetoRGB.red,objetoRGB.green,objetoRGB.blue))
					return 1

			print('dicionario nao conhece esse status -',status)
			return 0

		else:
			print ('dicionario vazio -',status)
			return 0

	def ligarLed(self,cor):
		print ('Vermelho:',cor[0])
		print ('Verde:',cor[1])
		print ('Azul:',cor[2])

	def desligarLed():
		print ('apagou')

class Teste:
	def __init__ (self):
		self.main()

	def main(self):
		objetoRGB= RGB.RGB('oi',2,2,2)
		gerenciador=LedManager()
		gerenciador.procurarSignificado('JONH CENA')
		gerenciador.procurarSignificado('Gas presente')
		gerenciador.procurarSignificado('Item esquecido')
		gerenciador.procurarSignificado('JONH CENA2')
		gerenciador.adicionarRGB()
		gerenciador.adicionarRGB()
		gerenciador.procurarSignificado( input('Status para procurar:') )
		gerenciador.procurarSignificado( input('Status para procurar:') )
		print('\n\n\n\nOLHA O DICIONARIO')
		for objetoRGB in gerenciador.dicionario:
			print(objetoRGB.Status)

teste=Teste()
