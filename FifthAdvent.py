import re
import os

class FifthAdvent():
	def __init__(self):
		pass

	def inputFile(self):
		file = open('Input\FifthAdventInput','r')
		unsortedWords=file.readlines()
		cleanedWords=[]
		for x in unsortedWords:
			x.rstrip('\n')
			cleanedWords.append(x)
		file.close()
		return cleanedWords

	def filter(self,pattern,list):
		filteredList=[]
		for word in list:
			if re.match(pattern,word):
				filteredList.append(word)
		return filteredList

	def main(self):
		wordList=[]
		wordList=self.inputFile()

		# print wordList

		vowelsPattern='(.*[aeiou]){3}'
		doublePattern='(.)\\1'
		substringPattern='(.*ab.*)|(.*bc.*)|(.*pq.*)|(.*xy.*)'
		filtered_word_list_1=[]
		filtered_word_list_2=[]
		filtered_word_list_3=[]
		filtered_word_list_1=self.filter(vowelsPattern,wordList)
		filtered_word_list_2=self.filter(doublePattern,filtered_word_list_1)
		filtered_word_list_3=self.filter(substringPattern,filtered_word_list_2)

		print len(wordList),len(filtered_word_list_1),len(filtered_word_list_2),len(filtered_word_list_3)

		# remove all matches of regex 3 from the final set
		for word in filtered_word_list_3:
			if word in filtered_word_list_2:
				filtered_word_list_2.remove(word)

		print len(wordList),len(filtered_word_list_1),len(filtered_word_list_2),len(filtered_word_list_3)

		# Note: number returned (23) is too low currently...don't really know how to deal with that as my regexs
		# are essentially the same as the ones in the solution thread...
		# https://www.reddit.com/r/adventofcode/comments/3viazx/day_5_solutions/

fa=FifthAdvent()
fa.main()

# [aeiou].*[aeiou].*[aeiou]
# (.*[aeiou].*[aeiou].*[aeiou].*)
# (\w)\1+
# ^/(?!ab|cd|pq|xy)([a-z0-9]+)$
#
#
# (.*[aeiou].*[aeiou].*[aeiou].*)|(\w)\1+
#
#
#(.*[aeiou].*){3}
#
#
# -----------------------
# (.*ab.*)|(.*bc.*)|(.*pq.*)|(.*xy.*)