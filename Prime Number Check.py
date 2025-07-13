
num = int(input(" Enter a number?"))

def function_is_prime(num):
    for divisor in range(2, num):
        if num%divisor == 0:
            print(num, " is not prime number")
            break
        else:
             print(num, " is prime number")
             break


function_is_prime(num)


