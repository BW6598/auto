from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC # 로딩될 때까지 대기
import time

# driver 옵션 추가(시스템에 부착된 장치가 작동하지 않습니다. 삭제 옵션)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

options.add_argument("--start-maximized")  # 전체화면 옵션

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
