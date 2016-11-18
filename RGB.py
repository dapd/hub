class RGB:
	Status=''
	red=0
	grenn=0
	blue=0
	"""docstring for RGB"""
	def __init__(self, status,red,green,blue):
		self.Status = status
		self.editarCor(red,green,blue)

	def editarCor(self,red,green,blue):
		self.red=red
		self.green=green
		self.blue=blue

