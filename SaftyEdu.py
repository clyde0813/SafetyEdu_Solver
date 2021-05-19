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

main_page = driver.current_window_handle
wait2.until(lambda driver: 2 == len(driver.window_handles))
for i in driver.window_handles:
    if i != main_page:
        popup_page = i
driver.switch_to.window(popup_page)
driver.maximize_window()
print("팝업창 감지")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ctrlBtn.volumeBtn.on"))).click()
print("무음 ON")
while True:
    if len(driver.find_elements_by_class_name("textBubble.view")) > 0:
        driver.find_element_by_class_name("textBubble.view").click()
        print("자동 넘기기 완료")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ctrlBtn.volumeBtn.on"))).click()
    elif len(driver.find_elements_by_class_name("motion.quizStartBtn.sudden.view")) > 0:
        driver.find_element_by_class_name("motion.quizStartBtn.sudden.view").click()
        print("퀴즈 진입")
        driver.find_element_by_class_name("option.option_1.option_o").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btns.correctBtn"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "textBubble.view"))).click()
        if len(driver.find_elements_by_class_name("btns.correctBtn")) > 0:
            driver.find_element_by_class_name("option.option_1.option_o").click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btns.correctBtn"))).click()
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "textBubble.view"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ctrlBtn.volumeBtn.on"))).click()
    elif len(driver.find_elements_by_class_name("motion.quizStartBtn.view")) > 0:
        print("마지막 퀴즈")
        driver.find_element_by_class_name("motion.quizStartBtn.view").click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "moveBtn.nextPageBtn"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ctrlBtn.volumeBtn.on"))).click()

    elif len(driver.find_elements_by_class_name("textBubble.complete.view")):
        if len(driver.window_handles) > 1:
            print("학습 완료")
            for i in driver.window_handles:
                if i != main_page:
                    driver.switch_to.window(i)
                    driver.close()
        driver.switch_to.window(main_page)
        driver.refresh()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "courseBtn"))).click()
        wait2.until(lambda driver: 2 == len(driver.window_handles))
        for i in driver.window_handles:
            if i != main_page:
                popup_page = i
        driver.switch_to.window(popup_page)
        print("팝업창 감지")
        driver.maximize_window()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ctrlBtn.volumeBtn.on"))).click()
        print("무음 ON")
    else:
        pass
