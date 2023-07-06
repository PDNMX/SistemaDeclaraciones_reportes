import assets.catalogos
import datetime
import json
from datetime import datetime, timedelta

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
    if(value):
        return (datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').astimezone() - timedelta(hours=5, minutes=0)).strftime(format)
    return ''

def restar_ano_modificacion(value):
    if(value):
        return (datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ').astimezone() - timedelta(hours=5, minutes=0, days=365)).strftime("%Y")
    return ''

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
