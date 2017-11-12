while True:
    exp = [i for i in input() if i == '(' or i == ')']
    if not exp:
        break
    stack = ['.']
    for carac in exp:
        stack.append(carac)
        if stack[len(stack)-2] == '(' and stack[len(stack)-1] == ')':
            stack.pop(len(stack)-2)
            stack.pop(len(stack)-1)
    if len(stack) > 1:
        print("incorrect")
    else:
        print("correct")
    
  
