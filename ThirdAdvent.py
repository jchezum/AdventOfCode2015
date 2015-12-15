class home():
	def __init__(self):
		pass

	symbol=0
	x_pos=0
	y_pos=0

	def set_symbol(self,direction):
		self.symbol=direction
	def get_symbol(self):
		return self.symbol
	def set_x(self,direction):
		self.x_pos=direction
	def get_x(self):
		return self.x_pos	
	def set_y(self,direction):
		self.y_pos=direction
	def get_y(self):
		return self.y_pos
	
class ThirdAdvent():
	def __init__(self):
		pass

	# directions=[]
	def inputFile(self):
		file = open('Input\ThirdAdventInput','r')
		directions=file.readline()
		file.close()
		return directions

	def splitList(self,directions):
		inputLength=len(directions)
		santasList=''
		roboSantasList=''
		for symbol in range(0,inputLength):
			if symbol%2==0:
				santasList=santasList+directions[symbol]
			else:
				roboSantasList=roboSantasList+directions[symbol]
		return santasList,roboSantasList

	def create_homes(self,houseList,directions):
		x=y=0
		inputLength=len(directions)
		for symbol in range(0,inputLength):
			house=home()
			house.set_symbol(directions[symbol])
			if directions[symbol]=='>':
				x=x+1
			elif directions[symbol]=='<':
				x=x-1
			elif directions[symbol]=='^':
				y=y+1
			elif directions[symbol]=='v':
				y=y-1
			house.set_x(x)
			house.set_y(y)
			houseList.append(house)
		return houseList

	def count_total_homes_visited(self,homeList,directions,total_homes_visited):
		visitedLocations=['0,0']
		total_gifts=0
		for x in homeList:
			coordinates=str(x.x_pos)+','+str(x.y_pos)
			if coordinates not in visitedLocations:
				total_homes_visited=total_homes_visited+1
				visitedLocations.append(coordinates)
		return total_homes_visited

	def main(self):
		# directions='^v^v^v^v^v'
		directions='^>v<'
		# directions='^^v^v^'
		homeList=[]
		total_homes_visited=1
		# directions=self.inputFile()
		homeList=self.create_homes(homeList,directions)
		total_homes_visited=self.count_total_homes_visited(homeList,directions,total_homes_visited)

		santasList=''
		roboSantasList=''
		santasList,roboSantasList=self.splitList(directions)
		print 'Santa: %s' %santasList
		print 'RoboSanta: %s' %roboSantasList

		#Santa
		#-------------------------------------------------------------
		total_homes_santa=1
		SantasHomeList=[]
		SantasHomeList=self.create_homes(SantasHomeList,santasList)
		# total_homes_santa=self.count_total_homes_visited(SantasHomeList,santasList,total_homes_santa)

		#RoboSanta
		#-------------------------------------------------------------
		total_homes_roboSanta=0
		RoboSantasHomeList=[]
		RoboSantasHomeList=self.create_homes(RoboSantasHomeList,roboSantasList)

		#De-duplication to remove homes both visited
		sCoordList=[]
		rsCoordList=[]
		for x in SantasHomeList:
			sCoordList.append(str(x.x_pos)+','+str(x.y_pos))
		for x in RoboSantasHomeList:
			rsCoordList.append(str(x.x_pos)+','+str(x.y_pos))

		duplicates=0
		for x in sCoordList:
			if x in rsCoordList:
				duplicates=duplicates+1

		total_homes_roboSanta=self.count_total_homes_visited(RoboSantasHomeList,roboSantasList,total_homes_roboSanta)
		total_homes_santa=self.count_total_homes_visited(SantasHomeList,santasList,total_homes_santa)

		print 'Total number of homes Santa visits: %s' %total_homes_santa
		print 'Total number of homes RoboSanta visits: %s' %total_homes_roboSanta
		print 'Total number of homes both visit: %s' %duplicates
		total=total_homes_roboSanta+total_homes_santa-duplicates
		print 'Total houses visited this year: %s' %total

		print 'Total homes visted last year: %s' %total_homes_visited


ta=ThirdAdvent()
ta.main()

