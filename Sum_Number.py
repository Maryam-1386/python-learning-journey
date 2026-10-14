number= int (input())
sum=0
number1=number+1
for i in range(1,number1):
    if i!=1:
      print(f" {i} ",end='')
    else:
       print(f"{i} " ,end='')
    sum+=i
    if i<number:
        print("+",end='')

print("=",sum)