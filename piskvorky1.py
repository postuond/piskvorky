from random import randint

pole = "-" * 20
konec = 0

def tah_pocitace(pole):
    pozicep = randint(0, 19)
    pole = pole[:pozicep] + 'o' + pole[pozicep + 1:]
    return pole

def tah_hrace(pole):
    poziceh = int(input("Zadej cislo cislo pozice (0-19): "))
    if pole[poziceh] == "-":#pokud je misto na pozici
        pole = pole[:poziceh] + 'x' + pole[poziceh + 1:]

    else:
        print("Tady neni volno!")
        print(pole)
    if pole[poziceh] == "o":
        print("Tady hraje protivnik!")

    return pole

def spusteni():
    while True:
        tah_pocitace("hraje pocitac")
        print(tah_pocitace(pole))
        tah_hrace("hraje hrac")
        print(tah_hrace(pole))

spusteni()



