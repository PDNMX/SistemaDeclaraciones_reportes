import assets.catalogos
import datetime
import json

def boolToSiNo(value):
    if (value):
        return 'si'
    return 'no'

def format_datetime(value, format="%d/%m/%Y"):
    if value is None:
        return ""
    return datetime.datetime.strptime(value[:10], "%Y-%m-%d").strftime(format)

def countryFormat(value):
    if (value):
        with open('assets/catalogos/paises.json') as file:
            data = json.load(file)
            for item in data:
                if item['clave']==value:
                    return item['valor']
    return ''
