# stack
stack = [None]*6
top = -1

def is_empty():
    return top == -1

def isfull():
    return top == len(stack)-1

def push(number):
    global top

    if not isfull() :
       top += 1
       stack[top] = number

    else:
        print("stak is full")

def pop():
    global top 

    if not is_empty():
        stack[top] = None
        top -= 1

    else:
        print("stack is empty")

# queue

queue = [None]*6
front = -1
rear = -1

def is_full_queue():
    return rear == len(queue)-1

def is_empty_queue():
    return front == rear

def push_queue(number):
    global rear , front

    if not is_full_queue():
        rear += 1
        queue[rear] = number

    else:
        print("queue is full")

def pop_queue():
    global rear , front
    if not is_empty_queue():
        front += 1
        queue[front] = None

    else:
        print("queue is empty")


#test stack
print("test stack")
push(10)
push(20)
push(30)
pop()
print(stack)
pop()
pop()
pop()

#test queue

print("\ntest queue")
pop_queue()
push_queue(10)
push_queue(20)
push_queue(30)
print(queue)
pop_queue()
print(queue)
pop_queue()
pop_queue()
pop_queue()
print(queue)