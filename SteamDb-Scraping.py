from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


driver=webdriver.Chrome()
url="https://steamdb.info/charts/"
driver.get(url)

listanombre=[]
listaactivos=[]
lista24h=[]
listapico=[]


pagina=driver.find_element(By.XPATH,f'//div[@class="dataTable_display"]/div[@class="dt-length"][1]/select[@class="dt-input"]')
pagina.click()
todolosdatos=driver.find_element(By.XPATH,f'//div[@class="dataTable_display"]/div[@class="dt-length"][1]/select[@class="dt-input"]/option[8]')
todolosdatos.click()
nombre_juego = driver.find_elements(By.XPATH, '//tr/td/a[normalize-space(text()) != ""]')
jugadores_activos=driver.find_elements(By.XPATH,'//tr/td[@class="dt-type-numeric"][1]')
pico_24h=driver.find_elements(By.XPATH,'//tr/td[@class="dt-type-numeric"][2]')
picohistorico=driver.find_elements(By.XPATH,'//tr/td[@class="dt-type-numeric"][3]')

for nombre_completo, activos, pico24, picoH in zip(nombre_juego, jugadores_activos, pico_24h, picohistorico):
    listanombre.append(nombre_completo.text)
    listaactivos.append(activos.text)
    lista24h.append(pico24.text)
    listapico.append(picoH.text)

datosunidos={'Nombre':listanombre,'Jugadores Activos':listaactivos,'Pico de 24H':lista24h ,'Pico Historico':listapico}
df=pd.DataFrame(datosunidos,columns=['Nombre','Jugadores Activos','Pico de 24H','Pico Historico'])
print(df)
df.to_csv('datos_steam.csv',index=False)
