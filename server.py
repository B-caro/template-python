import os
from flask import Flask, send_from_directory, render_template, redirect
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.banguat.gob.gt/tipo_cambio/')
soup = BeautifulSoup(r.text, 'html.parser')

fila = soup.find('tr', class_='detalle_banguat')
if fila:
    celda = fila.find('td', align='center')
    if celda:
        valor = celda.text
        print("Valor en la celda:", valor)
    else:
        print("No se encontró la celda con la alineación 'center'.")
else:
    print("No se encontró la fila con la clase 'detalle_banguat'.")
