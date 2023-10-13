import os
from flask import Flask, send_from_directory, render_template, redirect
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

#port = int(os.environ.get("PORT", 5000))

def obtener_precio(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    fila = soup.find('tr', class_='detalle_banguat')
    if fila:
        celda = fila.find('td', align='center')
        if celda:
            valor = celda.text
            return valor
        else:
            return "No se encontró la celda con la alineación 'center'."
    else:
        return "No se encontró la fila con la clase 'detalle_banguat'."

@app.route('/precio', methods=['GET'])
def precio():
    url = 'https://www.banguat.gob.gt/tipo_cambio/'
    precio = obtener_precio(url)
    return jsonify({"precio": precio})

if __name__ == '__main__':
    app.run(debug=True)
