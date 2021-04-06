import assets.catalogos
import datetime
import json

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
    return datetime.datetime.strptime(value[:10], "%Y-%m-%d").strftime(format)

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