#SteamDB Scraping Web 
Este es un pequeño proyecto personal que utiliza Selenium para automatizar la interacción con páginas web y Pandas para procesar y analizar los datos recopilados 

##Explicacion de los codigos:

####1.-SteamDb-Scraping.py
Este codigo nos permite sacar informacion de la pagina [SteamDb/charts](https://steamdb.info/charts/) extrayendo la informacion de las paginas que nosotros queramos sin un limite de tope
####Paso a paso del Codigo

se procede a instalar las librerias que usaremos  para el web scraping 

		pip install selenium
		pip install pandas

Una vez instalados los programas se procede a importar las librerias.


	from selenium import webdriver
	#"By" es esencial en Selenium para especificar cómo localizar elementos en una página web.
	from selenium.webdriver.common.by import By
	#pandas es una herramienta fundamental para el análisis y manipulación de datos en Python
	import pandas as pd

	driver = webdriver.Chrome()  # Crea una instancia del navegador Chrome
	url = "https://steamdb.info/charts/"  # Define la URL de la página web a visitar
	driver.get(url)  # Abre el navegador y carga la página especificada

Una vez se termina de configrar el navegador especificaremos donde se guardaran los datos que sacaremos

	listanombre=[]
	listaactivos=[]
	lista24h=[]
	listapico=[]
Ahora veremos el codigo que usaremos para extraer la informacion en este caso usaremos 2 ciclos for 

	for num in range(1, 40):  # Recorre los números del 1 al 39 (rango de 1 a 40 sin incluir el 40)
			pagina = driver.find_element(By.XPATH, f'//button[contains(text(),{num})]')  # Encuentra el botón con el número actual en el texto
			pagina.click()  # Hace clic en el botón encontrado para cargar la siguiente página o sección
			nombre_juego = driver.find_elements(By.XPATH, '//tr/td/a[normalize-space(text()) != ""]')  # Encuentra los nombres de los juegos (enlaces) en la página
			jugadores_activos = driver.find_elements(By.XPATH, '//tr/td[@class="dt-type-numeric"][1]')  # Encuentra el número de jugadores activos
			pico_24h = driver.find_elements(By.XPATH, '//tr/td[@class="dt-type-numeric"][2]')  # Encuentra el pico de jugadores en las últimas 24 horas
			picohistorico = driver.find_elements(By.XPATH, '//tr/td[@class="dt-type-numeric"][3]')  # Encuentra el pico histórico de jugadores
			#En este for hacemos que los datos obtenidos se dirigan a las listas que creamos primero 
			for nombre_completo, activos, pico24, picoH in zip(nombre_juego, jugadores_activos, pico_24h, picohistorico):  # Recorre todos los elementos encontrados en paralelo
					listanombre.append(nombre_completo.text)  # Añade el nombre del juego a la lista 'listanombre'
					listaactivos.append(activos.text)  # Añade el número de jugadores activos a la lista 'listaactivos'
					lista24h.append(pico24.text)  # Añade el pico de jugadores en las últimas 24 horas a la lista 'lista24h'
					listapico.append(picoH.text)  # Añade el pico histórico de jugadores a la lista 'listapico'

Finalmente todos los datos obtenidos por el programa se guadaran en un archivo csv para su uso.
```
datosunidos = {'Nombre': listanombre, 'Jugadores Activos': listaactivos, 'Pico de 24H': lista24h, 'Pico Historico': listapico}  # Crea un diccionario con los datos recopilados
df = pd.DataFrame(datosunidos, columns=['Nombre', 'Jugadores Activos', 'Pico de 24H', 'Pico Historico'])  # Convierte el diccionario a un DataFrame de pandas
print(df)  # Muestra el DataFrame por consola
df.to_csv('datos_steam.csv', index=False)  # Guarda el DataFrame como un archivo CSV sin el índice
```
