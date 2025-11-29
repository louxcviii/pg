def dec_to_bin(cislo):
    # funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int!!!)
    # 7 -> "111"
    # 5 -> "101"
    # Pokud dostanu string, zkusím převést na integer
    if isinstance(cislo, str):
        if cislo.isdigit():
            cislo = int(cislo)
        else:
            raise ValueError("Vstup musí být číslo (int nebo číselný řetězec).")

    # musí to být int
    if not isinstance(cislo, int):
        raise ValueError("Vstup musí být číslo.")

    # 0
    if cislo == 0:
        return "0"

    vysledek = ""

    # opakovaně dělíme 2 a bereme zbytky (0 nebo 1)
    while cislo > 0:
        bit = cislo % 2
        vysledek = str(bit) + vysledek
        cislo = cislo // 2

    return vysledek

def test_dec_to_bin(): # bylo test_bin_to_dec()
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"

if __name__ == "__main__":
    print(dec_to_bin("0"))
    print(dec_to_bin(1))
    print(dec_to_bin("100"))
    print(dec_to_bin(101))
    print(dec_to_bin(127))
    print(dec_to_bin("128"))