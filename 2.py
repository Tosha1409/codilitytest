def Solution(T):
	cities=len(T)-1
	paths=[0] * cities
	x=0
	while True:
		capital=x
		if (x>cities) or (x==T[x]): break
		x +=1

	for x in range(len(T)):
		if (x != capital):
			y=x
			distance=0;
			while (T[y] != capital) and (distance<len(paths)-1):
				distance += 1
				y=T[y]
			distance += 1
			paths[distance-1] += 1
	return(paths)			
	

#Tests
M = [9, 1, 4, 9, 0, 4, 8, 9, 0, 1]
M1 = [0]
M2 = [0, 0]
M3 = [0, 0, 1]
print (Solution (M))
print (Solution (M1))
print (Solution (M2))
print (Solution (M3))