def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).   
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Implementace pravidel pohybu pro různé figury zde.
    
    typ = figurka["typ"]
    radek_akt, sloupec_akt = figurka["pozice"]
    radek_cil, sloupec_cil = cilova_pozice 
    delta_radek = radek_cil - radek_akt
    delta_sloupec = sloupec_cil - sloupec_akt

    # Kontrola, zda je cílová pozice na šachovnici
    if not (1 <= radek_cil <= 8 and 1 <= sloupec_cil <= 8):
        return False

    # Kontrola, zda cílová pozice není obsazena vlastní figurou
    if cilova_pozice in obsazene_pozice:
        return False

    # Pěšec
    if typ == "pěšec":
        if delta_sloupec == 0 and (delta_radek == 1 or (radek_akt == 2 and delta_radek == 2)):
            return True
        return False

    # Jezdec
    elif typ == "jezdec":
        if (abs(delta_radek), abs(delta_sloupec)) in [(2,1), (1,2)]:
            return True
        return False

    # Věž
    elif typ == "věž":
        if delta_radek == 0:  # horizontálně
            krok = 1 if delta_sloupec > 0 else -1
            for c in range(sloupec_akt + krok, sloupec_cil, krok):
                if (radek_akt, c) in obsazene_pozice:
                    return False
            return True
        elif delta_sloupec == 0:  # vertikálně
            krok = 1 if delta_radek > 0 else -1
            for r in range(radek_akt + krok, radek_cil, krok):
                if (r, sloupec_akt) in obsazene_pozice:
                    return False
            return True
        return False

    # Střelec
    elif typ == "střelec":
        if abs(delta_radek) == abs(delta_sloupec):
            krok_radek = 1 if delta_radek > 0 else -1
            krok_sloupec = 1 if delta_sloupec > 0 else -1
            r, c = radek_akt + krok_radek, sloupec_akt + krok_sloupec
            while (r, c) != (radek_cil, sloupec_cil):
                if (r, c) in obsazene_pozice:
                    return False
                r += krok_radek
                c += krok_sloupec
            return True
        return False

    # Dáma
    elif typ == "dáma":
        # horizontální
        if delta_radek == 0:
            krok = 1 if delta_sloupec > 0 else -1
            for c in range(sloupec_akt + krok, sloupec_cil, krok):
                if (radek_akt, c) in obsazene_pozice:
                    return False
            return True
        # vertikální
        elif delta_sloupec == 0:
            krok = 1 if delta_radek > 0 else -1
            for r in range(radek_akt + krok, radek_cil, krok):
                if (r, sloupec_akt) in obsazene_pozice:
                    return False
            return True
        # diagonální
        elif abs(delta_radek) == abs(delta_sloupec):
            krok_radek = 1 if delta_radek > 0 else -1
            krok_sloupec = 1 if delta_sloupec > 0 else -1
            r, c = radek_akt + krok_radek, sloupec_akt + krok_sloupec
            while (r, c) != (radek_cil, sloupec_cil):
                if (r, c) in obsazene_pozice:
                    return False
                r += krok_radek
                c += krok_sloupec
            return True
        return False

    # Král
    elif typ == "král":
        if abs(delta_radek) <= 1 and abs(delta_sloupec) <= 1:
            return True
        return False

    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True