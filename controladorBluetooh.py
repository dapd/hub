# -*- coding: UTF-8 -*-

import * from adaptadorBluetooh

##
## @brief      Class for controlador bluetooh.
##
class ControladorBluetooh(object):

	##
	## @brief      Constructs the object.
	##
	## @param      self  The object
	## @param      arg   The argument
	##
	def __init__(self, arg):
		super(ControladorBluetooh, self).__init__()
		self.arg = arg
		