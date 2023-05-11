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
    #Si webdriver no está instalado lo descarga del paquete webdriver_manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    #Damos 2 segundos para que cargue la página
    time.sleep(2)

    # Si estamos en una categoría de apps devolvemos none
    if ('category' in url):
        print('Estamos dentro de una categoría')
        return None
    else:
        try:
            title = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[1]/div/div/c-wiz/div[2]/div[1]/div/h1/span').text
            #print(title)
            #Buscamos el botón más para ver las propiedades de la app
            driver.find_element(By.XPATH, "//button[contains(@class, 'VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD mN1ivc VxpoF')]").click()
            #print("Botón más encontrado")
            #Esperamos un segundo que cargue
            time.sleep(1)

            #Buscamos el cuadro de propiedades de la APP
            app_prop = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[4]/div[2]/div/div/div/div/div[2]/div[3]')
            #Sacamos todos los campos con datos que nos interesa de clase: reAt0
            props = app_prop.find_elements(By.CLASS_NAME, 'reAt0')
            #print(len(props))
            #print('Primer elemento:', props[0].text)
            #for i in range(len(props)):
            #    print('Elem: ', i, ' >', props[i].text)
            
            #Dependiendo de si el primer campo es el aviso de family share
            #hay que coger unos campos u otros porque se desplazan al mostrar ese nuevo campo
            if('información' in props[0].text): #Caso de family sharing
                up_date = props[2].text
                descargas = props[4].text
                pub_date = props[7].text
            else:                               #resto de caso, en principio que el campo 0 sea la versión
                up_date = props[1].text
                descargas = props[3].text
                pub_date = props[8].text
            #     print('Descargas:', props[i+1].text, 'campo anterior: ', props[i].text)
            # elif('Última actualización' in props[i].text):
            #     update_date = props[i+1].text
            print('Update:', up_date, descargas, pub_date)
        except:
            print("Botón no encontrado")
            #TODO ver si guardo las urls que fallen
    
    #TODO devolver objeto con las propiedades de la app
    #Falta por capturar: num de reviews, rate, descripción

    driver.quit

def main():
    cat = 'https://play.google.com/store/apps'
    url='https://play.google.com/store/apps/details?id=com.apalon.weatherlive'
    url1 = 'https://play.google.com/store/apps/details?id=com.apalon.weatherlive' # app con prop. familiar
    url2 = 'https://play.google.com/store/apps/details?id=com.coffeemeetsbagel' #app sin prop. familiar
    get_app(url1)

if __name__== "__main__" :
    main()