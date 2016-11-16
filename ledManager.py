##
## coding: UTF-8 -*-
##

##
## @brief      Classe para o ledManager.
##
class LedManager(object):

	##
	## @brief      Constrói o objeto.
	##
	## @param      self  O objeto
	## @param      arg   O argumento
	##
	def __init__(self, arg):
		super(LedManager, self).__init__()
		self.arg = arg
		