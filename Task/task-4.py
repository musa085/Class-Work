#tapsiriq-4 coin vermeyi unutmayin:)
with open("info.txt", "w") as file:
    file.write("Ad: Musa\n")
    file.write("Soyad: Bayramov\n")
    file.write("Yaş: 11\n")
    file.write("Hobby: Futbol\n")
    file.write("Dilller: English, Azerbaijani\n")


with open("info.txt", "r") as file:
    content = file.read()
    print(content)