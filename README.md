# SteamDB Scraping Web 
Este es un pequeño proyecto personal que utiliza Selenium para automatizar la interacción con páginas web y Pandas para procesar y analizar los datos recopilados 

## Explicacion de los codigos:

#### 1.-SteamDb-Scraping.py
Este codigo nos permite sacar informacion de la pagina [SteamDb/charts](https://steamdb.info/charts/) extrayendo la informacion de las paginas 1 al 80 
#### Paso a paso del Codigo

se procede a instalar las librerias que usaremos  para el web scraping 
```python
pip install selenium
pip install pandas
```
Una vez instalados los programas se procede a importar las librerias.

```python
	from selenium import webdriver
	#"By" es esencial en Selenium para especificar cómo localizar elementos en una página web.
	from selenium.webdriver.common.by import By
	#pandas es una herramienta fundamental para el análisis y manipulación de datos en Python
	import pandas as pd
```
```python
	driver = webdriver.Chrome()  # Crea una instancia del navegador Chrome
	url = "https://steamdb.info/charts/"  # Define la URL de la página web a visitar
	driver.get(url)  # Abre el navegador y carga la página especificada
```
Una vez se termina de configrar el navegador especificaremos donde se guardaran los datos que sacaremos
```python
	listanombre=[]
	listaactivos=[]
	lista24h=[]
	listapico=[]
```
Ahora veremos el codigo que usaremos para extraer la informacion en este caso usaremos 2 ciclos for 
```python
	for num in range(1, 40):  # si queremos extraer hasta la pagina 80 solo cambiariamos el 40 por culaquier numero de pagina que queramos
 
		pagina = driver.find_element(By.XPATH, f'//button[contains(text(),{num})]')  # Encuentra el botón con el número actual en el texto
		pagina.click()  # Hace clic en el botón encontrado para cargar la siguiente página o sección
  
		nombre_juego = driver.find_elements(By.XPATH, '//tr/td/a[normalize-space(text()) != ""]')  # Encuentra los nombres de los juegos (enlaces) en la página
		jugadores_activos = driver.find_elements(By.XPATH, '//tr/td[@class="dt-type-numeric"][1]')  # Encuentra el número de jugadores activos
		pico_24h = driver.find_elements(By.XPATH, '//tr/td[@class="dt-type-numeric"][2]')  # Encuentra el pico de jugadores en las últimas 24 horas
		picohistorico = driver.find_elements(By.XPATH, '//tr/td[@class="dt-type-numeric"][3]')  # Encuentra el pico histórico de jugadores
  
		#En este for hacemos que los datos obtenidos se dirigan a las listas que creamos primero 
		for nombre_completo, activos, pico24, picoH in zip(nombre_juego, jugadores_activos, pico_24h, picohistorico):# Recorre todos los elementos encontrados en paralelo
  
			listanombre.append(nombre_completo.text)  # Añade el nombre del juego a la lista 'listanombre'
			listaactivos.append(activos.text)  # Añade el número de jugadores activos a la lista 'listaactivos'
			lista24h.append(pico24.text)  # Añade el pico de jugadores en las últimas 24 horas a la lista 'lista24h'
			listapico.append(picoH.text)  # Añade el pico histórico de jugadores a la lista 'listapico'
```
Finalmente todos los datos obtenidos por el programa se guadaran en un archivo csv para su uso.
```python
datosunidos = {'Nombre': listanombre, 'Jugadores Activos': listaactivos, 'Pico de 24H': lista24h, 'Pico Historico': listapico}  # Crea un diccionario con los datos recopilados
df = pd.DataFrame(datosunidos, columns=['Nombre', 'Jugadores Activos', 'Pico de 24H', 'Pico Historico'])  # Convierte el diccionario a un DataFrame de pandas
print(df)  # Muestra el DataFrame por consola
df.to_csv('datos_steam.csv', index=False)  # Guarda el DataFrame como un archivo CSV sin el índice
```
Para terminar y lograr ejecutar el programa se abre la terminal y se inicia con el nombre
```python
py SteamDb-Scraping.py
```

#### 2.-SteamDb-Uni.py
Este segundo codigo nos permite sacar la informacion de cada juego ingresando y extrayendo los datos

#### Paso a paso del Codigo
se procede a instalar las librerias que usaremos  para el web scraping 
```python
pip install selenium
pip install pandas
```
Una vez instalados los programas se procede a importar las librerias:

```python
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from seleniumbase import SB
```

Una vez se importa los datos procedemos declarar la web que se va utilizar
`uc=True:`: Activa el "modo undetected-chromedriver", lo que significa que intenta evitar que los sitios web detecten el uso de herramientas de automatización como Selenium.
`test=True:` Activa el modo de pruebas, que podría implicar funcionalidades adicionales como registros o simulaciones específicas para depurar o verificar el código.
`disable_csp=True:` Desactiva la "Política de Seguridad de Contenidos" (Content Security Policy). Esto permite cargar scripts y recursos que de otro modo estarían bloqueados por restricciones del sitio web.

```python
	driver = webdriver.Chrome()  # Crea una instancia del navegador Chrome
	url = "https://steamdb.info/charts/"  # Define la URL de la página web a visitar
	driver.get(url)  # Abre el navegador y carga la página especificada
```
Procedemos a realizar una funcion para poder llamarla luego y acortar el codigo
`find_element` es un método utilizado para localizar un solo elemento en el DOM (Document Object Model) de una página web. 
`.text` esta propiedad obtiene el texto visible dentro del elemento HTML seleccionado.
`.strip()` es un método de cadenas en Python que elimina los espacios en blanco al principio y al final de una cadena de texto.
```python
def obtener_texto_o_null(xpath):  
    try:  
        elemento = sb.find_element(By.XPATH, xpath)  
        # Busca un elemento en la página usando el XPath proporcionado.
        return elemento.text if elemento.text.strip() else "NULL"  
        # Si el texto está vacío, devuelve la cadena "NULL".
    except NoSuchElementException:  
        return "null"  
        # Devuelve "null" para indicar que el elemento no existe en el DOM.
```

Una vez se termina de configrar el navegador especificaremos donde se guardaran los datos que sacaremos

```python
    listaid=[]
    listatipo=[]
    listasistema=[]
    listalanzamiento=[]
    listarpositiva=[]
    listarnegativa=[]
    listaseguidores=[]
    listatop=[]
    listanombrecompleto=[]
```

Para no tener problemas se procede a selecionar todos los elementos de SteamDB

```python
    pagina=sb.find_element(By.XPATH,f'//div[@class="dataTable_display"]/div[@class="dt-length"][1]/select[@class="dt-input"]')
    pagina.click()
    todolosdatos=sb.find_element(By.XPATH,f'//div[@class="dataTable_display"]/div[@class="dt-length"][1]/select[@class="dt-input"]/option[8]')
    todolosdatos.click()
```
Ahora veremos la parte de la extraccion de datos parte por parte
`.uc_click` es un método especializado para hacer clic en un elemento sin ser detectado como un bot, en automatización web.
`.sleep` es una función de la biblioteca estándar de Python que hace que el programa se detenga por un período específico de tiempo, en segundos.
`.append`  es un método de listas en Python que se utiliza para agregar un elemento al final de una lista.
`.go_back`  simula que el navegador navega hacia la página anterior (como presionar el botón de "Atrás" en un navegador).
```python
    for i in range(1,4):# esta parte nos muestra desde que lugar queremos que inicie la extraccion desde el 1 hasta el 4 elementos si deseamos podemos cambiar a los numeros que queramos
        sb.uc_click(f"tr:nth-of-type({i}) td a", 2) 
        sb.sleep(1)
       
        nombre_id = tipo_juego = sistemas_soporte = fecha_lanzamiento = None
        resena_positiva = resena_negativa = numero_seguidores = top_ventas = None
        try:
            nombrejuegocompleto=obtener_texto_o_null('//div/div[@class="d-flex flex-grow"]/h1')
            print(nombrejuegocompleto)
        except Exception as e:
            print(f"null")

        try:
            nombre_id=obtener_texto_o_null('//tr[td[@class="span3" and contains(text(), "App ID")]]/td[2]')
            print(nombre_id)
        except Exception as e:
            print(f"null")

        try:
            tipo_juego=obtener_texto_o_null('//td[text()="App Type"]/following-sibling::td')
            print(tipo_juego)
        except Exception as e:
            print(f"null")

        try:
            sistemas_soporte = obtener_texto_o_null('//td[text()="Supported Systems"]/following-sibling::td')
            print(sistemas_soporte)
        except Exception as e:
            print(f"null") 

        try:
            fecha_lanzamiento = obtener_texto_o_null('//td[text()="Release Date"]/following-sibling::td')   
            print(fecha_lanzamiento)
        except Exception as e:
            print(f"null")

        try:   
            resena_positiva=obtener_texto_o_null('//div[@class="row row-app-charts"]//li[contains(text(), "positive reviews")][1]/strong')           
            print(resena_positiva)   
        except Exception as e:
            print(f"null")

        try:
            resena_negativa=obtener_texto_o_null('//div[@class="row row-app-charts"]//li[contains(text(), "negative reviews")][1]/strong')          
            print(resena_negativa)
        except Exception as e:
            print(f"null")

        try:   
            numero_seguidores=obtener_texto_o_null('//div[@class="row row-app-charts"]//li[contains(text(), "followers")][1]/strong')   
            print(numero_seguidores)  
        except Exception as e:
            print(f"null")  

        try:         
            top_ventas=obtener_texto_o_null('//div[@class="row row-app-charts"]//li[contains(text(), "in top sellers")][1]/strong')
            print(top_ventas)
        except Exception as e:
            print(f"null")

        nombrejuegocompleto=nombrejuegocompleto if nombrejuegocompleto is not None else "null"
        nombre_id = nombre_id if nombre_id is not None else "null"
        tipo_juego = tipo_juego if tipo_juego is not None else "null"
        sistemas_soporte = sistemas_soporte if sistemas_soporte is not None else "null"
        fecha_lanzamiento = fecha_lanzamiento if fecha_lanzamiento is not None else "null"
        resena_positiva = resena_positiva if resena_positiva is not None else "null"
        resena_negativa = resena_negativa if resena_negativa is not None else "null"
        numero_seguidores = numero_seguidores if numero_seguidores is not None else "null"
        top_ventas = top_ventas if top_ventas is not None else "null"


        listanombrecompleto.append(nombrejuegocompleto)
        listaid.append(nombre_id)
        listatipo.append(tipo_juego)
        listasistema.append(sistemas_soporte)
        listalanzamiento.append(fecha_lanzamiento)
        listarpositiva.append(resena_positiva)
        listarnegativa.append(resena_negativa)
        listaseguidores.append(numero_seguidores)
        listatop.append(top_ventas)
        
        sb.go_back()
        sb.sleep(1.8)
```
Ahora se procede con la creacion del un diccionario de datos para guardar los archivos que listamos con append
```python
    datosunidos={'Nombre juego':listanombrecompleto ,
                'ID':listaid,'Tipo Juego':listatipo,'Sistemas Operativo':listasistema,'Lanzamiento':listalanzamiento,
                'Reseña Positiva':listarpositiva,'Reseña Negativa ':listarnegativa,'Seguidores':listaseguidores,
                'Top Ventas':listatop}

```
Este código recorre el diccionario llamado datosunidos y, para cada par clave-valor (key-value) en el diccionario, imprime una línea indicando la clave y la cantidad de elementos asociados a esa clave.

```python
    for key, value in datosunidos.items():
        print(f"'{key}': {len(value)} elementos")    
```

Ahora se usa pandas para la creacion del archivo CSV.

```python
    df=pd.DataFrame(datosunidos,columns=['Nombre juego','ID','Tipo Juego','Sistemas Operativo',
                                            'Lanzamiento','Reseña Positiva','Reseña Negativa','Seguidores','Top Ventas'])
    print(df)
    df.to_csv('datos_steam2.csv',index=False)
```
Para finalizar y correr el script usamos
```python
py SteamDb-Uni.py
```


