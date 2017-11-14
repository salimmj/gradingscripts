SET1 = set([(1, 3),(1, 4),(2, 3),(2, 1),(3, 3),(4, 2)])
SET2 = set([(1, 2),(1, 1),(2, 3),(2, 1),(3, 2),(4, 1)])

while True:
	list1 = input("first list: ")
	list2 = input("second list: ")
	list1 = ''.join([c for c in list1 if c!=' '])
	list2 = ''.join([c for c in list2 if c!=' '])

	list1 = list1[1:-1].strip().split("),")
	list1[-1] = list1[-1][:-1]
	for i,x in enumerate(list1):
		list1[i] = x[1:].split(',')
		list1[i] = (int(list1[i][0]),int(list1[i][1]))

	list2 = list2[1:-1].strip().split("),")
	list2[-1] = list2[-1][:-1]
	for i,x in enumerate(list2):
		list2[i] = x[1:].split(',')
		list2[i] = (int(list2[i][0]),int(list2[i][1]))

	list1 = set(list1)
	list2 = set(list2)
	print(list1)
	print(list2)
	# list1 variables
	n_1 = len(list1)
	mis_1 = len(SET1 - list1)
	inc_1 = len(list1-SET1)

	# list2 variables
	n_2 = len(list2)
	mis_2 = len(SET2 - list2)
	inc_2 = len(list2-SET2)

	### debugging

	grade = 15

	grade -= mis_1 + mis_2+ min(3, max(inc_1-mis_1,0) + max(inc_2-mis_2,0)) 

	print("len: {}\nmis_1: {}\ninc_1: {}\nlen: {}\nmis_1: {}\ninc_1: {}\ngrade: {}\n".format(n_1,mis_1,inc_1, n_2, mis_2, inc_2, grade))

# {(11,11),(22,22),(33,33),(44,44),(55,66),(66,77),(33,22),(55,44)}
# {(11,11),(22,22),(33,33),(1,1)}