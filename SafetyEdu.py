from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException, UnexpectedAlertPresentException, \
    ElementClickInterceptedException, NoAlertPresentException, ElementNotInteractableException, NoSuchElementException
import os

driver = webdriver.Chrome(os.getcwd() + "//es//chromedriver.exe")
url = "http://safetyedu.org/Edu/SafetyEduRoom"
driver.get(url)
wait = WebDriverWait(driver, 10)
wait2 = WebDriverWait(driver, 6000)

wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "chosen-single"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="frmStudent"]/div[1]/div[1]/div/div/div/input'))).send_keys(
    "목포대학교")
driver.find_element_by_xpath('//*[@id="frmStudent"]/div[1]/div[1]/div/div/div/input').send_keys(Keys.ENTER)
wait2.until(EC.element_to_be_clickable((By.CLASS_NAME, "applicationBtn"))).click()
main_page = driver.current_window_handle
wait2.until(EC.element_to_be_clickable((By.CLASS_NAME, "courseBtn"))).click()
print("팝업창 감지")

while True:
    wait2.until(lambda driver: 2 == len(driver.window_handles))
    for i in driver.window_handles:
        if i != main_page:
            popup_page = i
    driver.switch_to.window(popup_page)
    driver.maximize_window()
    wait2.until(EC.element_to_be_clickable((By.CLASS_NAME, "textBubble.view")))
    num = driver.find_element_by_class_name("pageNum.tPageNum").text
    num = int(num) + 1
    print(num)
    driver.execute_script('opener.PageLast(' + str(num) + ');')
    wait2.until(lambda driver: 1 == len(driver.window_handles))
    driver.switch_to.window(main_page)
    wait2.until(EC.element_to_be_clickable((By.CLASS_NAME, "courseBtn"))).click()

