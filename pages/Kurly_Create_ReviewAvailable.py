import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
from libs import create_driver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import random
from libs import login



# 컬리몰 상품 구매
def purchase():
    # 컬리 버튼 있는지 확인
    # WebDriverWait(create_driver.driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div[1]/img')))
    #
    # # 컬리 버튼 클릭(홈으로 이동)
    # create_driver.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div[2]/div[1]/img').click()
    # time.sleep(2)
    #
    # create_driver.driver.find_element(By.id, 'gnb_search').send_keys(randomPrice)
    # time.sleep(2)

    url = 'https://www.stg.kurly.com/goods/1000051603'
    create_driver.driver.get(url)

    # 장바구니 버튼 있는지 확인
    WebDriverWait(create_driver.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="product-atf"]/section/div[5]/div[3]/div/button')))

    # 장바구니 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="product-atf"]/section/div[5]/div[3]/div/button').click()
    time.sleep(1)

    # 장바구니로 이동
    create_driver.driver.find_element(By.XPATH, '//*[@id="top"]/div[2]/div[1]/div[2]/div[3]/div/div[2]/button').click()

    # 주문하기 버튼 있는지 확인
    WebDriverWait(create_driver.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[2]/div/div[3]/button')))

    # 주문하기 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[2]/div[2]/div/div[3]/button').click()
    time.sleep(2)

    # 적립금 inputbox 있는지 확인
    WebDriverWait(create_driver.driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'point-usage')))

    create_driver.driver.find_element(By.NAME, 'point-usage').click()
    time.sleep(2)

    # 적립금 [모두사용] 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[7]/div[1]/div[6]/div/div[1]/button').click()

    # [결제하기] 버튼 클릭
    create_driver.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[7]/div[1]/div[11]/button').click()
    time.sleep(2)

    # 주문 되었는지 확인
    # WebDriverWait(create_driver.driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/p')))
    time.sleep(2)

    orderNum = create_driver.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div/div/div[2]/div[2]/p').text


    url = 'https://lacms2.stg.kurlycorp.kr/signin'
    create_driver.driver.get(url)

    # id inputbox 있는지 확인
    WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.ID,'username')))

    # 아이디/비밀번호 입력
    create_driver.driver.find_element(by=By.NAME,
                                      value='username').send_keys('byungwook.lee@kurlycorp.com')
    create_driver.driver.find_element(by=By.NAME,
                                      value='password').send_keys('quddnr414@')

    # 로그인 버튼 클릭
    create_driver.driver.find_element(by=By.XPATH,
                                      value='//*[@id="root"]/div/form/button').click()

    # 주문 > 주문리스트 클릭
    WebDriverWait(create_driver.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav"]/div[4]/div/span')))
    create_driver.driver.find_element(by=By.XPATH,value='//*[@id="nav"]/div[4]/div/span').click()
    create_driver.driver.find_element(by=By.XPATH,value='//*[@id="nav"]/div[5]/div/div/div/div[1]/a').click()
    time.sleep(2)

    # 주문 번호 검색
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="searchCategory"]').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="menu-searchCategory"]/div[3]/ul/li[2]').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.ID, value='searchKeyword').send_keys(orderNum)
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="main__content"]/div[1]/div/div/div[5]/div/button[1]').click()
    time.sleep(1)

    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="main__content"]/div[3]/table/tbody/tr/td[3]').click()
    time.sleep(1)

    # 주문상태변경
    WebDriverWait(create_driver.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div')))

    # 배송준비중으로 변경
    create_driver.driver.find_element(by=By.XPATH,
                                      value='//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH,value='//*[@id="menu-"]/div[3]/ul/li[1]').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/button/span[1]').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH,
                                      value='/html/body/div[5]/div[3]/div/div[3]/button/span[1]').click()
    time.sleep(1)

    # 배송중으로 변경
    create_driver.driver.find_element(by=By.XPATH,
                                      value='//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="menu-"]/div[3]/ul/li[2]').click()
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/button/span[1]').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH,
                                      value='/html/body/div[5]/div[3]/div/div[3]/button/span[1]').click()
    time.sleep(1)

    # 배송완료로 변경
    create_driver.driver.find_element(by=By.XPATH,
                                      value='//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/div/div/div/div').click()
    time.sleep(1)
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="menu-"]/div[3]/ul/li[3]').click()
    create_driver.driver.find_element(by=By.XPATH, value='//*[@id="main__content"]/div/div[3]/div/div/div[1]/div[2]/button/span[1]').click()
    time.sleep(1.5)
    create_driver.driver.find_element(by=By.XPATH,
                                      value='/html/body/div[5]/div[3]/div/div[3]/button/span[1]').click()
    time.sleep(1)

    # 배송완료 확인
    create_driver.driver.refresh()
    time.sleep(2)
    state = create_driver.driver.find_element(by=By.XPATH, value='//*[@id="main__content"]/div/div[3]/div/div/div[5]/table/tbody/tr[1]/td[19]').text
    if(state == "배송완료"):
        print("배송완료로 변경 완료")

    else:
        print("배송완료가 아니고,"+ state + " 상태임..")













