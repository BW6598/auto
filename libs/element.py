from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 로딩될 때까지 대기
from selenium.webdriver.support import expected_conditions as EC  # 로딩될 때까지 대기
import time
from libs import login
import random

randomNumT = random.randrange(1, 1000)
randomNumI = random.randrange(1000, 10000)

# xpath로 버튼 클릭
def ClickByXPath(element, num):
    '''
    xpath로 버튼 클릭
    :param element: XPath
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.XPATH, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# css_selector로 버튼 클릭
def ClickByCSS_SELECTOR(element, num):
    '''
    css_selector로 버튼 클릭
    :param element: css_selector
    :param num: TC_num
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.CSS_SELECTOR, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# linktext로 버튼 클릭
def ClickByLINKTEXT(element, num):
    '''
    linktext로 버튼 클릭
    :param element: linktext
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.LINK_TEXT, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# id로 버튼 클릭
def ClickByID(element, num):
    '''
    id로 버튼 클릭
    :param element: ID
    :param num: TC_number
    :return:
    '''

    try:
        login.create_driver.driver.find_element(By.ID, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# name으로 버튼 클릭
def ClickByName(element, num):
    '''
    name으로 버튼 클릭
    :param element: NAME
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.NAME, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Name으로 버튼 클릭(인덱스사용)
def ClickByNameIndex(element, index, num):
    '''
    Name으로 버튼 클릭(인덱스사용)
    :param element: NAME 요소
    :param index: 인덱스
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_elements(By.NAME, value=element)[int(index)].click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# classname으로 버튼 클릭
def ClickByClassName(element, num):
    '''
    classname으로 버튼 클릭
    :param element: ClassName
    :param num: TC_number
    :return:
    '''
    try:
        login.create_driver.driver.find_element(By.CLASS_NAME, value=element).click()
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# xpath로 inputbox 내용 입력
def InputByXPath(element, input, num):
    '''
    xpath로 inputbox 내용 입력
    :param element: XPath
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''

    try:
        login.create_driver.driver.find_element(By.XPATH, value=element).clear()
        login.create_driver.driver.find_element(By.XPATH, value=element).send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Name으로 inputbox 내용 입력
def InputByName(element, input, num):
    '''
    Name으로 inputbox 내용 입력
    :param element: Name
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''

    try:
        login.create_driver.driver.find_element(By.NAME, value=element).clear()
        login.create_driver.driver.find_element(By.NAME, value=element).send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False


# Name으로 inputbox 내용 입력(인덱스사용)
def InputByNameIndex(element, index, input, num):
    '''
    Name으로 inputbox 내용 입력(인덱스사용)
    :param element: Name
    :param index: 인덱스
    :param input: input box 입력 내용
    :param num: TC_number
    :return:
    '''
    try:
        name_index = login.create_driver.driver.find_elements(By.NAME, value=element)[int(index)]
        name_index.clear()
        name_index.send_keys(input)
        time.sleep(1)
        print("TC " + num + " PASS")
        return True
    except Exception as e:
        print(e)
        print("TC " + num + " Fail")
        return False
