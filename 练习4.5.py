digit=[]
sum=0
for i in range(1,100000+1):
    digit.append(i)
    sum=sum+i
print(f"最小数是{min(digit)}")
print(f"最大数是{max(digit)}")
print(f"1到100000的和为：{sum}")