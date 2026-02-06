a = float(input("Enter a Value"))
b = float(input("Enter a Value"))

def sub( a , b):
    return a - b

def add( a , b):
    return a + b 

def multi (a , b):
    return a * b 

 
def div (a , b):
    if b == 0:     
        raise ZeroDivisionError   
    else:
        return a / b
divide ( a , b)

print("""
1.add
2.sub
3.multi
4.divide""")

a = input("Enter a Number for calulation : ")
if a == 1:
    add()
elif a == 2:
    sub()
elif a == 3:
    multi()
elif a == 4:
    div()
i

