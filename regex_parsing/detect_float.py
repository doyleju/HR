from re import match, compile

def is_float(number):
    expression = compile(r'^[+-]?[0-9]*\.[0-9]+$')
    return bool(expression.match(str(number)))
    # alternative without compile
    #return bool(match(r"^[+-]?[0-9]*\.[0-9]+$", str(number)))

num_lines = int(input())

for _ in range(num_lines):
    print(is_float(input()))
