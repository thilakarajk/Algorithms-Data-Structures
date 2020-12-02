from ds.stack.implementation import Stack

expression = "{}[]()[({})]"
TOKENS = [['{', '}'], ['(', ')'], ['[', ']']]
expression_list = list(expression)


def is_open_bracket(char):
    for brackets in TOKENS:
        if brackets[0] == char:
            return True
    return False


def is_matched(open_term, close_term):
    for brackets in TOKENS:
        if brackets[0] == open_term:
            return brackets[1] == close_term
    return False


def check_paranthesis(expr_list):
    stack = Stack()
    for char in expr_list:
        if is_open_bracket(char):
            stack.push(char)
        else:
            if stack.empty() or not is_matched(stack.pop(), char):
                return False
    return stack.empty()


print(check_paranthesis(expression_list))
