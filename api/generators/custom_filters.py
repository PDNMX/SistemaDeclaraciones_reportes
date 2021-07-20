import assets.catalogos
import datetime
import json
from pytz import timezone

def boolToSiNo(value):
    if (value):
        return 'si'
    return 'no'

def countryFormat(value):
    if (value):
        with open('assets/catalogos/paises.json') as file:
            data = json.load(file)
            for item in data:
                if item['clave']==value:
                    return item['valor']
    return ''

def dataEmptyPipe(value):
    if (value):
        return value
    return ''

def dateTranslationPipe(value):
    if (value):
         with open('assets/catalogos/meses.json') as file:
            data = json.load(file)
            for item in data:
                if value.upper().find(item['english']) != -1:
                    return value.upper().replace(item['english'], item['spanish'])
    return ''

def format_datetime(value, format="%d/%m/%Y"):
    if value is None:
        return ""
    new_date =  datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%fZ")
    return new_date.astimezone(  timezone('America/Mexico_City')  ).strftime(format)
    # return datetime.datetime.strptime(value[:10], "%Y-%m-%d").strftime(format)

def nationalityFormatPipe(value):
    if (value):
        with open('assets/catalogos/nacionalidades.json') as file:
            data = json.load(file)
            for item in data:
                if item['clave']==value:
                    return item['valor']
    return ''
    
def replacePipe(value: str, strToReplace: str, replacementStr: str): 
    if (not value or not strToReplace or not replacementStr):
      return value
    return value.replace(strToReplace, replacementStr)   

def replaceInstitutionPipe(value: str, institutionKey: str, type: str):
    if (value and institutionKey and type):
        with open('assets/json/institutuciones.json') as file:
            data = json.load(file)
            for item in data:
                if item['clave'] == institutionKey:
                    if type == 'ente_publico':
                        return item['ente_publico']
                    elif type == 'nombre':
                        return item['servidor_publico_recibe']['nombre']
                    elif type == 'cargo':
                        return item['servidor_publico_recibe']['cargo']
            return value 
    return value