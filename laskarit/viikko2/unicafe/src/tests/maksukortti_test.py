import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_rahan_ottaminen_vähentää_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)

    def test_rahaa_ei_voi_ottaa_yli_saldon(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_oikea_paluuarvo_ottaessa_kun_riittävästi_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_oikea_paluuarvo_ottaessa_kun_liian_vähän_rahaa(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test_oikea_maksukortin_tekstiesitys(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

