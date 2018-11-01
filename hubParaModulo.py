# -*- coding: UTF-8 -*-

##
## @brief      Class for hub para modulo.
##
class HubParaModulo(object):
	
	status = ""

	##
	## @brief      Constructs the object.
	##
	## @param      self  The object
	## @param      arg   The argument
	##
	def __init__(self, arg):
		super(HubParaModulo, self).__init__()
		self.arg = arg
	
	##
	## @brief      Connect to module
	##
	## @param      modulo  The module
	##
	## @return     Connection success or failure
	##
	def conectarModulo(modulo):
		return False

	##
	## @brief      Receive message from module
	##
	## @return     Message
	##
	def receberModulo():
		return "ASD"

	##
	## @brief      Send message to module
	##
	## @param      mensagem  The message
	##
	## @return     None
	##
	def mandarModulo(mensagem):
		pass
