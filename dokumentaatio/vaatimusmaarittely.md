# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovellus on laskinohelmisto, jolla voidaan ainakin suorittaa matriisilaskennan peruslaskutoimituksia, kuten matriisituloja ja matriisien summia. Ohelmaan voisi lisätä myös muita laskinohjelmia, kuten ohjelman, jolla matriiseja voisi viedä redusoituun porrasmuotoon Gaussin-Jordanin eliminointimenetelmällä. Laskinohjelmat tukevat matriiseja, jotka koostuvat vain kokonais-, liuku- tai rationaaliluvuista. Laskin ei siis tue polynomeja.

## Käyttäjät
Sovelluksessa on ainakin tavallisia käyttäjiä sekä mahdollisesti myös pääkäyttäjiä.

## Toiminnallisuudet
### Perusversion toiminnallisuudet
#### Ennen kirjautumista
* Käyttäjä voi luoda käyttäjätunnukset, tietyillä rajoituksilla käyttäjänimen ja salasanan formaattiin
* Käyttäjä voi kirjautua sisään luomillaan tunnuksilla
* Käyttäjä voi mahdollisesti myös käyttää sovellusta kirjautumatta, jollin ainakaan laskuhistoria ei olisi käytössä

#### Kirjautumisen jälkeen
* Käyttäjä voi selata omaa laskuhistoriansa
* Käyttäjä voi valita mitä laskinohjelmistoa käyttää
* Käyttäjä voi laskea laskuja valitulla laskinohjelmistolla
* Käyttäjä voi kopioida vastauksen LaTeX -muodossa
* Käyttäjä voi kirjautua ulos.

### Jatkokehitysideoita
* Välivaiheiden tarkastelu
* Automaattinen LaTeX -koodin muodostaminen myös välivaiheista
* Sovellukseen voisi lisätä myös muita laskinohjelmia
    * tavallisen laskimen tai funktiolaskimen
    * laskinohjelman jolla matriiseja voisi viedä redusoituun porrasmuotoon.
    * laskinohjelman jolla voisi etsiä käänteismatriisin
    * tuki polynomeille matriisilaskuissa