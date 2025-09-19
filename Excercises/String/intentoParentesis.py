def BracketMatcher(strParam):
    stack = []

    flag = False

    for char in strParam:

        if not stack:
            flag = False
        if char == ')':
            return 0
        elif char == '(':
            stack.append('(')
        else:
            if char == ')':
                stack.pop()
                flag = True
            elif char == '(':
                if flag:
                    return 0
                else:
                    stack.append('(')
    if not stack:
        return 1
    return strParam
    # keep this function call here 
print(BracketMatcher(input()))


