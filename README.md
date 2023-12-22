# Matriisilaskinohelmisto
Sovelluksella voidaan suorittaa yhteen- vähennys- ja kertolaskuja matriiseien välillä. 
Lisäksi laskimella voidaan saattaa matriiseja supistettuun porrasmuotoon Gaussin-Jordanin eliminointimenetelmällä.
Porrasmuotolaskujen ratkaisuista sovellus luo LaTeX -version, jonka käyttäjä voi kopioida.

## Dokumentaatio
* [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
* [Changelog](dokumentaatio/changelog.md)
* [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
* [Käyttöohje](dokumentaatio/kayttoohje.md)
* [Testaus](dokumentaatio/testaus.md)
* [Releaset](https://github.com/0442/ot-harjoitustyo/releases)


## Asentaminen
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

## Invoke -komennot
### Ohjelman ajaminen:
```shell
    poetry run invoke start
```
### Testien ajaminen:
```shell
    poetry run invoke test
```
### Tietokannan alustaminen:
```shell
    poetry run invoke build
```
### Testikattavuusraportin luominen:
```shell
    poetry run invoke coverage-report
```
### Pylint:
```shell
    poetry run invoke lint
```

