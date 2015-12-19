class deer():
	def __init__(self):
		pass

	name=''
	distance=0
	rate=0
	movementDuration=0
	restDuration=0
	periods=0

	distanceTraveled=0
	secondsMoved=0
	timeRested=0
	state='Moving'

	def get_name(self):
		return self.name

	def set_name(self,value):
		self.name=value

class FourteenthAdvent():
	def __init__(self):
		pass

	total_race_duration=2503
	reindeer=[]

	def inputFile(self):
		file = open('Input\FourteenthAdventInput','r')
		reindeer_stats=file.readlines()
		file.close()
		return reindeer_stats

	def parse_deer_stats(self,reindeer_stats):
		stats_parsed=[]
		for x in reindeer_stats:
			elements=[]
			elements=x.split(' ')
			stats_parsed.append(elements)
		return stats_parsed

	def reindeer_maker(self, list):
		deer_list=[]
		for x in list:
			newDeer=deer()
			newDeer.set_name(x[0])
			newDeer.rate=int(x[3])
			newDeer.movementDuration=int(x[6])
			newDeer.restDuration=int(x[13])
			deer_list.append(newDeer)
		return deer_list

	def main(self):
		reindeer_stats=[]
		reindeer_stats_parsed=[]
		reindeer=[]
		reindeer_stats=self.inputFile()

		reindeer_stats_parsed=self.parse_deer_stats(reindeer_stats)
		# for x in reindeer_stats_parsed:
		# 	print x[0],x[3],x[6],x[13]

		reindeer=self.reindeer_maker(reindeer_stats_parsed)

		currentTime=0
		while currentTime < self.total_race_duration:
			for d in reindeer:
				if d.state=='Moving' and d.secondsMoved<d.movementDuration:
					d.distanceTraveled=d.distanceTraveled+d.rate
					d.secondsMoved+=1
				else:
					d.state='Resting'
					d.secondsMoved=0

				if d.state=='Resting' and d.timeRested<d.restDuration:
					d.timeRested+=1
				else:
					d.state='Moving'
					d.timeRested=0
				# print d.name, d.secondsMoved,d.timeRested,d.state,d.distanceTraveled
				# print '---------------------------------------'
			currentTime+=1


		maxDistance=0
		winningDeer=0
		for d in reindeer:
			print d.name, d.distanceTraveled
			if d.distanceTraveled > maxDistance:
				maxDistance=d.distanceTraveled
				winningDeer=d.name

		print '----------------------------'
		print winningDeer
		print maxDistance

fa=FourteenthAdvent()
fa.main()