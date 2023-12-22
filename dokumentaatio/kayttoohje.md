# Käyttöohje
## Konfiguraatio
Konfiguraatiot tehdään `.env`-tiedostoon.
Hyväksyttyjä ympäristömuuttujia ovat
* `DB_FILE_PATH` joka määrittää polun sqlite3 tietokantatiedostoon.
* LaTeX -koodin generointi:
  * `LATEX_MAT_BEGIN` matriisiblokin aloittava komento, esim. "\\[\\begin{bmatrix}" tai "\\[\\begin{matrix}"
  * `LATEX_MAT_END` matriisiblokin lopettava komento, esim. "\\end{bmatrix}\\]" tai "\\end{matrix}\\]"
  * `INDENT` LaTeX -koodissa käytettävä indentaatio
Huom: Jos `DB_FILE_PATH` -konfiguraatiota muokkaa, tulee joko aikaisempi tietokanta nimetä uudelleen vastaamaan uutta konfiguraatiota tai tietokanta alustaa käyttöohjeiden mukaisesti uudelleen.
## Asentaminen ja käynnistäminen
1. Asenna riippuvuudet:
```shell
    poetry install
```
2. Alusta tietokanta:
```shell
    poetry run invoke build
```
3. Aja sovellus:
```shell
    poetry run invoke start
```

## Laskeminen
Ohjelma aukeaa laskinnäkymään, jossa voi heti laskea matriisilaskuja. Laskinnäkymässä on kaksi eri välilehteä: Matrix calculator ja Row echelon calculator.

Matrix calculatorilla voidaan laskea matriisien yhteen- (+), vähennys- (-) ja kertolaskuja (*).

Row echelon calculatorilla voidaan viedä matriiseja supistettuun porrasmuotoon. 
Porrasmuotolaskin antaa vastauksen lisäksi laskun välivaiheet ja vastauksen LaTeX -muodossa.   

Molemmissa laskimissa tekstikenttään tulee matriisit syöttää kaksiulotteisena listana tai vain listata rivit peräkkäin.
Sulkeina tulee käyttää "[]" -merkkejä.

![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/03a67e5e-f1ef-4aa2-96cd-d4958ec81e4a)
![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/ac102398-ca84-4d91-a451-501c23cc7985)


## Rekisteröityminen
Rekisteröityminen onnistuu kirjatumisnäkymästä. kirjautumisnäkymän saa auki painamalla "Login"-painiketta.
Kirjautumisnäkymässä rekisteröityminen tapahtuu syöttämällä tunnukset tekstikenttiin ja painamalla "Register".
Mikäli rekisteröitymienn ei onnistu, ilmoittaa sovellus virheestä. Onnistuessa ohjelma ilmoittaa käyttäjätunnuksen luomisen onnistuneen,
minkä jälkeen voit kirjatua sisään.

![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/d8f85c7a-fa32-47fe-941c-aca4f3a716e4)



## Kirjautuminen
Kirjautumalla sisään saa käyttöön laskuhistorian.
Myös kirjautuminen tapahtuu kirjautumisnäkymästä, jonka saa auki painamalla "Login"-painiketta.
Kirjautumisnäkymässä kirjautuminen tapahtuu syöttämällä tunnukset tekstikenttiin ja painamalla "Login".
Mikäli kirjautuminen ei onnistu, ilmoittaa sovellus virheestä. Onnistuessa ohjelma siirtyy takaisin laskinsivulle.

![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/09b4e060-ce48-41f1-9b1b-4ac35ae78172)


## Historian tarkastelu
Historiasivulle pääsee painamalla "History"-painiketta.
Mikäli et ole vielä kirjautunut sisää, sivulla ilmoitetaan, että tominto vaatii ensin kirjautumisen.

![image](https://github.com/0442/ot-harjoitustyo/assets/69271621/6e1d0675-c7af-4921-907d-f1265f72424a)

