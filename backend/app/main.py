import psycopg2
from fastapi import FastAPI
import Product

app = FastAPI()

#establishing the connection
conn = psycopg2.connect(
   database="fridgeai_db", user='fridgeai_user', password='fridgeai_password', host='localhost', port= '5432'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
@app.get("/products")
def Get_List_Of_Products():
   cursor.execute('''SELECT * from Products''')
   result = cursor.fetchall()
   List_of_Products = []
   for row in result:
      List_of_Products.append(Product.Product(id=row[0], name=row[1], quantity=row[2], categories=row[3]))
   return List_of_Products
