# Úkol 2

def cislo_text(cislo):

    # Ošetření vstupu - pokud je to string, pokusíme se ho převést na int
    if isinstance(cislo, str):
        cislo = cislo.strip()
        if cislo.isdigit():
            cislo = int(cislo)
        else:
            return "Zadaný vstup není celé číslo."

    # Musí to být integer
    if not isinstance(cislo, int):
        return "Vstup musí být číslo (int nebo číselný text)."

    do_dvaceti = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", 
                  "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", 
                  "osmnáct", "devatenáct", "dvacet"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    # kontrola rozsahu
    if cislo < 0 or cislo > 100:
        return "Číslo musí být v rozmezí 0–100."

    # 0–20
    if cislo <= 20:
        return do_dvaceti[cislo]

    # 100
    if cislo == 100:
        return "sto"

    # 21–99
    d = cislo // 10
    j = cislo % 10

    if j == 0:
        return desitky[d]
    else:
        return f"{desitky[d]} {do_dvaceti[j]}"


if __name__ == "__main__":
    cislo = int(input("Zadej číslo: "))
    text = cislo_text(cislo)
    print(text)
    # print(cislo_text("45"))
    # print(cislo_text(5))