import re

def allowed_chars(s):
    return re.match(r'^[0-9+\-*/.() ]*$', s)

def print_equation(nums, ops):
    for n in range(len(nums)):
        print(nums[n], end="")
        if n < len(ops):
            print(ops[n], end="")
    print("")

def calculate_expression(nums, ops, show_steps=True):
    operator_precedence = ["/", "*", "+", "-"]
    result = 0.0
    #print(f"Calculating expression: Numbers: {nums}, Operators: {ops}")
    for j in range(4):
        i = 0
        while i < len(ops):
            if ops[i] == operator_precedence[j]:
                print(nums, ops)
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

def calculate(expression, show_steps=True):
    delimiters = r"[-+*/()]"
    nums = re.split(delimiters, expression)
    ops = re.findall(delimiters, expression)

    print_equation(nums, ops)

    # Find and evaluate innermost parentheses
    while "(" in ops:
        open_index = None
        close_index = None
        for i, op in enumerate(ops):
            if op == "(":
                open_index = i
            elif op == ")" and open_index is not None:
                close_index = i
                break
        if open_index is not None and close_index is not None:
            sub_nums = nums[open_index + 1:close_index + 1]
            sub_ops = ops[open_index + 1:close_index]
            # If there is no operator inside the parentheses, just use the number
            if not sub_ops:
                result = sub_nums[0]
            else:
                result = calculate_expression(sub_nums, sub_ops)
                if result is None:
                    break
            # Replace the evaluated parentheses with the result
            nums = nums[:open_index] + [str(result)] + nums[close_index + 1:]
            ops = ops[:open_index] + ops[close_index + 1:]
            if show_steps:
                print("After evaluating parentheses:")
                print_equation(nums, ops)
        else:
            print("Error: Unmatched parentheses.")
            break

    result = 0.0
    #print(f"Evaluating final expression: Numbers: {nums}, Operators: {ops}")
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
    print(calculate("3+5+5+2"))
    """
    while True:
        exp = input("Enter calculation (or 'exit' to quit): ")
        if exp.lower() in ['exit', 'quit', 'q', 'e', '']:
            break
        if not allowed_chars(exp):
            print("Invalid characters in expression. Please use only numbers and +, -, *, /, ., (, ) operators.")
            continue
        show_steps = True
        exp = exp.replace(" ", "")

        # Handle parentheses by creating arrays for nested expressions 
        #first check that parentheses are balanced
        opencount = 0
        closedcount = 0
        for char in exp:
            if char == "(":
                opencount += 1
            elif char == ")":
                closedcount += 1
            if closedcount > opencount:
                print("Error: Unbalanced parentheses.")
                break

        if opencount != closedcount:
            print("Error: Unbalanced parentheses.")
            continue

        delimiters = r"[-+*/()]"
        operator_precedence = ["/", "*", "+", "-"]
        nums = re.split(delimiters, exp)
        ops = re.findall(delimiters, exp)

        if len(nums) - 1 != len(ops):
            print("Error: Mismatched numbers and operators.")
            continue

        print(calculate(exp))
        """





