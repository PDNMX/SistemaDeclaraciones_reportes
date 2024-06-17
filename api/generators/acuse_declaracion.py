import requests
import json

from datetime import datetime
from typing import Any
from typing import Dict
from typing import List
from jinja2 import Environment
from jinja2 import FileSystemLoader
from urllib.parse import urlparse
from weasyprint import CSS
from weasyprint import HTML

from api.generators.custom_filters import boolToSiNo
from api.generators.custom_filters import countryFormat
from api.generators.custom_filters import format_datetime
from api.generators.custom_filters import replacePipe
from api.generators.custom_filters import nationalityFormatPipe
from api.generators.custom_filters import dataEmptyPipe
from api.generators.custom_filters import dateTranslationPipe
# from api.generators.custom_filters import replaceInstitutionPipe


class AcuseDeclaracionGenerator(object):
    def __init__(self, owner: str, institucionData:Dict[str, Any], id: str, data: Dict[str, Any], preliminar: bool = False, publico: bool = False):        
        # print(json.dumps(institucionData,indent=2))
        self.owner:str = owner
        self.institucionData: Dict[str,Any] = institucionData
        self.id: str = id    
        self.data: Dict[str, Any] = data
        self.preliminar = preliminar
        self.publico = publico

    def addJson(self):        
        self.data.update(self.institucionData)
        

    def make_pdf(self):
        env: Environment = Environment(loader=FileSystemLoader('.'))
        env.filters['toSiNo'] = boolToSiNo
        env.filters['formatdatetime'] = format_datetime
        env.filters['countryFormat'] = countryFormat
        env.filters['replace'] = replacePipe
        env.filters['nationalityFormat'] = nationalityFormatPipe
        env.filters['dataEmpty'] = dataEmptyPipe
        env.filters['dateTranslation'] = dateTranslationPipe
        # env.filters['replaceInstitution'] = replaceInstitutionPipe
        templateName = 'templates/acuse_declaracion.html'
        if self.publico:
            templateName = 'templates/publico/acuse_declaracion.html'
        template = env.get_template(templateName)
        self.addJson()
        body_html: str = template.render(self.data)
        # pdf_filename: str = f'reports/acuse-{self.id}.pdf'
        stylesheets: List[CSS] = [CSS(filename='styles/acuse_declaracion.css')]
        if self.preliminar:
            stylesheets.append(CSS(filename='styles/preliminar.css'))
        if self.publico:
            stylesheets.append(CSS(filename='styles/publico.css'))

        return HTML(string=body_html, encoding='utf8').write_pdf(stylesheets=stylesheets)
