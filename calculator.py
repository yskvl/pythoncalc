print("this will only work with 2 numbers")
print('what do you want to calculate?')
print("1: add")
print("2: subtract")
print('3: multiply')
print('4: divide')
while True:
    choice = input('add:1, subtract:2, multiply:3, divide:4, which one do you want? ')
    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input('first number: '))
        num2 = float(input('second number: '))
        
        if choice == '1':
            print(num1, 'plus', num2, 'equals', num1 + num2)
        
        elif choice == '2':
            print(num1, 'minus', num2, 'equals', num1 - num2)
        
        elif choice == '3':
            print(num1, 'multiplied by', num2, 'equals', num1 * num2)
        
        elif choice == '4':
            print(num1, 'divided by', num2, 'equals', num1 / num2)
        break
    else:
        print('enter a proper number')