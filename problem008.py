f = open("problem008-data.txt")
lines = f.read().replace("\n","")

maximum = 0
for i in range(5,len(lines)):
    try:
        test = lines[i-5:i]
        testProduct = 1
        for position in range(0,len(test)):
            testProduct *= int(test[position])
        if testProduct>maximum:
            maximum = testProduct
    except ValueError:
        raise ValueError("There is a not number in this file.")
print maximum
