
from calculator import add, subtract


functions = [add, subtract]

print("Available functions:")
for func in functions:
    print(func.__name__)  
