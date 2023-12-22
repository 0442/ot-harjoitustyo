# Testaus

## Yksikkötestaus
### Korkean tason sovelluslogiikka
Sovelluslogiikan abstrahoinnista vastaa kaksi luokkaa: `CalculatorService` ja `UserService`.
`CalculatorService` -luokkaa testataan `TestCalculatorService` -testiluokalla, ja `UserService` -luokkaa vastaavasti `TestUserSerivce` -testiluokalla.

### Merkittävimmät apufunktiot ja -luokat
Rationaalilukua esittävää luokaa `RatNum` testataan kahdella testiluokalla, `TestRatNum` ja `TestRatNumWithInts`. `TestRatNum` testaa laskutoimituksia rationaalilukujen kesken, kun taas `TestRatNumWithInts` testaa laskutoimituksia rationaalilukujen ja kokonaislukujen kesken.

Matriiseja supistettuun porrasmuotoon vievää funktiota `reduced_row_echelon` testataan luokalla `TestEchelon`.

Testit ajetaan komennolla `poetry run invoke test`. Komento asettaa ympäristömuttujalle `TEST` arvon, jolloin testitietokanta on käytössä.
### Testikattavuusraportti
![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/24264e5f-3682-4b2d-a8da-81ba19946291)

## Järjeselmätestaus
Järjestelmätestaus suoritetaan manuaaalisesti.

