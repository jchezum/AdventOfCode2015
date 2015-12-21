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
		print '----------------------------'
		for x in reindeer_stats_parsed:
			# print x[0],x[3],x[6],x[13]
			rate=int(x[3])
			duration=int(x[6])
			restTime=int(x[13])
			period=(self.total_race_duration/(duration+restTime))
			distance_travelled=rate*duration*(self.total_race_duration/(duration+restTime))
			extraDistance=0
			remaining_race_time=self.total_race_duration-(period*(duration+restTime))
			if remaining_race_time!=0:
				remainder=self.total_race_duration-remaining_race_time
				if remainder<duration:
					distance_travelled+=(rate*remainder)
				else:
					distance_travelled+=(rate*duration)

			# print period, distance_travelled,self.total_race_duration-period
			print (x[0]+'\t'+str(distance_travelled)).expandtabs(10)
		print '----------------------------'

		reindeer=self.reindeer_maker(reindeer_stats_parsed)

		currentTime=0
		while currentTime < self.total_race_duration:
			for d in reindeer:
				# if d.name=='djacuan':
				# 	print 'Before: ',d.name, d.secondsMoved,d.timeRested,d.distanceTraveled
				if d.secondsMoved<d.movementDuration:
					d.distanceTraveled+=d.rate
					d.secondsMoved+=1
					# print 'moving'
				elif d.timeRested<d.restDuration:
					d.timeRested+=1
					# print 'resting'
				else:
					d.secondsMoved=0
					d.timeRested=0
					# print 'resetting'
					# currentTime-=1 #not sure about this term
				# if d.name=='djacuan':
				# 	print 'After:  ',d.name, d.secondsMoved,d.timeRested,d.distanceTraveled
				# print '---------------------------------------'
			currentTime+=1

		maxDistance=0
		winningDeer=0
		for d in reindeer:
			print (d.name+'\t'+str(d.distanceTraveled)).expandtabs(10)
			if d.distanceTraveled > maxDistance:
				maxDistance=d.distanceTraveled
				winningDeer=d.name

		print '----------------------------'
		print winningDeer
		print maxDistance

fa=FourteenthAdvent()
fa.main()