j=[25,12,11,17,20,1]
sum=0
for i in j:
    sum+=i
print("sum=",sum)
avg=sum/len(j)
print(avg)
j.sort()
print("minimum=",j[0])
print("maximum=",j[-1])
