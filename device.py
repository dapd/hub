# -*- coding: UTF-8 -*-

##
## @brief      Classe para Device.
##
class Device(object):
	
	##
	## @brief      Constrói o objeto.
	##
	## @param      self  O objeto
	## @param      arg   O argumento
	##
	def __init__(self, arg):
		super(Device, self).__init__()
		self.arg = arg
		