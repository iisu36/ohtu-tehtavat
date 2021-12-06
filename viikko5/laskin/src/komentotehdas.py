class Laskutoimitus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        arvo = int(self._lue_syote())
        self.laske(arvo)

    def laske(self, arvo):
        return 0

class Summa(Laskutoimitus):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def laske(self, arvo):
        self._sovelluslogiikka.plus(arvo)

class Erotus(Laskutoimitus):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def laske(self, arvo):
        self._sovelluslogiikka.miinus(arvo)

class Nollaus(Laskutoimitus):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self._sovelluslogiikka.nollaa()
        

class Kumoa(Laskutoimitus):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        pass