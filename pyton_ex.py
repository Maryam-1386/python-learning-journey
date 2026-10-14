print(walrus := False) # True

x=[x**2 for x in range(1,11)]
print(x)

y=[x for x in range(1,21) if x%3==0]
print(y)

names=["ali","sara","reza","mina"]
scores=[12,19,14,20]
Student=[{"name":name,"score":score}for name,score in zip(names,scores)]
print(Student)

numbers=[5,12,7,18,3,22,9,14,6,11]
numbers10=[x for x in numbers if x>=10]
square=[x**2 for x in numbers10]
print(square)

words=["ali","sara","reza","mina","mphmmad","zahra"]
list_Words=[x.capitalize() for x in words if len(x)>=4]
out_words=[{"Hello":name} for name in list_Words]
print(out_words)