max=int(input("Enter number:"))
while True:
    number=input("Enter number:")
    if number=="exit":
        break
    if int(number) > int(max):
      max=number


print(f"Max is {max}")