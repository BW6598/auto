from unittest import TestCase
from libs import login
from pages import Kurly_Add_ContentProduct
import time
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Test(TestCase):
    def test_login(self):
        # login.login()
        Kurly_Add_ContentProduct.login()

        time.sleep(1)

        Kurly_Add_ContentProduct.create_masterproduct()

        time.sleep(3)