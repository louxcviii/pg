# vas program nacte ze souboru, ktery dostane jako argument z prikazove radky, text a vypise ho pozpatku
# vytvorte funkce pozpatku(), ktera jako parametr bere text a vraci ho pozpatku tzn "ahoj" -> "joha"
# osetrete chybove stavy pomoci try - except

import sys

def pozpatku(text):
    text_pozpatku = ""
    for znak in text:
        text_pozpatku = znak + text_pozpatku
    return text_pozpatku

if __name__ == "__main__":
    soubor = sys.argv[1]
    try:
        with open(soubor, "r") as s:
            obsah = s.read()
            print(pozpatku(obsah))
    except IndexError:
        print("Zadej nazev souboru")
    except FileNotFoundError:
        print("Soubor neexistuje")