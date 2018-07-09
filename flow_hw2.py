n = int(input("輸入一個正整數"))

square_root = n ** 0.5
print('平方根為：{}.'.format(square_root)) if square_root.is_integer() else print("平方根不為正整數")
