# Matriisilaskinohelmisto
## Valmiin sovelluksen kuvaus:
Sovelluksella voidaan suorittaa joitakin operaatiota matriiseille, kuten matriisikertolaskuja sekä saattaa matriiseja supistettuun porrasmuotoon Gaussin-Jordanin eliminointimenetelmällä.
Ratkaisuista sovellus luo LaTeX -version, jonka käyttäjä voi kopioida.


## Dokumentaatio
* [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
* [Changelog](dokumentaatio/changelog.md)
* [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
* [Releaset](https://github.com/0442/ot-harjoitustyo/releases)
* [Käyttöohje](dokumentaatio/kayttoohje.md)

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

