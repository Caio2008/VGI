# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 14:03:59 2020

@author: caio
"""

from datetime import  datetime
import xml.etree.ElementTree as ET
import requests
import re
#### data formato ano,mes dia###############
data_limite= datetime(2020,7,23,0,0,0)


def le_entrada():
    ##############Local do arquivo de entrada##############
    entra= open('input file path')
    entrada=entra.readlines()
    saida=[]
    for i in entrada:
        saida.append(re.sub('[^0-9]', '', i))
    entra.close()
    return(saida)

def coleta(idd):
    try:
        url = "https://www.openstreetmap.org/api/0.6/way/"+str(idd)+"/history"
        header = { 'Accept': 'application/xml' }
        r = requests.get(url, headers=header)
    except :
        print("ERRO ID: "+str(idd), "NÃO LOCALIZADO")
 
    tree =  ET.ElementTree(ET.fromstring(r.content))

    root = tree.getroot()
    retorno=''
    user={}
    version=[]
    for i in root:
        data=datetime.strptime(i.get('timestamp'), "%Y-%m-%dT%H:%M:%SZ")
         # < se quiser data maxima, > se quiser data minima
        if(data <= data_limite):
            user[str(i.get('user'))]=1
            version.append(int(i.get('version')))
            len(user)
    retorno=str(idd)+'\t'+str(max(version))+'\t'+str(len(user))+'\n'
    print(str(idd),str(max(version)),len(user))
    return retorno

def main():
    entrada=le_entrada()
    txt='id\tversion\tuser\n'
    
    for i in entrada:
        txt+=coleta(i)
    saida=open('output file path','w')
    saida.write(txt)
    saida.close()
    
main()    

    
