# Úkol 2

def cislo_text(cislo):
    do_dvaceti = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset", 
             "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct", "dvacet"]
    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    
    if int(cislo) < 0:
        return "Číslo musí být v rozmezí 0-100"
    elif int(cislo) < 21:
        return f'"{cislo}" -> "{do_dvaceti[int(cislo)]}"'
    elif int(cislo) < 100:
        if cislo[1] == "0":
            return f'"{cislo}" -> "{desitky[int(cislo[0])]}"'
        else:
            return f'"{cislo}" -> "{desitky[int(cislo[0])]} {do_dvaceti[int(cislo[1])]}"'
    elif int(cislo) == 100:
        return f'"{cislo}" -> "sto"'
    else:
        return "Číslo musí být v rozmezí 0-100"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)