import sys
import os

# Agrega la carpeta padre de 'logic' y 'main' al path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.file import DataReader
from logic.parser_html import ParserHtml
from logic.article import Article

#
#
#       SUBPROGRAMAS
#
#

def inicializar_articulos():
    mapper = lambda titulo, autor, texto: Article(titulo, autor, texto)
    argumentos_mapper = ['titulo', 'autor', 'texto']
    ruta_archivo = 'data/datos.csv'

    for article in DataReader.read_data(ruta_archivo, argumentos_mapper, mapper):
        if article.autor_how_id() in generador.articles:
            generador.articles[article.autor_how_id()].append(article)
        else: 
            generador.articles[article.autor_how_id()] = [article]

def crear_index(generador):
    try:
        with open('./build/index.html', 'w', encoding='utf-8') as html:
            html.write(generador.to_html())
        print("index.html generado exitosamente.")
    except IOError:
        print("Error: al escribir en el archivo index.html")

def crear_articulos(generador: ParserHtml):
    ruta_base = './build/articulos/'
    nombre_pagina = ''
    try:
        for autor, articles in generador.articles.items():
            cantidad_articulos = len(articles)
            for index, article in enumerate(articles):
                nombre_pagina = f'{ruta_base}{autor}-{index}.html'
                with open(nombre_pagina,'w', encoding='utf-8') as pagina:
                    prev = None
                    next = None
                    if index>0:
                        prev = f'{autor}-{index-1}.html'
                    if index<cantidad_articulos-1:
                        next = f'{autor}-{index+1}.html'
                    pagina.write(article.to_html(prev, next))
    except FileNotFoundError:
        print(f"La ruta {ruta_base} no existe")
    except IOError:
        print(f"Error al escribir en el archivo {nombre_pagina}")



#
#
#       PROGRAMA PRINCIPAL
#
#

generador = ParserHtml("La historia de Italia")

inicializar_articulos()
crear_index(generador)
crear_articulos(generador)