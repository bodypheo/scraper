from sys import exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from scraper import get_app
from scraper import is_app
from scraper import is_category_app
###########
#Función para obtener los links de una url
###########
def get_links(url):
    options = Options()
    options.add_argument("--disable-extensions")
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(2)

    try:
        elems = driver.find_elements(By.TAG_NAME, 'a')
        print("Enlaces encontrados")
        
    except:
        print("Enlaces no encontrados")

    time.sleep(2)
    lista_url = []
    for elem in elems:
        href = elem.get_attribute("href")
        if href is not None:
            if href not in lista_url:
                lista_url.append(href)
    driver.quit()
    return(lista_url)

###########
#Función que devuelve una url de la cola
###########
def get_url_from_q(file):
    
    url = ''

    with open(file, 'r') as fin:
        data = fin.read().splitlines(True)
        fin.close()
    with open(file, 'w') as fout:
        fout.writelines(data[1:])
        fout.close()
    if (data):
        url = data[0]
    else:
        print('No quedan urls ninio, solo masibon')
        exit()
    return(url)

###########
#Función para comprobar si una url está en un archivo
###########
def url_in_q(url, file):
    with open(file, 'r') as fin:
        if url in fin.read():
            fin.close
            return 1
        else:
            fin.close
            return 0


###########
#Función para añadir una url a a l cola
###########
def add_url_to_q(lista_urls, file):
    print(len(lista_urls))

#Bloque pa borrar después de debug    
    with open('urls_brutas.log', 'w') as fout: #testing files
        fout.write('\n'.join(lista_urls))
        fout.close()
##

    #We remove items that !is_category_app (have /apps in url)
    for i in lista_urls[:]:
        if not is_category_app(i):
            lista_urls.remove(i)

#Bloque pa borrar después de debug
    print(len(lista_urls))
    with open("urls_cat_app.log", 'w') as fout: # Limpieza de categorías
        fout.write('\n'.join(lista_urls))
        fout.close()
##
   
    #Check if url is in the queue
    urls_to_remove=[]
    for i in lista_urls:
        print(i)
        if url_in_q(i, file):
            print("Eliminada de la lista:", i)
            urls_to_remove.append(i)
    for url in urls_to_remove:
        lista_urls.remove(url)

#Bloque pa borrar después de debug
    with open("urls_pa_guardar.log", 'w') as fichero: # Listado de líneas pa guardar
            fichero.write('\n'.join(lista_urls))
            fichero.close()
####            
    
    #TODO: check if url is in DB ver si la fecha de db es superior a un mes en ese caso actualizar datos.

    #Write the remaining urls that are not in the DB or in queue
    with open(file, 'a') as fout:
        print(len(lista_urls))
        fout.write("\n")
        fout.write('\n'.join(lista_urls))
        fout.close()

def main():
    #Todo: Poner while
    file = 'queue_url.txt'
    url = get_url_from_q(file)
    print("Visitamos:", url)
    #Si es una app, la metemos en BD y sacamos los links de la página de la APP
    if is_app(url):
        #TODO meter en DB
        print('check db')      
        add_url_to_q(get_links(url),file)
    #Si es una categoría sacamos los links de la página
    elif is_category_app(url):
        add_url_to_q(get_links(url),file)

if __name__== "__main__" :
    main()