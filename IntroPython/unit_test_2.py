import unittest


def ConnectToDB():
    print("[connected to database]")


def DisconnectDB(db):
    print("[Disconnected from database {}]".format(db))


class User:
    username = ""
    active = False

    def __init__(self, db, username):
        self.username = username

    def SetActive(self):
        self.active = True


class TestUser(unittest.TestCase):

    def setUp(self):
        self.db = ConnectToDB()
        self.dicoding = User(self.db, "dicoding")

    def tearDown(self):
        DisconnectDB(self.db)

    # Test Case 1
    def test_user_default_not_active(self):
        self.assertFalse(self.dicoding.active)

    # Test Case 2
    def test_user_is_active(self):
        self.dicoding.SetActive()
        self.assertTrue(self.dicoding.active)

if __name__ == '__main__':
    # Test Runner
    unittest.main()
