import time
from unittest import TestCase
from libs import login
from pages import Kurly_Create_ReviewAvailable
import sys, os  # 폴더 다를 때 사용
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

class Test(TestCase):
    def test_001(self):
        login.login()
        time.sleep(2)

    def test_002(self):
        Kurly_Create_ReviewAvailable.purchase()



