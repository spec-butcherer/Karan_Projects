#Happy Numbers - A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers. Display an example of your output here. Find first 8 happy numbers.

# 12 -> 5 -> 25 -> 29 -> 85 -> 89 - 
# 5655 -> 111 -> 3
count = 0
finished = False
for x in range(100): 
	number = x
	results = []
	while x != 1:
		y = str(x)
		z = 0
		
		for char in y:
			z += int(char)**2
		x = z
		if x == 1:
			count += 1
			print('count = ', count)
			print(number, ' = happy number')
			print(results, '\n')
			
			if count == 8:
				finished = True
		if x in results:
			break
		results.append(x)
	if finished:
		break
print("These were the first 8 happy numbers.")
