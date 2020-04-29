#guess#s
import random
r = random.randint(1,100)
count = 0

while True:

	count += 1 #就是count = count + 1的意思
	a = input('請猜一個數字')
	a = int(a)

	if a == r:
		print("終於猜對了，恭喜你總共猜了", count, '次')
		break

	elif a > r:
		print("再小，你猜了第", count, "次")

	elif a < r:
		print('再大，你猜了第', count, '次')