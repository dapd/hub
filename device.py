# -*- coding: UTF-8 -*-

##
## @brief      Class for device.
##
## @param _id       The Id
##
class Device(object):
	
	_id = ""

	##
	## @brief      Constructs the object.
	##
	## @param      self  The object
	## @param      arg   The argument
	##
	def __init__(self, arg):
		super(Device, self).__init__()
		self.arg = arg
	
	##
	## @brief      Descrição curta
	##
	## Descrição longa
	##
	## @return     Valor de retorno
	##
	def desativar():
		return False

	##
	## @brief      Descrição curta
	##
	## Descrição longa
	##
	## @return     Valor de retorno
	##
	def validarSenha():
		return False