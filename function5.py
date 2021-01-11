def hello_world(num1, num2):            ### num1 = 36 , num2 = 77
    sum = num1 + num2                   ### sum = 36 + 77 
    return sum                          ### return 113

def sub(num1, num2):                    ### num1 = 36 , num2 = 77
    sub = num1 - num2                   ### sub = 36 - 77 
    return sub

def mul(num1, num2):                    ### num1 = 35 , num2 = 77
    mul = num1 * num2                   ### mul = 35 * 77
    return mul

def div(num1, num2):                    ### num1 = 35 , num2 = 77
    div = num1 / num2                   ### div = 35 / 77
    return div

def pow(num1, num2):                    ### num1 = 35 , num2 = 77
    pow = num1 ** num2                  ### pow = 35 ** 77
    return pow

def get_value():
    num = int(input('Enter a value')) 
    return num

val1 = get_value()                      ### val1 = 36
val2 = get_value()                      ### val2 = 77

answer = hello_world(val1, val2)                          ### hello_world(36, 77) answer = 113
print('The answer of addition is ' + str(answer))   


answer = sub(val1, val2)                                  ### sub(36, 77) answer = -44
print('The answer of subtraction  is ' + str(answer))


answer = mul(val1, val2)                                  ### mul(36, 77) answer = 2541
print('The answer of multiplication is ' + str(answer))


answer = div(val1, val2)                                  ### div(36, 77) answer = 0.42857142857142855
print('The answer of division is ' + str(answer))


answer = pow(val1, val2)                                  ### pow(36, 77) answer =
print('The answer of power is ' + str(answer))