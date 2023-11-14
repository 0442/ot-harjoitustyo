import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alussa_oikea_rahamäärä(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_alussa_oikea_myytyjen_lounaiden_määrä(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_edullisten_käteisosto_kasvattaa_kassan_rahamäärää(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)

    def test_maukkaiden_käteisosto_kasvattaa_kassan_rahamäärää(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004.0)

    def test_edullisten_käteisosto_palauttaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(480), 240)

    def test_maukkaiden_käteisosto_palauttaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(480), 80)

    def test_edullisten_käteisosto_liian_pienellä_rahamäärällä_palauttaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10), 10)

    def test_maukkaiden_käteisosto_liian_pienellä_rahamäärällä_palauttaa_vaihtorahat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(10), 10)

    def test_edullisten_käteisosto_liian_pienellä_rahamäärällä_ei_kasvata_rahamäärää(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaiden_käteisosto_liian_pienellä_rahamäärällä_ei_kasvata_rahamäärää(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_edullisten_käteisosto_liian_pienellä_rahamäärällä_ei_kasvata_myytyjen_määrää(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_käteisosto_liian_pienellä_rahamäärällä_ei_kasvata_myytyjen_määrää(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisten_käteisosto_kasvattaa_myytyjen_määrää(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_käteisosto_kasvattaa_myytyjen_määrää(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)




    def test_edullisten_korttiosto_riittävällä_rahamäärällä_oikea_palautusarvo(self):
        maksukortti = Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)

    def test_maukkaiden_korttiosto_riittävällä_rahamäärällä_oikea_palautusarvo(self):
        maksukortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)

    def test_edullisten_korttiosto_riittävällä_rahamäärällä_vähentää_kortin_saldoa(self):
        maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo_euroina(), 0.0)

    def test_maukkaiden_korttiosto_riittävällä_rahamäärällä_vähentää_kortin_saldoa(self):
        maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo_euroina(), 0.0)

    def test_edullisten_korttiosto_riittävällä_rahamäärällä_kasvattaa_myytyjen_määrää(self):
        maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_korttiosto_riittävällä_rahamäärällä_kasvattaa_myytyjen_määrää(self):
        maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisten_korttiosto_riittävällä_rahamäärällä_ei_kasvata_kassan_rahamäärää(self):
        maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaiden_korttiosto_riittävällä_rahamäärällä_ei_kasvata_kassan_rahamäärää(self):
        maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)



    def test_edullisten_korttiosto_liian_pienellä_rahamäärällä_oikea_palautusarvo(self):
        maksukortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)

    def test_maukkaiden_korttiosto_liian_pienellä_rahamäärällä_oikea_palautusarvo(self):
        maksukortti = Maksukortti(10)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)

    def test_edullisten_korttiosto_liian_pienellä_rahamäärällä_ei_vähennä_kortin_saldoa(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo_euroina(), 0.1)

    def test_maukkaiden_korttiosto_liian_pienellä_rahamäärällä_ei_vähennä_kortin_saldoa(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo_euroina(), 0.1)

    def test_edullisten_korttiosto_liian_pienellä_rahamäärällä_ei_kasvata_myytyjen_määrää(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_korttiosto_liian_pienellä_rahamäärällä_ei_kasvata_myytyjen_määrää(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisten_korttiosto_liian_pienellä_rahamäärällä_ei_kasvata_kassan_rahamäärää(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_maukkaiden_korttiosto_liian_pienellä_rahamäärällä_ei_kasvata_kassan_rahamäärää(self):
        maksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)



    def test_rahan_lataaminen_kasvattaa_kortin_saldoa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(maksukortti.saldo_euroina(), 1.0)

    def test_rahan_lataaminen_kasvattaa_kassan_rahamäärää(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1001.0)

    def test_negatiivisen_rahamäärän_lataaminen_ei_kasvata_kortin_saldoa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(maksukortti.saldo_euroina(), 0.0)

    def test_negatiivisen_rahamäärän_lataaminen_ei_kasvata_kassan_rahamäärää(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)