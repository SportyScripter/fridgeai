# TU WPISUJE SCIEZKE ABY POD DANYM ADRESEM WYSWIETLIC ZAPYTANIA Z PLIKU main.py
import requests
print(requests.get('http://127.0.0.1:8000/products').json())
print(requests.get('http://127.0.0.1:8000/products?name=Milk').json())
