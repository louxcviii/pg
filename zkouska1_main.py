# prace s operatory

def operace(operator, a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Nelze delit nulou"
        else:
            return a / b
    
if __name__ == "__main__":
    print(operace("+", 1, 2))  # 3
    print(operace("-", 2, 1))  # 1
    print(operace("*", 0, 5))  # 0
    print(operace("/", 4, 2))  # 2