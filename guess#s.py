#guess#s
import random
r = random.randint(1,100)

while True:

	a = input('請猜一個數字')
	a = int(a)

	if a == r:
		print("終於猜對了")
		break

	elif a > r:
		print('再小')

	elif a < r:
		print('再大')