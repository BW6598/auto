from unittest import TestCase
from libs import login
from pages import front_login
import time
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Test(TestCase):
    def test_login(self):
        # login.login()
        front_login.login()

        time.sleep(5)

    @classmethod
    def setUpClass(cls):
        login.login()
        time.sleep(1)

    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        login.create_driver.driver.quit()