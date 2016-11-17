# -*- coding: UTF-8 -*-

import * from device

##
## @brief      Class for adaptador bluetooth.
##
## @param pin     The pin
## @param _id     The id
##
class AdaptadorBluetooth(Device):
	
	pin = 0
	_id = 0

	##
	## @brief      Constructs the object.
	##
	## @param      self  The object
	## @param      arg   The argument
	##
	def __init__(self, arg):
		super(adaptadorBluetooth, self).__init__()
		self.arg = arg
	
	##
	## @brief      { function_description }
	##
	## @return     { description_of_the_return_value }
	##
	def parear():
		return False

	##
	## @brief      { function_description }
	##
	## @return     { description_of_the_return_value }
	##
	def tornarVisivel():
		pass