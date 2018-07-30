import sys
import os
import time
import xml.etree.ElementTree as ET
from connectMongoDB import connectionMongoDB
from xml.dom import minidom



# def parsePostXml(file):
#     tree = ET.parse(file)
#     root = tree.getroot()
#     for child in root:
#         savePosts(child.attrib)

def parsePostXml1(file):
    for event, element in ET.iterparse(file):
        if element.tag == 'row':
            savePosts(element.attrib)
        element.clear()

def savePosts(dictionary):
    coleccion.save(dictionary)

if __name__ == "__main__":
    os.system("cls")
    if len(sys.argv) < 3:
        print("Introduce el fichero xml y el nombre de la base de datos")
        print("-> Ejemplo: python .\parserXml.py [fichero.xml] [nombre]")
    else:
        coleccion = connectionMongoDB(sys.argv[2])
        start_time = time.time()
        parsePostXml1(sys.argv[1])
        elapsed_time = time.time() - start_time
        print("---->Tiempo ejecución:", elapsed_time)