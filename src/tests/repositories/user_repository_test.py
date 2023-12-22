import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.clear_database()

        self._test_user = User("hello", "world")

    def test_create_user(self):
        user_repository.create_user(self._test_user)
        result = user_repository.find_user(self._test_user.username)

        self.assertEqual(result, self._test_user)

    def test_find_user(self):
        user_repository.create_user(self._test_user)
        result1 = user_repository.find_user(self._test_user.username)
        result2 = user_repository.find_user("This user does not exist")

        self.assertEqual(result1, self._test_user)
        self.assertEqual(result2, None)

    def test_delete_user(self):
        user_repository.create_user(self._test_user)
        user_repository.delete_user(self._test_user)

        result = user_repository.find_user(self._test_user.username)
        self.assertEqual(result, None)
