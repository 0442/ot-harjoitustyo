# Testaus

## Yksikkötestaus
### Korkeamman tason sovelluslogiikka
Sovelluslogiikan abstrahoinnista vastaa kaksi luokkaa: `CalculatorService` ja `UserService`.
`CalculatorService` -luokkaa testataan `TestCalculatorService` -testiluokalla, ja `UserService` -luokkaa vastaavasti `TestUserSerivce` -testiluokalla.

### Repositoriot
Sovelluksessa käytetään sqlite3 -tietokantaa, jonka kanssa komminikointi on piilotettu `UserRepository` ja `HistoryRepository` -luokkien taakse.
Repositorioita testataan testiluokilla `TestUserRepository` ja `HistoryRepostiory`. 

### Merkittävimmät apufunktiot ja -luokat
Rationaalilukua esittävää luokaa `RatNum` testataan kahdella testiluokalla, `TestRatNum` ja `TestRatNumWithInts`. `TestRatNum` testaa laskutoimituksia rationaalilukujen kesken, kun taas `TestRatNumWithInts` testaa laskutoimituksia rationaalilukujen ja kokonaislukujen kesken.

Matriiseja supistettuun porrasmuotoon vievää funktiota `reduced_row_echelon` testataan luokalla `TestEchelon`.

Testit ajetaan komennolla `poetry run invoke test`. Komento asettaa ympäristömuttujalle `TEST` arvon, jolloin testitietokanta on käytössä.
### Testikattavuusraportti
![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/24264e5f-3682-4b2d-a8da-81ba19946291)

Entities -kansion tiedostot eivät juurikaan sisällä logiikkaa. calculator_utils -kansion types.py sisältää vain tyyppejä, joten testattavaa ei ole myöskään siellä.
latex_generator.py:ssä olevilla LaTeX -koodia generoiville funktioille ei ole automaattisia testejä. Myöskään matrix_utils.py -tiedoston yksittäisiä matriisioperaatioita
vastaavia funktioita ei ole automaattisesti testattu. str_to_matrix ja str_to_num funkioille ei myöskään ole automaattisia testejä.

## Järjeselmätestaus
Järjestelmätestaus suoritetaan manuaaalisesti.

Sovellusta on testattu dokumentaatiosta löytyvän käyttöohjeen mukaisesti eri konfiguraatioilla.
Järjestelmätestauksessa on käyty läpi kaikki märittelydokumentin kuvaamat ominaisuudet.


