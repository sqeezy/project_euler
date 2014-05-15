result = []
a = 0
end = int(333)
while a < end:
    for b in range(a+1,500):
        for c in range(b+1,1000):
            if (a*a + b*b)==c*c:
                sum3 = a+b+c
                if sum3 == 1000:
                    result = [a,b,c,a*b*c]
                    break
    a+=1
print "a={} b={} c={} for a^2 + b^2 + c^2 = 1000 and a<b<c to be true.\n" \
      "There product is {}.".format(result[0],result[1],result[2],result[3])