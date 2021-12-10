class Stack:


    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def main():
    s = Stack()
    #Create an stack, and check if it empty
    print(s.isEmpty())

    # Push an item to the stack & check it is no longer empty
    s.push(1)
    print(s.isEmpty())

    #Return the top of the stack (Dont pop, just view/peek at the top of the stack)
    print(s.peek())

    # Return the top of the stack. The stack should now be empty
    print(s.pop())
    print(s.isEmpty())

if __name__ == "__main__":
    main()