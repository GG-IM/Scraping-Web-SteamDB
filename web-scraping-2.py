#para ejecutar el codigo escribir   py .\web-scraping-2.py
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
#se usa pandas apara ponerlo en archivo csv y columnas
import pandas as pd
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
url="https://steamdb.info/charts/"
driver.get(url)

#se crean las listas que se van a usar
listanombre=[]
listaactivos=[]
lista24h=[]
listapico=[]


#num para que empieze desde el numero 1 con el range(1,21)siendo el segundo valor el maximo al que llegara osea al 20 por que se le resta 1 
for num in range(1,40):
    #se le añade el f para Cuando se usa una f-string, cualquier expresión dentro de las llaves {} 
    # f al inicio indica que es una f-string.----{num} es la variable que queremos insertar dentro del XPath.---Cuando Python ejecuta este código, reemplaza {num} por el valor actual de la variable num en cada iteración del bucle.
    

    pagina=driver.find_element(By.XPATH,f'//button[contains(text(),{num})]')
    pagina.click()

    #toda la funcion de arriba permite cambiar las paginas entre los valores num
    #la de abajo al ejecutarse el cambio de pagina obtiene los nombres de juegos y los imprime
    #empezamos por los nombres de los juegos 
    #se uso el normalize-space(text()) Elimina espacios en blanco al inicio y al final del texto.
    # != "": Verifica que el texto no esté vacío. y tambien Excluye elementos <a> que no tienen texto o cuyo contenido es solo espacios en blanco.
    nombre_juego = driver.find_elements(By.XPATH, '//tr/td/a[normalize-space(text()) != ""]')
    jugadores_activos=driver.find_elements(By.XPATH,'//tr/td[@class="dt-type-numeric"][1]')
    pico_24h=driver.find_elements(By.XPATH,'//tr/td[@class="dt-type-numeric"][2]')
    picohistorico=driver.find_elements(By.XPATH,'//tr/td[@class="dt-type-numeric"][3]')

    for nombre_completo, activos, pico24, picoH in zip(nombre_juego, jugadores_activos, pico_24h, picohistorico):
        listanombre.append(nombre_completo.text)
        listaactivos.append(activos.text)
        lista24h.append(pico24.text)
        listapico.append(picoH.text)



#se crea un diccionario que contiene todo los datos
datosunidos={'Nombre':listanombre,'Jugadores Activos':listaactivos,'Pico de 24H':lista24h ,'Pico Historico':listapico}

#se crea la variable df para las columnas se pone tal cual esta en el diccionario si no da error
df=pd.DataFrame(datosunidos,columns=['Nombre','Jugadores Activos','Pico de 24H','Pico Historico'])
print(df)

#ahora crearemos el csv
df.to_csv('datos_steam.csv',index=False)

time.sleep(15)