# TASKS
#-----------------------------------------#
# Filename: 		tasks.py
# Belongs To: 		keyModder
# Usage: 			from tasks import Tags
# Description:		Used to define XML elements and their function.
# Created: 			19 Nov 2014
# Modified: 		19 Nov 2014 
# Author: 			Shaun Wilesmith
# Notes:
#
#
#-----------------------------------------#

class Tags:

	def __init__(self):
		self.tags = {
			"tapkey": tapkey()
		}

	def parse(self,task):
		tag = task.tag
		
		self.tags[task.tag].required["index"] = True

		for key in self.tags[task.tag].required:
			if self.tags[task.tag].required[key]==True:
				if key not in task.attrib:
					print "ERROR: Required attribute '"+key+"' not found."  # TODO: Create a proper error handler
					exit();

		self.tags[task.tag].attrib = task.attrib
		call = self.tags[task.tag].run()


class tapkey:

	def __init__(self):
		self.required = {
			"key": True,
			"modifier": False
		}

	def run(self):
		cmd = "self.KeyboardEmulator.TapKey('"+self.attrib['key']+"'"
		if "modifier" in self.attrib:
			cmd = cmd + "," + self.attrib['modifier']
		cmd = cmd + ")"
		return cmd
