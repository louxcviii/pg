# Úkol 1

# Definice funkce sudé nebo liché číslo.
def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0: # Podmínka která nám určuje, zda po dělení zbyde nula.
        print(f"Číslo {cislo} je sudé.") # Vrátí, že číslo je sudé.
    else: # Pokud if podmínka není pravdivá, zbyde zbytek.
        print(f"Číslo {cislo} je liché.") # Vrátí, že číslo je liché.

# Spuštění funkce.
if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)