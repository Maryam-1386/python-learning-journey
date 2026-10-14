def reverse_Number(number):
    reverse=0
    while number>0:
        digit=number%10
        reverse=reverse*10+digit
        number/=10
    print(reverse) 
number=int(input("Enter Number: "))
print("Reverse Number is ",reverse_Number(number))
