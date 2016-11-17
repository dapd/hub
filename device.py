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
	## @brief      { function_description }
	##
	## @return     { description_of_the_return_value }
	##
	def desativar():
		return False

	##
	## @brief      { function_description }
	##
	## @return     { description_of_the_return_value }
	##
	def validarSenha():
		return False