def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    sum=1
    for i in range(1,num+1):
        sum = sum*i
    return sum
print(factorial(0))
