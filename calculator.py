import re

def allowed_chars(s):
    return re.match(r'^[0-9+\-*/.() ]*$', s)

def print_equation(nums, ops):
    for n in range(len(nums)):
        print(nums[n], end="")
        if n < len(ops):
            print(ops[n], end="")
    print("")

def calculate_expression(nums, ops, show_steps=False):
    operator_precedence = ["/", "*", "+", "-"]
    result = 0.0
    #print(f"Calculating expression: Numbers: {nums}, Operators: {ops}")
    for j in range(4):
        i = 0
        while i < len(ops):
            if ops[i] == operator_precedence[j]:
                if show_steps:
                    print_equation(nums, ops)
                try:
                    if ops[i] == "/":
                        result = float(nums[i]) / float(nums[i + 1])
                    elif ops[i] == "*":
                        result = float(nums[i]) * float(nums[i + 1])
                    elif ops[i] == "+":
                        result = float(nums[i]) + float(nums[i + 1])
                    elif ops[i] == "-":
                        result = float(nums[i]) - float(nums[i + 1])
                except ZeroDivisionError:
                    if show_steps:
                        print("Error: Division by zero.")
                    return None
                
                if show_steps:
                    print(f"Calculating: {nums[i]} {ops[i]} {nums[i + 1]} = {result}")

                nums[i] = str(result)
                del nums[i + 1]
                del ops[i]
                i = i - 1
                if len(ops) == 0:
                    break
            i += 1
    return nums[0]

def calculate(expression, show_steps=False):
    # Handle parentheses by creating arrays for nested expressions 
    #first check that parentheses are balanced
    expression = expression.replace(" ", "")

    opencount = 0
    closedcount = 0
    for char in expression:
        if char == "(":
            opencount += 1
        elif char == ")":
            closedcount += 1
        if closedcount > opencount:
            if show_steps:
                print("Error: Unbalanced parentheses.")
            return None
        
    if opencount != closedcount:
        if show_steps:
            print("Error: Unbalanced parentheses.")
        return None

    delimiters = r"[-+*/()]"
    nums = re.split(delimiters, expression)
    ops = re.findall(delimiters, expression)

    if show_steps:
        print_equation(nums, ops)
        print(f"Initial split: Numbers: {nums}, Operators: {ops}")

    #Evaluate parentheses first
    while "(" in ops:
        open_index = None
        close_index = None
        for i in range(len(ops)):
            if ops[i] == "(":
                open_index = i
            elif ops[i] == ")":
                close_index = i
                break
        if open_index is not None and close_index is not None:
            sub_nums = nums[open_index + 1:close_index + 1]
            sub_ops = ops[open_index + 1:close_index]
            if show_steps:
                print(f"Evaluating parentheses: Numbers: {sub_nums}, Operators: {sub_ops}")
            sub_result = calculate_expression(sub_nums, sub_ops, show_steps)
            if sub_result is None:
                return None
            # Replace the parenthesized section with the result
            nums = nums[:open_index] + [str(sub_result)] + nums[close_index + 1:]
            ops = ops[:open_index] + ops[close_index + 1:]
            # Remove empty strings from nums
            # Only remove blank strings between open_index and close_index (the updated section)
            updated_section = [n for n in nums[open_index:open_index + 2] if n != '']
            nums = nums[:open_index] + updated_section + nums[open_index + 2:]
            if show_steps:
                print(f"After evaluating parentheses: Numbers: {nums}, Operators: {ops}")
        else:
            if show_steps:
                print("Error: Unbalanced parentheses.")
            return None

    result = 0.0
    if show_steps:
        print(f"Evaluating final expression: Numbers: {nums}, Operators: {ops}")

    if len(ops) > 0:
        result = calculate_expression(nums, ops)
        if result is not None:
            if show_steps:
                print(f"Final result: {result}")
            return str(result)
    else:
        if show_steps:
            print(f"Final result: {nums[0]}")
        return nums[0]

if __name__ == "__main__":
    """
    while True:
        exp = input("Enter calculation (or 'exit' to quit): ")
        if exp.lower() in ['exit', 'quit', 'q', 'e', '']:
            break
        if not allowed_chars(exp):
            print("Invalid characters in expression. Please use only numbers and +, -, *, /, ., (, ) operators.")
            continue
        show_steps = True

        print(calculate(exp, True))
    """

    calculate("((2+6)*4)-5", True)





