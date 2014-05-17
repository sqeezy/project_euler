f = open("problem013-data.txt",'r')
nums = []
for line in f:
    nums.append(int(line))
print sum(nums)