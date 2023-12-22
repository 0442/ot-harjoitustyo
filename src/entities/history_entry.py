from typing import NamedTuple


class HistoryEntry(NamedTuple):
    """Represents a calculation history entry.

    Attributes:
        username (str): Username of the user whom the entry belongs to.
        calculation (str): A string representation of a calculation.
        answer (str): A string representation of the answer to the calculation.
    """
    username: str
    calculation: str
    answer: str

    def __str__(self):
        return f"{self.calculation}\n = {self.answer}"
