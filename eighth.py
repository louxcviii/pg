def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    # Pokud dostanu integer, převedu ho na string
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)

    # Zkontrolujeme, že řetězec obsahuje jen 0 a 1
    if not all(bit in "01" for bit in binarni_cislo):
        raise ValueError("Vstup musí být binární číslo (obsahovat pouze 0 a 1).")

    # Výpočet binární hodnoty
    vysledek = 0
    for bit in binarni_cislo:
        vysledek = vysledek * 2 + int(bit)

    return vysledek

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

if __name__ == "__main__":
    print(bin_to_dec("0"))
    print(bin_to_dec(1))
    print(bin_to_dec("100"))
    print(bin_to_dec(101))
    print(bin_to_dec("010101"))
    print(bin_to_dec(10000000))