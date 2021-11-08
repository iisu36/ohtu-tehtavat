import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_pelaajahaku_palauttaa_olemassaolevan_pelaajan(self):
        self.assertEqual(self.statistics.search("Semenko").name, "Semenko")

    def test_pelaajahaku_palauttaa_none_kuulumattomalle_pelaajalle(self):
        self.assertEqual(self.statistics.search("Koivu"), None)
    
    def test_joukkuehaku_palauttaa_oikein(self):
        joukkuelista = self.statistics.team("EDM")
        self.assertEqual(len(joukkuelista), 3)
        self.assertEqual(joukkuelista[0].name, "Semenko")
        self.assertEqual(joukkuelista[1].name, "Kurri")
        self.assertEqual(joukkuelista[2].name, "Gretzky")

    def test_joukkuehaku_palauttaa_tyhjan_listan_vaaralla_joukkueella(self):
        joukkuelista = self.statistics.team("MON")
        self.assertEqual(len(joukkuelista), 0)

    def test_top_jarjestaminen_toimii_oikein_kaikilla(self):
        pelaajalista = self.statistics.top_scorers(4)
        self.assertEqual(pelaajalista[0].name, "Gretzky")
        self.assertEqual(pelaajalista[1].name, "Lemieux")
        self.assertEqual(pelaajalista[2].name, "Yzerman")
        self.assertEqual(pelaajalista[3].name, "Kurri")
        self.assertEqual(pelaajalista[4].name, "Semenko")

    def test_top_jarjestaminen_toimii_oikein_nollalla(self):
        pelaajalista = self.statistics.top_scorers(0)
        self.assertEqual(pelaajalista[0].name, "Gretzky")

    def test_top_jarjestaminen_toimii_oikein_miinuksella(self):
        pelaajalista = self.statistics.top_scorers(-1)
        self.assertEqual(len(pelaajalista),0)

    def test_top_jarjestaminen_laskee_oikein_kaikilla(self):
        pelaajalista = self.statistics.top_scorers(4)
        self.assertEqual(pelaajalista[0].points, 35+89)
        self.assertEqual(pelaajalista[1].points, 45+54)
        self.assertEqual(pelaajalista[2].points, 42+56)
        self.assertEqual(pelaajalista[3].points, 37+53)
        self.assertEqual(pelaajalista[4].points, 4+12)