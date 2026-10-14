
def prime (number):
    if number<=1:
        return False
    else:
        for i in range (2,number) :
         if number%i==0:
               return False
        
        return True

number=int(input())
sumNumber=0
number1=abs(number)
#abs = absoulute value قدرملق عدد رو بر میگردونه
number2=number
while(number1>0):
 sumNumber+=number1%10
 number1//=10
while sumNumber>0:
   number2+=1
   if prime(number2):
      sumNumber-=1
print(number2)
