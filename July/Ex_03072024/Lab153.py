print("--Start of the Program-- ")
try: 
    a = int(input("Enter a number 1: "))
    b = int(input("Enter a number 2: "))
    c = a/b #Zero Division
    print("Result: ", c)
except Exception as e:
    print(e)
    print("Please enter interger")

print("--End of the Program-- ")