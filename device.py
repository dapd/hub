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
	## @brief      Disable device
	##
	## @return     Success or failure to disable
	##
	def desativar():
		return False

	##
	## @brief      Validate password
	##
	## @return     Validation success or failure
	##
	def validarSenha():
		return False
