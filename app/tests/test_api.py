import unittest
from app import create_app
from flask import current_app



class APITestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        self.app_context.pop()

    def test_app_is_exist(self):
        """测试 Flask 实例是否存在"""
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()