# To create a custom exception class (must extend Exception)
# class EmptyStackException(Exception):
#    pass
# Note: 'pass' is a stub used for a class or method that does nothing;
# in this case, the class only exists to be raised and caught.


class Stack:
    def __init__(self):
        self.__stack = []

    # Stack operations - is_empty()
    def is_empty(self):
        if len(self.__stack) == 0:
            return True
        else:
            return False

    # push()
    def push(self, item):
        self.__stack.append(item)

    # pop()
    def pop(self):
        # Check that stack is not empty first or use try-except
        try:
            item = self.__stack.pop()
        except IndexError:
            print('Stack is empty!')
        else:
            # Successful pop!
            return item

    # peek()
    def peek(self):
        return self.__stack[len(self.__stack) - 1]

    # size()
    def size(self):
        return len(self.__stack)

    def __str__(self):
        string = ''
        for item in self.__stack:
            string += str(item) + ' '
        return string


def main():
    # reverse a list
    my_stack = Stack()
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(list1)):
        my_stack.push(list1[i])

    list1_reversed = []
    for i in range(len(list1)):
        list1_reversed.append(my_stack.pop())

    print("Original list:")
    print(list1)
    print("Reversed list:")
    print(list1_reversed)

    print('Checking that stack is empty...')
    print(my_stack.is_empty())
    print()

    # Match parentheses
    equation = input('Enter an equation:')
    matched = False
    for char in equation:
        if char == '(':
            my_stack.push(char)
        if char == ')':
            if my_stack.is_empty():
                matched = False
                break
            else:
                my_stack.pop()
                matched = True

    if my_stack.is_empty() and matched is True:
        print("Matched parentheses!")
    else:
        print('Unmatched parentheses!')

main()