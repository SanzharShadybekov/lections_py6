from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


base_url = 'https://translate.yandex.ru/?source_lang=ru&target_lang=ky'
chrome_options = webdriver.ChromeOptions()


def get_page_html_selenium(url, data):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'fakearea-container'))
    )

    input_element = driver.find_element(By.CSS_SELECTOR, '.textinput')
    input_element.send_keys("Привет!, как дела? все хорошо ?")

    sleep(1)

    res_text = driver.find_element(By.CSS_SELECTOR, '.translation')
    print(res_text.text)

    driver.quit() 
    return res_text


get_page_html_selenium(base_url, '1')