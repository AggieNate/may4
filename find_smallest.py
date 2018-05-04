

array = [5,13,53,2,45]
min = array[0]

for num in range(0,len(array)):
	if array[num] < min:
		min = array[num]

print(min)

