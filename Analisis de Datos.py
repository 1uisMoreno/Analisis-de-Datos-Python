# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:27:24 2021

@author: Luis_Moreno
"""
import math
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA as pca

num1 = 50
num2 = 55

print(num1+num2)

print(str(num1)+str(num2))

rad = int(input("Dame el radio del circulo: "))

area = math.pi*(math.pow(rad, 2))

area = round(area,4)
print(f"El area del circulo es {area}")
num3 = 3.99
num3 = math.floor(int(num3))
print(num3)


cadena1 = "Luis Miguel Moreno Olmos"
cadena2 = "Angelina Gutierrez Zamora"
cadena3 = "3121743708"

cadena1.count("g")

centrar = cadena1.center(100)
print(centrar)

cadena1.index("o")
cadena1.find("u")

cadena1.lower()
cadena1.upper()

cad1 = cadena1.replace("o", "0")
print(cad1)

cad2 = cadena2.replace("a", "X",2)
print(cad2)

cadena2.upper()

#Listas Colecciones oredenadas, no indexadas y mutables

lista1 = [2,4,5,'Hola',[2,3,4,54,5]]
lista1.append(3)
print(lista1)
lista1.append('2')
lista1[-1]
lista1[4][-1]
del(lista1[1])
del(lista1[3][-1])
print(lista1)
lista1[3][-1] = True
print(lista1)

#Tuplas: Colecciones ordenadas, no indexadas  que son inmutables
#Son 
tup = (2,3,4,'hola',[6,5,0,True, False])
tup[2]
tup[4] = 3 #No se pueden modificar los valores
tup[2:]
tup[:-1]
del(tup[2])

#Set: Colecciones no ordenadas, mutables pero no repetitivas
set1 = {1,2,3,45,5,2,2,8,8,3,True}
print(set1)
set1.append(1)
print(set1)
set1.add(False)
set1.update([1,2,3,4,True,40]) #Nomas se agrega el 40 por que los demas ya se encuentran
set1.discard(False)
set1.discard(1)


#Diccionarios: Colecciones no ordenadas, indexadas, mutables que permiten indices duplicados

dic2 = {'Marcas':["Hp","Dell","Lenovo","Huawei","Macbook"],'Colores':["Verde","Rojo","Negro","Blanco"]}

dic2.keys()
dic2.values()
dic2.update({'Precio':5000})
cantidades = 50
dic2.update({'Cantidades':cantidades})
print(dic2)

#Sentencia IF-ELIF-ELSE

numero = int(input("Dame un numero: "))

if(numero%2==0):
    print("El numero es par y ")
    if (numero<10):
        print("es menor que 10")
    elif (numero<10 and numero<50):
        print("es mayor que 10 pero menos que 50")
    elif (numero>50 and numero<100):
        print("mayor que 50 y menor que 100")
    else:
        print("es mayor que 100")
else:
    print("El numero es impar y ")
    if (numero<10):
        print("es menor que 10")
    elif (numero<10 and numero<50):
        print("es mayor que 10 pero menos que 50")
    elif (numero>50 and numero<100):
        print("mayor que 50 y menor que 100")
    else:
        print("es mayor que 100")

#Ciclo For
rango = range(0,10,2)
for numero in rango:
    print(numero)
    
for index,numero in enumerate(rango):
    print("indie: "+ str(index) +" numero: "+ str(numero))
    
li = "LUISMI"
li2 = ["l","u","i","s","m","i"]
for ix,letra in enumerate(li):
    print(f"indie:{str(ix)} letra:{str(letra)} {li2[ix]}")
    
lista = [["hola","como","estas"],("Luis","Miguel","Moreno","Olmos")]
for contenido in lista:
    for ix1,contenido2 in enumerate(contenido):
        print(f"El Indice {ix1} del valor {contenido} es {contenido2} ")


contenedor = []

for contExt in lista:
    for contInt in contExt:
        contenedor.append([contExt, contInt, len(contInt)])


#CICLO WHILE

opc = input("Quieres jugar un juego [Y/N]): ")
if opc == "y" or opc=="Y":
        numero = int(input("Dame un numero positivo: "))
        while (numero<0):
            numero = int(input("Ese era negativo... intenta de nuevo:"))
        else:
            print("¡Muchas gracias!")
            

num1 = 0
while num1<10:
    print(num1)
    num1 += 1

#Funciones en Python
def cuadrado(numero):
    numCuad = numero**2
    return numCuad

hola = cuadrado(10)

import matplotlib.pyplot as plt

def parabola(minimo, maximo, step):
    x = []
    y = []
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**2)
    plt.plot(x,y)    
    return x,y

valoresX, valoresY = parabola(0, 55, 5)


#Argumentos ARBITRARIOS en Funciones


def Datos(*datos):
    tiposDatos = []
    for valores in datos:
        tiposDatos.append(type(valores).__name__)
    return tiposDatos

data = Datos(2,3,"hola",[1,2,3],(2,3,4),10,"Luis")

def precioSIva(**argumento):
    precioSinIva = argumento["precioPublico"]/(1+argumento["IVA"])
    return precioSinIva
    
data2 = round(precioSIva(precioPublico = 100, IVA = 0.16),4)

#Llamar funciones dentro de funciones

import matplotlib.pyplot as plt

def parabolaCuadrada(minimo, maximo, step):
    x = []
    y = []
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**2)
    plt.plot(x,y)    
    return x,y

def parabolaCubica(minimo, maximo, step):
    x = []
    y = []
    for valor in range(minimo,maximo,step):
        x.append(valor)
        y.append(valor**3)
    plt.plot(x,y)    
    return x,y

def elegirFuncion(minimo,maximo,step,valorParabola):
    if valorParabola == 1:
        return parabolaCuadrada(minimo, maximo, step)
    elif valorParabola == 2:
        return parabolaCubica(minimo, maximo, step)
    else:
        return print("Los valores no son correctos, vuelve a intentarlo")
    

x, y = elegirFuncion(-55, 55, 5, 2)    


import string

alfabeto = list(string.ascii_lowercase)

def cifradoCesar(alfabeto,n,texto):
    textoCifrado=""
    for letra in texto:
        if letra in alfabeto:
            indexActual=alfabeto.index(letra)
            indexCifrado=indexActual + n
            if indexCifrado > 25:
                indexCifrado -= 25
            textoCifrado += alfabeto[indexCifrado]
        else:
            textoCifrado+=alfabeto[letra]
    return textoCifrado
texto1 = "hola"
texto2 = cifradoCesar(alfabeto, 3, "hola")

def desifracion(alfabeto,n,texto):
    textoOriginal=""
    for letra in texto:
        if letra in alfabeto:
            indexActual=alfabeto.index(letra)
            indexOriginal=indexActual - n
            if indexOriginal < 0:
                indexOriginal += 25
            textoOriginal += alfabeto[indexOriginal]
        else:
            textoOriginal += alfabeto[letra]
    return textoOriginal
               
texto3 = desifracion(alfabeto, 3, "krod")            


"""
    ===================
    List comprehension
    ===================
""" 

pares=[]
for i in range(1,101):
    if i%2==0:
        pares.append(i)

pares_lc=[numero for numero in range(100) if numero%2==0]

pares_dc = {"ix: "+str(numero):numero for numero in range(101) if numero%2==0}

generador=(numero for numero in range(100) if numero%2==0)
generador=list(generador)

import numpy as np
import matplotlib.pyplot as plt

parabola=np.array([[x,x**2] for x in range(-10,11,1)])
plt.plot(parabola[:,0],parabola[:,1])

frases = ["la casa roja","papeleria tonatiuh la mejor","la luna roja de anoche"]
tokens = [palabra.split(" ") for palabra in frases]

frasesM = [palabra.upper() for palabra in frases]
tokensM = [palabra.split(" ") for palabra in frasesM]

"""Funciones lamda en Python (Funciones anonimas)"""

import math

mensaje = lambda x: "El nunmero ingresado es: " + str(x)
mensaje(5)

binomioCuadrado = lambda a,b: "El binomio cuadrado es: " + str(math.pow(a, 2) + (2*a*b) + math.pow(b, 2))  
binomioCuadrado(2,4)


def cubos(numero):
    numeroStr = str(numero)
    cubos = (int(numero)**3 for numero in numeroStr)

numCubicos = []
for i in range(100,1000):
    if i == cubos(i):
        numCubicos.append(i)
        
cubos = lambda digito: sum(int(digito)**3 for digito in str(digito))
digCubicos = [digito for digito in range(100,1000) if digito==cubos(digito)]

my_dict = {"A": 1, "B": 2, "C": 3}
sorted(mi_dicc, key=lambda x: my_dict[x]%3) 

"""Ejercicio comun"""
mi_lista = [10, 2, 30, 4, 50, 60, 70, 8, 90, 10, 1, 2]
filtrado = []
for numero in mi_lista:
    numeroStr = str(numero)
    if len(numeroStr) > 1:
        filtrado.append(numero)
        
"""List Comprehension"""        
filtrado_2 = [x for x in [10, 2, 30, 4, 50, 60, 70, 8, 90, 10, 1, 2] if len(str(x)) > 1]

"""Funciones lambda"""
mi_lista_3 = [10, 2, 30, 4, 50, 60, 70, 8, 90, 10, 1, 2]
filtrado_3 = filter(lambda x: len(str(x)) > 1, mi_lista)
list(filtrado_3)


"""
    ===========================
    Funciones de orden superior
    ===========================
""" 

frase = "La casa roja de la papeleria tona no esta de color rojo porque es de color azul"
tokens = frase.split()  

def filtrado(letra):    
    if len(letra) > 3:
        return True


list(filter(filtrado,tokens))

list(filter(lambda x: len(x) > 3, frase.split()))

numeros = [1,3,5,7,15,4,3,25,50]
list(filter(lambda x: x%5==0, numeros))

list(map(lambda letra: letra.upper(), tokens))

list(map(lambda x: x**2, numeros))

"""
    ========================
    Introduccion de numpy 1
    ========================
""" 


import numpy as np

escalar_0d = 10
vector_1d = np.array([1,2,3,4,5,6])
vector_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]],[[21,22,23],[24,25,26],[27,28,29]]])


vector_2d[2,0] #7
vector_2d[2,2] #9    
vector_3d[1,1,0] #14
vector_3d[1,2,2] #19
vector_3d[2,1,1] #25
vector_3d[2,2,1] #28
vector_3d[0,1,0] #4



"""
    ========================
    Introduccion de numpy 2
    ========================
""" 

import matplotlib.pyplot as plt

"""Operaciones basicas"""

vector_a = np.arange(100)
vector_b = np.arange(100)*(2)

suma_v = vector_a + vector_b
resta_v = vector_a - vector_b
multi_v = vector_a * vector_b
divi_v = vector_b / vector_a

"""Calculo de matrices"""

matriz = np.array([[1,2],[3,4]])

matriz.sum()
matriz.std()
matriz.mean()
matriz.max()
matriz.min()
matriz.__pow__(2)
matriz**2
inversa = np.linalg.inv(matriz)
transponer = np.transpose(matriz)

a = np.arange(9) - 4
b = a.reshape((3, 3))

c = np.arange(216)
d = c.reshape((6,6,6))

np.dot(matriz, inversa) #Matriz identidad

"""Ajuste polinomico"""

x= np.arange(-2,2.1,.1)

y = np.array([np.sin(valor * (180/np.pi)) for valor in x])
plt.plot(x, y)

coeficiente = np.polyfit(x,y,13)
y_estimada = np.polyval(coeficiente, x)
plt.plot(x,y_estimada)

z = np.array([np.cos(valor * (180/np.pi)) for valor in x])
plt.plot(x, z)

coeficiente = np.polyfit(x,z,16)
z_estimada = np.polyval(coeficiente, x)
plt.plot(x,z_estimada)


"""Numeros aleatorios en Numpy"""

numeros = 100000
uniformes = np.random.uniform(20,80,numeros)
plt.subplot(2,2,1)
plt.hist(uniformes, bins= 100)

normales = np.random.normal(50,10,numeros)
plt.subplot(2,2,2)
plt.hist(normales, bins=100)

triangular = np.random.triangular(20,50,80,numeros)
plt.subplot(2,2,3)
plt.hist(triangular, bins=100)

exponenciales = np.random.exponential(100,numeros)
plt.subplot(2,2,4)
plt.hist(exponenciales, bins=100)


"""
    ========================
    Introduccion de Pandas
    ========================
""" 


"""
    ## Principales caracterisiticas de pandas ##
    
    >> Carga de datos de distintas fuentes
    >> Transformaciones de datos
    >> Transformaciones de forma de las tablas
    >> Cálculo de medidas derivadas
    >> Análisis y visualización de datos
    >> Escritura de datos de distintas fuentes
    >> Mayor velocidad de ejecución y es menos tedioso
    
    >> El fuerte de pandas son sus dataFrames que son comparados con
    matrices de 2 dimenciones de numpy. la diferencia es que estas 
    tienen caracteristicas propias para una mejor obtencion y manejo
    de datos, ademas de indexación de filas y columnas
    

"""
import pandas as pd
import requests
#EXCEL
cancer_mama = pd.read_excel("breast_cancer.xlsx")

#CSV
titanic = pd.read_csv("https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
vinoRojo = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv",sep=";")
datosCovid = pd.read_csv("covid_20200430.csv")

#JSON
fake_json_covid = requests.get("https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=capacityPillarFour&metric=cumCasesByPublishDate&metric=cumPeopleVaccinatedFirstDoseByPublishDate&metric=cumPeopleVaccinatedSecondDoseByPublishDate&metric=hospitalCases&format=json&release=2021-12-23").json()
fake_datos_coronavirus = pd.DataFrame.from_dict(fake_json_covid["body"])
prodcutos = pd.read_json("producto.json")

datosCovid.info()

vinoRojo.describe()

muestraCancer = cancer_mama.head(10)

muestraTitanic = titanic.tail(10) 

"""
    =====================================
    Manipulacion de DataFrames en Pandas
    =====================================
""" 

"""Shape dataframe"""
type(datosCovid)
datosCovid.shape

"""Columnas dataframe"""
list(titanic.columns)

"""Indices"""
titanic.index

"""Seleccionar columna"""
nombres = titanic["Name"]
nombres2 =list(titanic.Name)

"""Seleccionar varias columnas y reordenar un dataframe"""
titanic=titanic[['Name',
 'Sex',
 'Age',
 'Siblings/Spouses Aboard',
 'Parents/Children Aboard',
 'Fare','Survived',
  'Pclass']]

nombre_sexo=titanic[["Name","Sex"]]

nombre_sexo_age_survived= titanic[["Name","Sex","Age","Survived"]]

"""Como re-asignar indices de un dataframe"""

cancer_mama.index = cancer_mama["id"] 
cancer_mama.drop("id",axis=1,inplace=True)

"""Filtrando las columnas de un dataframe"""

cols_cancer=list(cancer_mama.columns)
cols_cancer.remove("radius_mean")
cancer_mama=cancer_mama[cols_cancer]
"""Acceder a valores especificos en un dataframe"""

""" >>LOC<< Accede a los valores a través de los nombres
propios asignados a índices de filas y columnas
"""

cancer_mama.loc[842302]
cancer_mama.loc[842302,"diagnosis"]
cancer_mama.loc[[842302,842517],["diagnosis","texture_mean" ]]
cancer_mama.loc[[842302,842517]]

titanic.loc[:49,"Sex"]
titanic.loc[:49,["Sex","Age"]]
titanic.head(50)


""" >>ILOC<< Accede a los valores a través de las posiciones
propioas asignados a las filas y columnas
"""
datosCovid.iloc[0,0]
datosCovid.iloc[:20,:4]
datosCovid.iloc[-20:-1,-1]


"""Filtro de dataframe con operadores lógicos """

calidad_5 = vinoRojo["quality"]==5
SoloCalidad_5 = vinoRojo[calidad_5]


calidad_5_6 = (vinoRojo["quality"]==5) | (vinoRojo["quality"]==6)
SoloCalidad_5_6 = vinoRojo[calidad_5_6]

calidad_5_alcohol = (vinoRojo["quality"]==5) & (vinoRojo["alcohol"]>10)
SoloCalidad_5_alcohol = vinoRojo[calidad_5_alcohol]


"""
    ======================================================
    Medidas derivadas y funciones en DataFrames en Pandas
    ======================================================
"""

"""Medidas aritmeticas para columna/variable/atributo/descriptores"""
vinoRojo.mean() #Media para cada columna
vinoRojo.std() #Desviacion estandar
vinoRojo.median() #Mediana


"""Conteo de valores en una columna"""
vinoRojo["quality"].value_counts() #Conteo de los valores que tiene la columna
titanic["Survived"].value_counts()
cancer_mama["diagnosis"].value_counts()


"""Creando nuevas columnas derivadas"""
datosCovid["DeathRate"] = 1
datosCovid["DeathRate"] = datosCovid["TotalDeaths"] / datosCovid["TotalConfirmed"]
datosCovid.sort_values("DeathRate", ascending=False, inplace=True)


"""Aplicando funciones a la medida sobre series (columna)"""
titanic["SurvivedText"] = titanic["Survived"].map({0:"Murió",1:"Vivió"})

seriesUpper = lambda x: x.upper()
sexUpper = titanic["Sex"].map(seriesUpper)
nameUpper = titanic["Name"].str.upper()


"""Aplicando funciones a la medida sobre datagrames (varias columnas)"""

name_sex = titanic[["Name","Sex"]].applymap(seriesUpper)
 
def_lower = lambda x: x.lower() if type(x)==str else x
titanic_low = titanic.applymap(def_lower)

vinoRojoSum = vinoRojo.apply(np.sum, axis=1)
titanic_low2 = titanic.apply(def_lower)

"""
    ================================================
    Manejo de fechas en python con datetime y Pandas
    ================================================
"""

import datetime
import pandas as pd

"""Fechas con datetime"""

fecha=datetime.datetime.now()
type(fecha)
print(type(fecha))
print(fecha)

fecha.year
fecha.month
fecha.day
fecha.date()

str(fecha.date())

fecha.strftime("%x")
fecha.strftime("%X")         
fecha.strftime("%A") #Nombre del Dia
fecha.strftime("%d") #Numero del dia
fecha.strftime("%B") #Nombre del Mes 
fecha.strftime("%m") #Numero del Mes 
fecha.strftime("%Y") #Año completo
fecha.strftime("%y") #Año sin los primeros 2 digitos

#Tambien hay de hora,minuto,segundo (documentacion de datetime)
"""Fechas con pandas"""

pd.to_datetime("01/05/2022")
pd.to_datetime("01-05-2022")
pd.to_datetime("20220105")
pd.to_datetime("20220501", format="%Y%d%m")
pd.to_datetime("01/05/22")

energy = pd.read_csv("opsd_germany_daily.csv")


type(energy.iloc[0,0])
energy.index = energy["Date"]
type(energy.index[0])

energy.drop("Date", axis=1, inplace=True)

energy = energy.loc["2014":] #Toma los valores desde 2014 en adelante
energy = energy.loc["2014-06":] 
energy = energy.loc["2014-06":"2017-06"] 
energy.reset_index(inplace=True)
energy["Date"]>"2015"
energy = energy[energy["Date"]>"2015"]
energy["Date"] = pd.to_datetime(energy["Date"])
print(energy.iloc[0,0])
type(energy.iloc[0,0])
energy.plot(x="Date")

energy["Year"] = energy["Date"].dt.year
energy["DayOfWeek"] = energy["Date"].dt.strftime("%A")
energy["Month"] = energy["Date"].dt.strftime("%B")

energy = energy.drop(["Year","DayOfWeek","Month"], axis=1)

energy = energy.resample("M",on="Date").sum()
energy.plot()


"""
    ==================================
    Agrupaciones y pivoteos en pandas
    ==================================
"""

"""Carga y revision de datos"""
historicSales = pd.read_csv("OnlineRetail.csv", encoding="latin1")
historicSales.info()

historicSales.isna().sum() #Verifica cuantos valores son nulos por clumna
sample= historicSales.sample(5000) #Obiene "n" cantidad de datos aleatorios del dataframe


"""Cálculo de fecha mensual"""

historicSales["InvoiceDate"] = pd.to_datetime(historicSales["InvoiceDate"])
sample= historicSales.sample(5000)
year_month = lambda x: x[:7] #Lo que hace es tomar los primeros 7 digitos del str que va a recibir
historicSales["FechaMes"] = historicSales["InvoiceDate"].astype(str).map(year_month)


"""Cálculo del monto económico de ventas"""

historicSales["Ventas"] = historicSales["Quantity"] * historicSales["UnitPrice"] 


"""Cúal es el monto de ventas historico por mes  (Fecha mes, $ventas)"""

historic_ventas_mes = historicSales.groupby("FechaMes").agg({"Ventas":"sum"})   
historic_ventas_mes = historicSales.groupby("FechaMes", as_index=False).agg({"Ventas":"sum"})   


"""Cúal es el monto de ventas historico por mes y pais (Fecha mes, $ventas)"""

historic_ventas_pais_mes = historicSales.groupby(["FechaMes","Country"],as_index=False).agg({"Ventas":"sum"})


"""Cúal es el numero de órdenes historico por pais  (Fecha mes, pais, órdenes)"""

ordenes_historic_pais_mes = historicSales.groupby(["FechaMes","Country"],as_index=False).agg({"InvoiceNo":"nunique"})


"""historico de ventas de mandera amigable para quien no esta relacionado con formato tidy"""

ventas_producto = historicSales.pivot_table(index="StockCode", columns=["FechaMes"], values="Ventas", aggfunc="sum", fill_value=0)

"""Haga un pivote de las ventas mensuales por pais, para que casa pais sea una columna"""

ordenes_mensaules_pais_pivote = ordenes_historic_pais_mes.pivot_table(index="FechaMes",columns=["Country"], values="InvoiceNo", aggfunc="sum", fill_value=0)



"""
    ======================================================================
    Particionar archvos y leer partes en bloque usando pandas, numpy y glob2
    =======================================================================
"""

import pandas as pd
import numpy as np
import glob


path_base = r"C:\Users\luis_\OneDrive\Escritorio\wine_files"

archivoOriginal = pd.read_csv(path_base + "\winemag-data-130k-v2.csv")
partes = np.array_split(archivoOriginal,10)

for ix, df in enumerate(partes):
    df.to_excel(path_base+"\wine_div"+ str(ix+1).zfill(2) + ".xlsx", index=False)
    #zfill rellena con 0 los digitos que tu se lo ordenes
    #enumerate() es lo forma del for donde obtienes en una variable los indices de forma ascendente
    #to_excel() es la funcion para convertir un dataframe a excel
    
rutas = glob.glob(path_base + "\*.xlsx") 

partes_glob = [pd.read_excel(ruta) for ruta in rutas]

archivo_completo = pd.concat(partes_glob)

archivo_completo.to_excel(path_base+"\wine_complete_sin_index.xlsx", index=False)


"""
    ========================
    Melt o Unpivot en pandas
    ========================
"""

import pandas as pd

series_tiempo= pd.read_excel("venta_productos.xlsx")

valores = [col for col in series_tiempo.columns if col!="Producto"]

base_unpivot = pd.melt(series_tiempo, id_vars=["Producto"], value_vars=valores)

base_unpivot_2 = pd.melt(series_tiempo, id_vars=["Producto"], value_vars=valores, value_name="Piezas", var_name="AnioMes")


"""
    ========================
    Pandas y SQL
    ========================
"""

import pandas as pd
import sqlite3
import psycopg2


con_sqlite = sqlite3.connect("festivos_colombia.db")
festivos = pd.read_sql("SELECT * FROM holidays", con_sqlite)
festivos = pd.read_sql("SELECT * FROM holidays", con_sqlite, parse_dates= "date")

query = " SELECT date, localName, countryCode FROM holidays LIMIT 20"

festivos_20 = pd.read_sql(query, con_sqlite, parse_dates="date")


registro_sqlite = sqlite3.connect("registro.sql")
ibank = pd.read_sql("SELECT * FROM registro", registro_sqlite)


"""
    =============================
    Exportar dataframes en Pandas
    =============================
"""




"""
    ================================================
    Manejo de errores y excepciones (TRY AND EXCEPT)
    ================================================
"""


#Error de tipo
a=1+"r"

#Error de div entre 0
a = 1/0

#Error de sintaxis
a= 1/**´¨¡

#Error de variable no definida
a = 1/x

validador = True
while validador==True:
    x=input("Dame un numero divisor para 10: ")
    try:
        x = float(x)
        print(f'El numero es {5/x}')
        validador=False
    except:
        print(f'{x} no es numero valido')
    



validador = True
while validador==True:
    x=input("Dame un numero divisor para 10: ")
    try:
        x = float(x)
        print(f'El resultado de 10/x es: {10/x}')
        validador=False
    except ValueError:
        print(f'{x} no es un numero')
    except ZeroDivisionError:
        print(f'No se puede dividir entre {int(x)}')
    except:
        print(f'Error en numero, favor de revisar el dato ingresado')
    
import math
def suma(n1,n2):
    try:
        res= float(n1)+ float(n2)
        print(f'El resultado de la suma es {res}')
    except ValueError:
        print("El digito/digistos que ingresaste no son un numero")
    except:
        print("Ha ocurrido un error en la suma")

def resta(n1,n2):
    try:
        res= float(n1) - float(n2)
        print(f'El resultado de la resta es {res}')
    except ValueError:
        print("El digito/digistos que ingresaste no son un numero")
    except:
        print("Ha ocurrido un error en la resta")

def multiplicacion(n1,n2):
    try:
        res= float(n1) * float(n2)
        print(f'El resultado de la multiplicacion es {res}')
    except ValueError:
        print("El digito/digistos que ingresaste no son un numero")
    except:
        print("Ha ocurrido un error en la multiplicacion")
        
def division(n1,n2):
    try:
        res= float(n1) / float(n2)
        print(f'El resultado de la division es {res}')
    except ValueError:
        print("El digito/digistos que ingresaste no son un numero")
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except:
        print("Ha ocurrido un error en la division")

def potencia(n1,n2):
    try:
        res= math.pow(float(n1),float(n2)) 
        print(f'El resultado de la division es {res}')
    except ValueError:
        print("El digito/digistos que ingresaste no son un numero")
    except:
        print("Ha ocurrido un error en la division")


opc1= input("Bienvenido a la calculadora de luismi, quieres hacer algunas operaciones [y/n]?")
if opc1=="y" or opc1=="Y":
    validador = True
    while validador==True:
        print("""Elige la operacion que quieras hacer:
              [1] Sumar
              [2] Restar
              [3] Multiplicar
              [4] Dividir
              [5] Potencia
              [6] Salir
              """)
        opc2= input(">> ")
        if opc2=="1" or opc2==1:
            x=input("Dame el primer numero a sumar: ")
            y=input("Dame el segundo numero a sumar: ")
            suma(x,y)
            validador=True
        elif opc2 =="2" or opc2==2:
            x=input("Dame el primer numero a restar: ")
            y=input("Dame el segundo numero a restar: ")
            resta(x,y)
            validador=True
        elif opc2 =="3" or opc2==3:
            x=input("Dame el primer numero a multiplicar: ")
            y=input("Dame el segundo numero a multiplicar: ")
            multiplicacion(x,y)
            validador=True
        elif opc2 =="4" or opc2==4:
            x=input("Dame el primer numero a dividir: ")
            y=input("Dame el segundo numero a dividir: ")
            division(x,y)
            validador=True
        elif opc2 =="5" or opc2==4:
            x=input("Dame el numero que vas a elevar a potencia: ")
            y=input(f'Dame la potencia a la que va a elvear {x}:')
            potencia(x,y)
            validador=True
        elif opc2 =="6" or opc2==6:
            print("Gracias por usar la calculadora, que tenga buena tarde")
            validador=False
else:
    print("Esta bien, que tenga buena tarde")
