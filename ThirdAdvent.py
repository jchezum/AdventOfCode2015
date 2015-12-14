class ThirdAdvent():
	def __init__(self):
		pass

	def inputFile(self):
		file = open('SecondAdventInput','r')
		directions=file.readlines()
		file.close()
        print directions
		return directions

    def main(self):
        self.inputFile()

ta=ThirdAdvent()
ta.main()

#
# case:
#
# current dimension is horizontal AND first symbol is right:
# current symbol is right -> +1
# current symbol is left -> nothing
# current symbol is up or down -> dimension is set to vertical
#
# current dimension is vertical AND first symbol is up:
# symbol is up -> +1
# symbol is down -> nothing
# symbol is left or right -> dimension is set to horizontal
#
#
# need to set a dimension and a direction
#
#
