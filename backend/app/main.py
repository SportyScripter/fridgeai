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
def get_List_Of_Products():
   cursor.execute('''SELECT * from Products''')
   result = cursor.fetchall()
   List_of_Products = []
   for row in result:
      List_of_Products.append(Product.Product(name=row[0], quantity=row[1], weight=row[2]))
   return List_of_Products

@app.get("/pure_list")
def get_List():
   cursor.execute('''SELECT * from Products''')
   result = cursor.fetchall()
   return result
