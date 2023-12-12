# Rakenne
Ohelma on toteutettu hyödyntäen kerrosarkkitehtuuria. Ohjelmassa on käyttöliittymästä, sovelluslogiikasta ja tietokantojen kanssa kommunikoinnista vastaavat kerrokset. Laskimen logiikkakerros hyödyntää useita laskufunktioita. Ohjelman kerrosarkkitehtuuria esittävä luokkakaavio (calculatorUtilities ja database eivät esitä luokkia):
```mermaid
classDiagram
    class UI

    class UserRepository
    class HistoryRepository
    class RatNum

    class database {
        The sqlite3 database UserRepository
        and History Repository uses.
    }
    class CalculatorService
    class UserService
    class calculatorUtilities {
        This represents various utility functions like
        reduced_row_echelon used by CalculatoService
    }

    UI --> CalculatorService
    UI --> UserService
    UserService --> UserRepository
    UserService --> HistoryRepository

    UserRepository --> database
    HistoryRepository --> database
    CalculatorService --> calculatorUtilities
    calculatorUtilities --> RatNum
```
## Käyttöliittymä
Käyttöliittymästä vastaa `UI`-luokka. Käyttöliittymätaso eli `UI` kommunikoi sovelluslogiikkatason kanssa käyttämällä `CalculatorService`- ja `UserService`-luokkia.
Käyttöliittymässä on kolme eri näkymää, `CalculatorView`, `LoginView` ja `HistoryView`. Laskinnäkymässä laskinkomponentilla on lisäksi kaksi eri välilehteä. . Näkymiä ja välilehtiä vastaavat luokat perivät `BaseView`-luokan.
Näkymien vaihtamista kontrolloi `UI`-luokka.
```mermaid
    classDiagram
    class BaseView

    class UI

    class CalculatorView
    class LoginView
    class HistoryView
    class MatrixCalculator
    class EchelonCalculator

    UI --* BaseView
    BaseView <|-- CalculatorView
    BaseView <|-- LoginView
    BaseView <|-- HistoryView
    BaseView <|-- MatrixCalculator
    BaseView <|-- EchelonCalculator
    CalculatorView --> MatrixCalculator
    CalculatorView --> EchelonCalculator
```

## Sovelluslogiikka
Rajapinnoista sovelluslogiikkaan vastaavat luokat `CalculatorService` ja `UserService`.

`CalculatorService`
käyttää useita laskennassa apufunktioita jotka taas käyttävät muita apufunktioita ja luokkia. Nämä sijaitsevat
calculator_utils -kansiossa.

`UserService`
Vastaa käyttäjän kirjautumiseen ja historiaan liittyvästä rajapinnasta. `UserService` kommunikoi repositorytason luokkien
`UserRepository`:n ja `HistoryRepository`:n kanssa.

## Tietokanta
Tietokannan kanssa kommunikoinnista vastaavat `UserRepository` ja `HistoryRepository`. Luokat käyttävät SQLite3 tietokantaa.
Luokat noudattavat Repository-mallia.

# Tominnallisuuksia

## Käyttäjä suorittaa laskutoimituksen
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant CalculatorService
    participant HistoryRepository
    User ->> UI: input "[[1,2,3], [4,5,6]]" to "matrix" text field
    User ->> UI: click "Row reduce" button
    UI ->> CalculatorService: find_reduced_row_echelon("[[1,2,3], [4,5,6]]", user)
    CalculatorService ->> HistoryRepository: add_entry("[[1,2,3], [4,5,6]]", user)
    CalculatorService ->> UI: answer
```
