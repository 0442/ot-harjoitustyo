import unittest

from services.user_service import UserService
from entities.user import User
from entities.history_entry import HistoryEntry


class DummyHistRepo:
    def __init__(self, database: list[HistoryEntry] = None) -> None:
        self._database = database or []

    def get_history(self, username: str) -> list[HistoryEntry]:
        hist = [e for e in self._database if e.username == username]
        return "\n\n".join([str(h) for h in hist])

    def append_history(self, entry: HistoryEntry):
        self._database.append(entry)

    def clear_database(self) -> None:
        self._database.clear()

    @property
    def database(self):
        return self._database


class DummyUserRepo:
    def __init__(self, database: list[User] = None) -> None:
        self._database = database or []

    def create_user(self, user: User) -> bool:
        self._database.append(user)
        if user in self._database:
            return True
        else:
            return False

    def find_user(self, username: str) -> User | None:
        for user in self._database:
            if user.username == username:
                return user

        return None

    def delete_user(self, user: User) -> None:
        for i, user in enumerate(self._database):
            if user == user:
                self._database.pop(i)
                break

    def clear_database(self) -> None:
        self._database.clear()

    @property
    def database(self):
        return self._database


class TestUserService(unittest.TestCase):
    def setUp(self) -> None:
        self._test_user = User("Hello", "World")

        self._user_repo = DummyUserRepo()
        self._hist_repo = DummyHistRepo()
        self._user_service = UserService(self._user_repo, self._hist_repo)

    def test_registration(self):
        success, status = self._user_service.register(self._test_user)

        self.assertTrue(self._test_user in self._user_repo.database)
        self.assertTrue(success)
        self.assertIsInstance(status, str)

    def test_login(self):
        user_repository = DummyUserRepo([self._test_user])
        user_service = UserService(user_repository, self._hist_repo)
        success, status = user_service.log_in(self._test_user)

        self.assertEqual(user_service.user, self._test_user)
        self.assertTrue(success)
        self.assertEqual(status, None)

    def test_login_wrong_credentials(self):
        user_repository = DummyUserRepo([self._test_user])
        user_service = UserService(user_repository, self._hist_repo)
        success, status = user_service.log_in(User("Wrong", "Credentials"))

        self.assertEqual(user_service.user, None)
        self.assertFalse(success)
        self.assertIsInstance(status, str)

    def test_log_out(self):
        user_repository = DummyUserRepo([self._test_user])
        user_service = UserService(user_repository, self._hist_repo)
        success, _ = user_service.log_in(self._test_user)
        self.assertTrue(success)

        self._user_service.log_out()

        self.assertEqual(self._user_service.user, None)

    def test_get_history(self):
        entry1 = HistoryEntry(self._test_user.username, "1+1", "2")
        entry2 = HistoryEntry("Someone else", "2+2", "4")
        entry3 = HistoryEntry("Not test_user", "3+3", "6")
        entry4 = HistoryEntry(self._test_user.username, "3+3", "6")

        hist_repo = DummyHistRepo([entry1, entry2, entry3, entry4])
        user_repo = DummyUserRepo([self._test_user])

        user_service = UserService(user_repo, hist_repo)
        success, _ = user_service.log_in(self._test_user)
        self.assertTrue(success)

        result = user_service.get_history()
        self.assertIsInstance(result, str)

    def test_append_history(self):
        user_repository = DummyUserRepo([self._test_user])
        user_service = UserService(user_repository, self._hist_repo)
        success, _ = user_service.log_in(self._test_user)
        self.assertTrue(success)

        calc = "[[1]] + [[1]]"
        answ = "[[2]]"
        user_service.append_history(calc, answ)

        as_entry = HistoryEntry(self._test_user.username, calc, answ)
        self.assertTrue(as_entry in self._hist_repo.database)
