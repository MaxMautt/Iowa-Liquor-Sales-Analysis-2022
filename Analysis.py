import pandas as pd
import requests
import duckdb
from io import StringIO

#Utilizando el URL del API se extraen los datos de la web directamente con las columnas necesitadas para el analisis

response = requests.get("https://data.iowa.gov/resource/m3tr-qhgy.csv", 
    params={
    "$limit": 2500000, 
    "$where": "date >= '2022-01-01' AND date <= '2022-12-31'",
    "$select": "date,name,city,category_name,state_bottle_cost,state_bottle_retail,sale_dollars,sale_liters,vendor_name"})

df = pd.read_csv(StringIO(response.text))

#Verificamos los datos con Data Wangler para confirmar que no haya duplicados, null values o algún otro error que corregir

#ANALISIS 1 - LOCAL CON MAYOR VENTA EN DOLARES Y LITROS DE ALCOGOL
m1= """
    SELECT d.name, SUM(d.sale_dollars) AS total_sales, SUM(sale_liters)
from df AS d
group by 1
order by 2 DESC 

"""

#ANALISIS 2 - TIPO DE ALCOHOL MAS VENDIDO
m2="""
    SELECT d.category_name, SUM(d.sale_dollars) AS total_sales
    FROM df AS d
    GROUP BY 1
    ORDER BY 2 DESC

"""

#ANALISIS 3 - VENDOR CON MAS VENTAS
m3="""
    SELECT d.vendor_name, SUM(d.sale_dollars) AS total_sales
    FROM df AS d
    GROUP BY 1
    ORDER BY 2 DESC

"""

#ANALISIS 4 - MES CON MAYOR VENTAS
m4="""
    SELECT EXTRACT(MONTH FROM CAST(d.date AS date)) AS month, SUM(d.sale_dollars) AS total_sales
    FROM df AS d
    GROUP BY 1
    ORDER BY 2 DESC

"""

#ANALISIS 5 - MARGEN DE GANANCIA SEGUN LA CATEGORIA DE ALCOHOL
m5="""
    SELECT d.category_name, AVG((d.state_bottle_retail-d.state_bottle_cost)) AS average_margin
    FROM df AS d
    GROUP BY 1
    ORDER BY 2 DESC

"""

#ANALISIS 6 - CIUDAD CON MAYOR VENTAS DE VOLUMEN DE ALCOHOL 
m6="""
    SELECT d.city, SUM(d.sale_liters) AS total_liters
    FROM df AS d
    GROUP BY 1
    ORDER BY 2 DESC
"""

#Con ayuda de Duckdb de leen los queries en SQL y se les asigna a cada resultado
result1 = duckdb.query(m1).df()
result2 = duckdb.query(m2).df()
result3 = duckdb.query(m3).df()
result4 = duckdb.query(m4).df()
result5 = duckdb.query(m5).df()
result6 = duckdb.query(m6).df()

result1.to_csv('data/top_stores.csv', index=False)
result2.to_csv('data/top_categories.csv', index=False)
result3.to_csv('data/top_vendors.csv', index=False)
result4.to_csv('data/sales_by_month.csv', index=False)
result5.to_csv('data/margin_by_category.csv', index=False)
result6.to_csv('data/city_and_volume.csv', index=False)