#  find the first occurrence of an alphanumeric character in (read from left to right) that has consecutive repetitions.
# Sample Input
# ..12345678910111213141516171820212223
# Sample Ouput
# 1

from re import search, match, compile
line = input()

expression = compile(r"([a-zA-Z0-9])\1+")
m = expression.search(line)

#m = search(r'([a-zA-Z0-9])\1', line)
print(m.group(1) if m else -1)
