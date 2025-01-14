class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()


def is_balanced_parentheses(string):

    my_stack=Stack()

    for i in range(len(string)):
        print(string[i])
        if string[i]=="(":
            my_stack.push("(")
        if string[i]==")":
            if my_stack.is_empty():
                print("no ok")
                return False
            else:
                my_stack.pop()

    if my_stack.is_empty():
        print("ok")
        return True
    else:
        print("no ok")
        return False
