```mermaid
classDiagram
    UI --> CalculatorService
    MatrixCalculator ..> LatexGenerator

    User --> HistoryRepository
    CalculatorService ..> MatrixCalculator
    CalculatorService --> User

    HistoryRepository ..> Solution
    MatrixCalculator ..> Solution
```