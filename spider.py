from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url='https://play.google.com/store/apps/'

driver.get(url)
time.sleep(2)

#title = driver.title


try:
    elems = driver.find_element(By.XPATH, "//a[@href]")
    #driver.find_element(By.XPATH, "//button[contains(@class, 'VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD mN1ivc VxpoF')]").click()
    time.sleep(1)
    #descargas = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div[3]/div[5]/div[2]').text
    #pub_date = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div[3]/div[8]/div[2]').text
    
except:
    print("Botón no encontrado")

time.sleep(2)

for elem in elems:
    print(elem.get_attribute("href"))


driver.quit