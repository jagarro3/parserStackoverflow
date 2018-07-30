import os
import sys
import time
import xml.etree.ElementTree as ET
from xml.dom import minidom
from connectMongoDB import connectionMongoDB

def parserXml(file):
    for event, element in ET.iterparse(file):
        if element.tag == 'row':
            savePosts(element.attrib)
        element.clear()

def savePosts(dictionary):
    coleccion.save(dictionary)

if __name__ == "__main__":
    os.system("cls")
    if len(sys.argv) < 3:
        print("Introduce el fichero xml y el nombre de la colección MongoDB")
        print("-> Ejemplo: python .\parser.py fichero.xml nombreColeccion")
    else:
        coleccion = connectionMongoDB(sys.argv[2])
        start_time = time.time()
        parserXml(sys.argv[1])
        elapsed_time = time.time() - start_time
        print("---->Tiempo ejecución:", elapsed_time)
