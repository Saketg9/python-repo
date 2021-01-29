import sys

if len(sys.argv) != 4:
    print('\nUsage: ')
    print(f'{sys.argv[0]} <number> <number> <add|sub|mul|div>')
    print(f'For example: python3 {sys.argv[0]} 20 20 add\n')
    sys.exit()

def add(arg1, arg2):
    result = arg1 + arg2
    return result

def sub(arg1, arg2):
    result = arg1 - arg2
    return result

def mul(arg1, arg2):
    result = arg1 * arg2
    return result

def div(arg1, arg2):
    result = arg1 // arg2
    return result


num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
op = sys.argv[3]

if op == 'add':
    print(add(num1, num2))

elif op == 'sub':
    print(sub(num1, num2))

elif op == 'mul':
    print(mul(num1, num2))

elif op == 'div':
    print(div(num1, num2))

print(sys.argv)

# message = sys.argv[1]
# range = sys.argv[2]


# elif range() == arg1, arg2:
#     print(message())



