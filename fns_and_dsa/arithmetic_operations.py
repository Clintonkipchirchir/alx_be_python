def perform_operation(num1, num2, operation):
    match operation:
        case "add":
           return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                print(f"ERROR:Division of {num2} is impossible")
            else:
             return num1 / num2
            
