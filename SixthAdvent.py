import re
import os

# http://adventofcode.com/day/6
class SixthAdvent():
	def __init__(self):
		pass

	def inputFile(self):
		file = open('Input\SixthAdventInput','r')
		rawInstructions=file.readlines()
		file.close()
		return rawInstructions

	def main(self):
		master_instruction_list=[]
		master_instruction_list=self.inputFile()
		print master_instruction_list


sa=SixthAdvent()
sa.main()