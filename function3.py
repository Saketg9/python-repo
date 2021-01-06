def hello_world(num1, num2):            ### num1 = 36 , num2 = 77
    sum = num1 + num2                   ### sum = 36 + 77 
    return sum                          ### return 113

def get_value():
    num = int(input('Enter a value')) 
    return num

val1 = get_value()                      ### val1 = 36
val2 = get_value()                      ### val2 = 77

answer = hello_world(val1, val2)        ### hello_world(36, 77)  answer = 113
print('The answer is ' + str(answer))