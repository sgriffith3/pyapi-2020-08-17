x = 11

y = 0

print(x + y)

print(x - y)

#print(x / y)

#print("You can't divide by Zero")


pi = "Raspberry"
#pi = 3.14
print(pi)
print(type(pi))    
try:
    #print(x / y)
    print(int(pi))
    print("Yay!")
#except ZeroDivisionError:
#    print("Zero cannot be divided by")
except ValueError:
    print("Boo!")
#except Exception as err:
#    print("There was a different exception")
#    print(f"The exception was {err}") 
else:
    print("Yay again!")
finally:
    print(x, y, pi)
print("There was no error or the error was handled")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
