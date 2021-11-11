from random import randint
import string

pole = "-" * 20;
npole = "-" * 20;
pozicep = "";
poziceh = ""


# citac = 0

def tah_pocitace(pole, pozicep):
    global npole

    print("Hraje pocitac")
    pozicep = randint(0, 19)  # ; citac = citac + 1

    if pole[pozicep] == "-":
        npole = pole[:pozicep] + 'o' + pole[pozicep + 1:]
        znovu = 0
    else:
        print("Tady neni volno ani pro pocitac!")
        znovu = 1
        tah_pocitace(pole, pozicep)
    if znovu == 0:
        print(npole)

    return pole[:pozicep] + 'o' + pole[pozicep + 1:]


def tah_hrace(pole, pozicep):
    print("Hraje hrac")
    poziceh = int(input("Zadej cislo pozice (0-19): "))

    global npole

    if pole[poziceh] == "-":  # pokud je misto na pozici
        npole = pole[:poziceh] + 'x' + pole[poziceh + 1:];  # citac = citac + 1
        znovu = 0
    else:
        print("Tady neni volno!")

        if pole[poziceh] == "o":
            print("Tady hraje protivnik!")
        if pole[poziceh] == "x":
            print("Tady jsi uz byl!")
        znovu = 1
        tah_hrace(pole, poziceh)
    if znovu == 0:
        print(npole)
    return pole[:poziceh] + 'x' + pole[poziceh + 1:]


def spusteni():
    while True:
        pole = npole
        tah_pocitace(pole, pozicep)

        pole = npole
        tah_hrace(pole, poziceh)
        pole = npole


spusteni()