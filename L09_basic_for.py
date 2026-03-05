# range()
for i in range(10):
	print(i)
else: 
	print()

for i in range(20, 30):
	print(i)
else: 
	print()

for i in range(0, 10 ,3):
	print(i)
else: 
	print()

# 九九乘法表
for i in range(1, 10):
	for j in range (1, i + 1):
		print(f"{j} x {i} = {i * j}", end = "\t")
	print()