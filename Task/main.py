# main.py

# calculator.py faylından funksiyaları import edirik
from calculator import add, subtract

# Funksiyaları siyahıda göstərəcəyik
functions = [add, subtract]

# Funksiyaların siyahısını çap edirik
print("Available functions:")
for func in functions:
    print(func.__name__)  # funksiyanın adını çap edirik