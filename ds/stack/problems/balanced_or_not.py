from ds.stack.implementation import Stack

TOKENS = ['<','>']

def is_open_tag(char):
    return TOKENS[0] == char

def is_matching(open_tag, close_tag):
    return TOKENS[0] == open_tag and TOKENS[1] == close_tag

def compare(expression, replacement):
    stack = Stack()
    for char in list(expression):
        if is_open_tag(char): # open tag
            stack.push(char)
        else:
            if stack.is_empty() and replacement == 0:
               return 0
            else:
                if replacement == 0:
                    return 0
                if stack.is_empty() or not is_matching(stack.pop(), char):
                    replacement -= 1
    return 1 if stack.size == 0 else 0

def balancedOrNot(expressions, maxReplacements):
    output_list = []
    for expression, replacement in zip(expressions,maxReplacements):
        output_list.append(compare(expression, replacement))
    return output_list

result = balancedOrNot(["<<>>>","<>>>>"],[0,2])
result = map(str, result)
print("\n".join(result))