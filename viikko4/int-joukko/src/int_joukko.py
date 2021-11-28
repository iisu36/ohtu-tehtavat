class IntJoukko:
    def __init__(self, kapasiteetti=5, kasvatuskoko=5):
        if self.validoi_int(kapasiteetti):
            self.kapasiteetti = kapasiteetti

        if self.validoi_int(kasvatuskoko):
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def validoi_int(self, validoitava):
        if not isinstance(validoitava, int) or validoitava < 0:
            raise Exception("Pitää olla nollaa suurempi luku")
        return True

    def kuuluu(self, luku):

        for i in range(0, self.alkioiden_lkm):
            if luku == self.lukujono[i]:
                return True
        
        return False


    def lisaa(self, lisattava):

        if not self.kuuluu(lisattava) or self.alkioiden_lkm == 0:
            self.lukujono[self.alkioiden_lkm] = lisattava
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                vanha_taulukko = self.lukujono
                self.kopioi_taulukko(self.lukujono, vanha_taulukko)
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(vanha_taulukko, self.lukujono)


    def poista(self, poistettava):
        poistettavan_indeksi = -1

        for i in range(0, self.alkioiden_lkm):
            if poistettava == self.lukujono[i]:
                poistettavan_indeksi = i
                self.lukujono[poistettavan_indeksi] = 0
                break

        if poistettavan_indeksi != -1:
            for j in range(poistettavan_indeksi, self.alkioiden_lkm - 1):
                self.lukujono[j], self.lukujono[j + 1] = self.lukujono[j + 1], self.lukujono[j]

            self.alkioiden_lkm = self.alkioiden_lkm - 1

    def kopioi_taulukko(self, kopioitava, kopio):
        for i in range(0, len(kopioitava)):
            kopio[i] = kopioitava[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
