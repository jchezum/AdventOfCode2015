class SecondAdvent():
	def __init__(self):
		pass

	dimensions=length=width=height=0
	def inputFile(self):
		file = open('Input\SecondAdventInput','r')
		dimensions=file.readlines()
		file.close()
		return dimensions

	def dimensioner(self,dimensions):
		d=dimensions.split('x')
		dims=[]
		for side in d:
			dims.append(int(side))
		return dims

	def small_side(self,sideTheFirst,sideTheSecond,sideTheThird):
		sides=[sideTheFirst,sideTheSecond,sideTheThird]
		smallestSide=min(sides)
		# for x in sides:
		# 	print x
		# print smallestSide
		# print '==================================='
		return smallestSide

	def smallest_edges(self,sides):
		set_of_sides=[]
		for x in sides:
			set_of_sides.append(x)
		smallest_edge=min(sides)
		largest_edge=max(sides)
		set_of_sides.remove(smallest_edge)
		set_of_sides.remove(largest_edge)
		middle_edge=set_of_sides[0]
		return [smallest_edge,middle_edge]

	def perimeter(self,small_edges):
		l=small_edges[0]
		w=small_edges[1]
		edgeTheFirst=2*l
		edgeTheSecond=2*w
		perimeter=edgeTheFirst+edgeTheSecond
		# print 'Per Package Perimeter: %s' %perimeter
		return perimeter

	def volume(self,sides):
		volume=sides[0]*sides[1]*sides[2]
		return volume

	def area(self,sides):
		l=sides[0]
		w=sides[1]
		h=sides[2]
		sideTheFirst=2*l*w
		sideTheSecond=2*w*h
		sideTheThird=2*l*h
		surface_area=sideTheFirst+sideTheSecond+sideTheThird
		total_area=surface_area+(.5*self.small_side(sideTheFirst,sideTheSecond,sideTheThird))
		# print 'Per Package Area: %s' %total_area
		# print '==================================='
		return total_area

	def main(self):
		dims=l=w=h=packageArea=totalArea=0
		totalBow=0
		area_of_packages=[]
		length_of_bow=[]
		package_sizes=self.inputFile()
		for x in package_sizes:
			sides=self.dimensioner(x)
			# Wrapping Paper
			packageArea=self.area(sides)
			area_of_packages.append(packageArea)
			# Ribbon
			small_edges=self.smallest_edges(sides)
			packagePerimeter=self.perimeter(small_edges)
			packageVolume=self.volume(sides)
			length_of_bow.append(packagePerimeter+packageVolume)

		for package in area_of_packages:
			totalArea=totalArea+package
		print 'Total sq ft of paper: %s' %totalArea

		for gift in length_of_bow:
			totalBow=totalBow+gift
		print 'Total length of ribbon: %s' %totalBow

sa=SecondAdvent()
sa.main()