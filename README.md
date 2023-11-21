# Matriisilaskinohelmisto
## Valmiin sovelluksen kuvaus:
Sovelluksella voidaan suorittaa joitakin operaatiota matriiseille, kuten matriisikertolaskuja sekä saattaa matriiseja supistettuun porrasmuotoon Gaussin-Jordanin eliminointimenetelmällä.
Ratkaisuista sovellus luo LaTeX -version, jonka käyttäjä voi kopioida.


## Dokumentaatio
* [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
* [Työaikakirjanpito](dokumentaatio/tuntikirjanpito.md)
* [Changelog](dokumentaatio/changelog.md)

## Asentaminen
1. Asenna riippuvuudet:
```shell
    poetry install
```
2. Aja sovellus:
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
### Testikattavuusraportin luominen:
```shell
    poetry run invoke coverage-report
```
