# Funkce, která vrátí True, pokud je zadané číslo prvočíslo, jinak False
def je_prvocislo(cislo):
    if cislo <= 1:
        return False

    for delitel in range(2, cislo):
        if cislo % delitel == 0:
            return False

    return True

# Funkce, která vrátí seznam všech prvočísel od 2 do zadaného maximum
def vrat_prvocisla(maximum):
    results = []  
    for i in range(2, maximum + 1): 
        if je_prvocislo(i):         
            results.append(i)       
    return results                  

# Hlavní část programu, spustí se jen když soubor spustíme přímo
if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))
    print(f"{cislo} -> {je_prvocislo(cislo)}")
    print(f"{cislo} -> {vrat_prvocisla(cislo)}")