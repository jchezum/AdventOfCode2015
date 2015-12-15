import hashlib

class FourthAdvent():
	def __init__(self):
		pass

	def hashGen(self,seedString):
		m=hashlib.md5()
		m.update(seedString)
		return m.hexdigest()

	def main(self):
		base='iwrupvqb' #346387
		# base='abcdef'
		seed=0
		hashValue=''
        #For challenge 1, use [0:5]='00000'
		while hashValue[0:6]!='000000':
			seedString=base+str(seed)
			hashValue=self.hashGen(seedString)
			seed=seed+1
			print hashValue

		print 'Winning hash is: %s' %hashValue
		finalSeed=seed-1
		print 'Seed value is: %s' %finalSeed


fa=FourthAdvent()
fa.main()