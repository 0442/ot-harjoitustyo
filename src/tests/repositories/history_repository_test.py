import unittest

from repositories.history_repository import history_repository
from entities.history_entry import HistoryEntry


class TestHistoryRepository(unittest.TestCase):
    def setUp(self):
        self._username = "User123"

        history_repository.clear_database()
        calc1 = "[[1,2]] + [[3,4]]"
        answer1 = "[[4,6]]"
        self._entry1 = HistoryEntry(self._username, calc1, answer1)

        calc2 = "[[3,2]] + [[2,3]]"
        answer2 = "[[5,5]]"
        self._entry2 = HistoryEntry(self._username, calc2, answer2)

    def test_get_history(self):
        history_repository.append_history(self._entry1)

        result = history_repository.get_history(self._username)
        self.assertEqual(result, [self._entry1])

    def test_append_history(self):
        history_repository.append_history(self._entry1)

        result = history_repository.get_history(self._username)
        self.assertEqual(result, [self._entry1])

        history_repository.append_history(self._entry2)

        result = history_repository.get_history(self._username)
        self.assertEqual(result, [self._entry1, self._entry2])
