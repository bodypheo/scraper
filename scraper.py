from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def is_category_app(url):
    if('/apps' in url):
        return 1
    else:
        return 0

def is_app(url):
    if('store/apps/details' in url):
        return 1
    else:
        return 0

def get_app(url):
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    #url='https://play.google.com/store/apps/details?id=com.apalon.weatherlive'

    driver.get(url)
    time.sleep(2)

    #title = driver.title
    if ('category' in url):
        print('Estamos dentro de una categoría')
        return None
    else:
        title = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span').text

    try:
        driver.find_element(By.XPATH, "//button[contains(@class, 'VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD mN1ivc VxpoF')]").click()
        print("Botón más encontrado")
        time.sleep(1)
        descargas = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div[3]/div[5]/div[2]').text
        print(descargas)
        pub_date = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div[3]/div[8]/div[2]').text
        update_date = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div[3]/div[3]/div[2]').text
    except:
        print("Botón no encontrado")

    time.sleep(2)
    print(title, "descargas:", descargas, pub_date, update_date)
    driver.quit