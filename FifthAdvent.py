import re

class FifthAdvent():
	def __init__(self):
		pass

	def inputFile(self):
		file = open('Input\FifthAdventInput','r')
		unsortedWords=file.readlines()
		file.close()
		return unsortedWords

	def main(self):
		wordList=[]
		wordList=self.inputFile()
		print wordList

fa=FifthAdvent()
fa.main()


# (.*[aeiou].*[aeiou].*[aeiou].*)
# (\w)\1+
# ^/(?!ab|cd|pq|xy)([a-z0-9]+)$
#
#
# (.*[aeiou].*[aeiou].*[aeiou].*)|(\w)\1+
#
#
#
#
#
# -----------------------
# (.*ab.*)|(.*bc.*)|(.*pq.*)|(.*xy.*)