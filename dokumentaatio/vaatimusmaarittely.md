# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovellus on matriisilaskinohelmisto, jossa on kaksi eri laskinta. Ensimmäisellä laskimista voidaan suorittaa matriisien yhteen- vähennys- ja kertolaskuja.  
Toisella laskinohjelmalla voidaan matriiseja viedä redusoituun porrasmuotoon Gaussin-Jordanin eliminointimenetelmällä. 
Laskinohjelmat tukevat matriiseja, jotka koostuvat vain kokonais- tai rationaaliluvuista. Laskin ei siis tue mm. polynomeja.

## Käyttäjät
Sovelluksessa on tavallisia käyttäjiä. 
Sovellusta voi kuitenkin käyttää myös ilman kirjautumista.
Kirjautumalla käyttäjä saa käyttöönsä laskuhistorian.

## Toiminnallisuudet
### Ennen kirjautumista
* Käyttäjä voi luoda käyttäjätunnukset. Tunnuksen ja salasanan pituus oltava >= 3 merkkiä (tehty)
* Käyttäjä voi kirjautua sisään luomillaan tunnuksilla (tehty)
* Käyttäjä voi käyttää sovellusta kirjautumatta, jollin laskuhistoria ei ole käytössä (tehty)

#### Kirjautumisen jälkeen
* Käyttäjä voi selata omaa laskuhistoriansa (tehty)
* Käyttäjä voi valita mitä laskinohjelmistoa käyttää (tehty)
* Käyttäjä voi laskea laskuja valitulla laskinohjelmistolla (molemmat laskinohjelmistot tehty)
* Käyttäjä voi kopioida vastauksen LaTeX -muodossa (tehty (porrasmuotolaskin))
* Käyttäjä voi kirjautua ulos. (tehty)

### Jatkokehitysideoita
* Sovellukseen voisi lisätä myös muita laskinohjelmia
    * tavallisen laskimen tai funktiolaskimen
    * laskinohjelman jolla voisi etsiä käänteismatriisin
    * tuki polynomeille matriisilaskuissa
