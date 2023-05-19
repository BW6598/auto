import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from libs import create_driver
from selenium.webdriver.support.select import Select
import random


# La-CMS 로그인
def login():

    url = 'https://lacms2.stg.kurlycorp.kr/signin'
    create_driver.driver.get(url)
    try:
        # id inputbox 있는지 확인
        WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.ID,'username')))

        # 아이디/비밀번호 입력
        create_driver.driver.find_element(by=By.NAME,
                                          value='username').send_keys('byungwook.lee@kurlycorp.com')
        create_driver.driver.find_element(by=By.NAME,
                                          value='password').send_keys('testtest00')

        # 로그인 버튼 클릭
        create_driver.driver.find_element(by=By.XPATH,
                                          value='//*[@id="root"]/div/form/button').click()

        # alert 존재하면 내용 출력, 없으면 pass 출력
        WebDriverWait(create_driver.driver, 3).until(EC.alert_is_present())
        alert = create_driver.driver.switch_to.alert
        print("login : Fail")
        print(alert.text)
        alert.accept()
    except:
        print("login : Pass")

# 상품 > 마스터 상품 진입 후 마스터 상품 생성
def create_masterproduct():

    # 랜덤 숫자 생성
    randomNum = str(random.randrange(1, 100))
    randomPrice = random.randrange(1,20) * 1000

    # 상품 리스트가 있는지 확인
    WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "nav"] / div[2]')))

    # 상품 클릭
    create_driver.driver.find_element(By.XPATH, '// *[ @ id = "nav"] / div[2]').click()
    time.sleep(1)

    # 마스터 상품 클릭
    create_driver.driver.find_element(By.LINK_TEXT, '마스터 상품').click()
    time.sleep(1)

    # ... 버튼 클릭(마스터 상품 생성 버튼 클릭 전)
    create_driver.driver.find_element(By.XPATH, '// *[ @ id = "root"] / div / div / div '
                                                '/ div[1] / div / div[1] / button').click()
    time.sleep(1)

    # [마스터 상품 등록] 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/button[1]').click()
    time.sleep(1)

    # 마스터 상품 등록 진입된 이후
    # 분류 카테고리 있는지 확인
    WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                  '//*[@id="sectionContainer"]/header'
                                                                                  '/div/div[2]/div/div/div/div/div/'
                                                                                  'div[1]/div[1]/div/div/button[2]')))

    # 분류 카테고리 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="sectionContainer"]/header'
                                                  '/div/div[2]/div/div/div/div/div/'
                                                  'div[1]/div[1]/div/div/button[2]').click()
    time.sleep(1)

    # 분류 카테고리 선택(가구/인테리어 > 가구/시공 > 가구)
    create_driver.driver.find_element(By.XPATH, '// *[ @ id = "a11y-tabpanel-1"] / div / div '
                                                '/ div[1] / div[1] / div / ul / div[1]').click()
    time.sleep(0.5)

    create_driver.driver.find_element(By.XPATH, '//*[@id="a11y-tabpanel-1"]/div/div/'
                                                'div[1]/div[2]/div/ul/div[1]').click()
    time.sleep(0.5)

    create_driver.driver.find_element(By.XPATH, '//*[@id="a11y-tabpanel-1"]/div/div/'
                                                'div[1]/div[3]/div/ul/div[1]').click()
    time.sleep(0.5)

    # 마스터 상품명 입력
    create_driver.driver.find_element(By.NAME, 'masterProductName').send_keys("마스터 상품 자동화" + randomNum)
    time.sleep(1)

    # [저장] 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="main__content"]/div[2]/header/div/div/div/button[2]').click()
    time.sleep(1)

    # 판매가 입력
    create_driver.driver.find_element(By.NAME, 'basePrice').send_keys(randomPrice)
    time.sleep(1)

    # 상품 정보 제공 고시 입력
    create_driver.driver.find_element(By.XPATH, '//*[@id="a11y-tabpanel-0"]/div/div/div[3]/div[2]/'
                                                'div/div/div/div/div/div/div/div/div/div/div/button[2]').click()
    time.sleep(1)

    create_driver.driver.find_element(By.ID, 'mui-19215').send_keys("가공식품")
    time.sleep(1)

    create_driver.driver.find_element(By.NAME, 'allChecked').click()
    time.sleep(1)

    # [저장] 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="main__content"]/div[2]/header/div/div/div/button[2]').click()
    time.sleep(1)

