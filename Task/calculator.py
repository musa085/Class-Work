#calculator tapsiqiq coin vermeyi unutmayin:)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Sifirdən bolmə mumkun deyil!"
    return a / b

def calculator():
    print("Kalkulyatora xoş gəlmisiniz!")
    print("Emeliyyatlar:")
    print("1. Toplama")
    print("2. Cixxma")
    print("3. Vurma")
    print("4. Bolmə")

    choice = input("Emeliyati secin (1/2/3/4): ")

    a = float(input("Birinci ededi daxil edin: "))
    b = float(input("İkinci ededi daxil edin: "))

    if choice == '1':
        print(f"Netice: {add(a, b)}")
    elif choice == '2':
        print(f"Netice: {subtract(a, b)}")
    elif choice == '3':
        print(f"Netice: {multiply(a, b)}")
    elif choice == '4':
        print(f"Netice: {divide(a, b)}")
    else:
        print("Yanlis secim etdiniz")


calculator()