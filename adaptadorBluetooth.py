# -*- coding: UTF-8 -*-

import * from device

##
## @brief      Classe para adaptador bluetooth.
##
class AdaptadorBluetooth(Device):
	

	##
	## @brief      Constrói o objeto.
	##
	## @param      self  O objeto
	## @param      arg   O argumento
	##
	def __init__(self, arg):
		super(adaptadorBluetooth, self).__init__()
		self.arg = arg
		