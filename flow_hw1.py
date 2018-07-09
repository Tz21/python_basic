n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
op = input("operation(+,-,*,/): ")
if op == "+":
  result = n1 + n2
elif op == "-":
  result = n1 - n2
elif op == "*":
  result = n1 * n2
elif op == "/":
  result = n1 / n2
print("{0} {2} {1} = {3}".format(n1, n2, op, result))
