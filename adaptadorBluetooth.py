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
	## @brief      Performs pairing with the device
	##
	## @return     Success or failure in pairing
	##
	def parear():
		return False

	##
	## @brief      Make the device visible
	##
	## @return     None
	##
	def tornarVisivel():
		pass
