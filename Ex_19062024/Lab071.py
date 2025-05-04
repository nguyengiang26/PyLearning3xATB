# Function scope
number = [1,2,3]

def do_something(number):
    number.append(100)
    number[0] = 123
    return number

number.append(10)
l = do_something(number)
print(l)
