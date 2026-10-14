tasks=[
    {"title":"learn Python","done":False},
    {"title":"Backend practice","done":True}
]
for task in tasks:
    if task["done"]==True:
        status="The work is finished "
    else:
        status="work is still going on "
    print(f"{task["title"]}:{status}")

def add_task():
    title=input("Enter New title:").strip()
    if len(title)!=0:
        tasks.append({"title":title,"done":False})
        print(f"added title:{title}")
    else:
        print("title can not null")
    
while True:
    choice=input("choose one options:\n1:Show\n2:Add task\n3:Exit \n")
    if choice=="1":
        for i,task in enumerate(tasks):
            print(f"{i+1}-{task["title"]}")
    elif choice=="2":
        add_task()
    elif choice=="3":
        print("Bay!")
        break
    else:
        print("please choice 1 or 2 or 3")