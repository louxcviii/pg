# definice trid

class Osoba():
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"Jmeno {self.jmeno}, vek {self.vek}"
    
class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f"Student {self.jmeno} studuje {self.rocnik} rocnik"

class Ucitel(Osoba):
    def __init__(self, jmeno, vek, obor):
        super().__init__(jmeno, vek)
        self.obor = obor

    def __str__(self):
        return f"Ucitel {self.jmeno} uci obor {self.obor}"

if __name__ == "__main__":
    print(Student("Adam", 20, 2))
    print(Student("Eva", 19, 1))
    print(Ucitel("Tomas", 40, "IT"))
    print(Osoba("Jan", 50))