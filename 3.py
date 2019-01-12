def Solution(A, B, M, X, Y):
	trips=0
	sum_weight=0
	sum_people=0
	elevator_floors=[]
	elevator_moves=0
	for person in range(len(A)):
		if (sum_weight+A[person]<Y) and (sum_people+1<=X) and (person!=len(A)-1):
			sum_weight += A[person]
			sum_people += 1
			if B[person] not in elevator_floors: elevator_floors.append(B[person])
		else:
			if (person==len(A)-1) and (B[person] not in elevator_floors): elevator_floors.append(B[person])	
			trips += len(elevator_floors)+1
			sum_weight=A[person]
			sum_people=1
			elevator_floors=[B[person]]	
	return (trips)

#Test
A=[40,40,100,80,20]
B=[3,3,2,2,3]
print (Solution(A,B,3,5,200))			