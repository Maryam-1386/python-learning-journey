brick_company=int(input())
max=0
colorless=0
for i in range(brick_company):
    r,l= map(int, input().split())
    if l>max and l>r:
        max=l
    if r>max and r>l:
        max=r
    colorless+=abs(r-l)
Total_Brick=brick_company*(max+1)
print(Total_Brick-colorless)