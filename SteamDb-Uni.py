from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from seleniumbase import SB

with SB(uc=True, test=True, disable_csp=True) as sb:
    url = "https://steamdb.info/charts/"
    sb.uc_open_with_reconnect(url, 3)

    def obtener_texto_o_null(xpath):
        try:
            elemento = sb.find_element(By.XPATH, xpath)
            return elemento.text if elemento.text.strip() else "NULL"
        except NoSuchElementException:
            return "null"  

    listaid=[]
    listatipo=[]
    listasistema=[]
    listalanzamiento=[]
    listarpositiva=[]
    listarnegativa=[]
    listaseguidores=[]
    listatop=[]
    listanombrecompleto=[]



    pagina=sb.find_element(By.XPATH,f'//div[@class="dataTable_display"]/div[@class="dt-length"][1]/select[@class="dt-input"]')
    pagina.click()
    todolosdatos=sb.find_element(By.XPATH,f'//div[@class="dataTable_display"]/div[@class="dt-length"][1]/select[@class="dt-input"]/option[8]')
    todolosdatos.click()

    for i in range(1,4):
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


    datosunidos={'Nombre juego':listanombrecompleto ,
                'ID':listaid,'Tipo Juego':listatipo,'Sistemas Operativo':listasistema,'Lanzamiento':listalanzamiento,
                'Reseña Positiva':listarpositiva,'Reseña Negativa ':listarnegativa,'Seguidores':listaseguidores,
                'Top Ventas':listatop}


    for key, value in datosunidos.items():
        print(f"'{key}': {len(value)} elementos")    


    df=pd.DataFrame(datosunidos,columns=['Nombre juego','ID','Tipo Juego','Sistemas Operativo',
                                            'Lanzamiento','Reseña Positiva','Reseña Negativa','Seguidores','Top Ventas'])
    print(df)
    df.to_csv('datos_steam2.csv',index=False)


