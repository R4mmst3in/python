import sys
from collections import Counter

nums = [1,2,-3,4,-5]

for i in range(len(nums)):
	if nums[i] < 0:
		nums[i] = 0
print(nums)

nums = [1,2,-3,4,-5]
for idx, num in enumerate(nums):
	if num < 0:
		nums[idx]=0
print(nums)


squares=[]
for i in range(10):
	squares.append(i*i)
print(squares)

squares = [i*i for i in range(10)]
print(squares)


data = [3,5,6,7,8,9,5]
sorted_data = sorted(data)
print(data)

data = [{"name": "Max", "age": 8},
		{"name": "Lisa", "age": 3},
		{"name": "Rober", "age": 5},
		{"name": "Ruth", "age": 2},
		{"name": "Ben", "age": 3}]

print(data)

data_sorted = sorted(data, key=lambda x: x["age"])
print(sorted_data)


my_list = [1,10,21,762,135,4,84,59,46,447,127,135]
my_set = set(my_list)
print(sorted(my_set))

my_list = [i for i in range(100000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = [i for i in range(1200000)]
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

my_list=[2,2,2,2,3,4,5,6,7,8,9,9,9,9,10,10,10,11,11,12,12]
counter = Counter(my_list)

print(counter)
print(counter[11])


d1 = {"name": "Alex", "age": 23}
d2 = {"name": "Alex", "city": "Tokio"}
merged_dict = {**d1, **d2}
print(d1)
print(d2)
print(merged_dict)


colors = ["red","green","blue","pink","magenta"]
c = "blue"

if c in colors:
	print(f"{c} is in {colors}")
