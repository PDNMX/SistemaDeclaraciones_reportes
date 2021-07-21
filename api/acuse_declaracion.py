import logging

from decouple import config
from typing import Any
from typing import Dict
from flask import request
from flask import make_response
from flask_restful.reqparse import RequestParser
from flask_restful import Resource

from api.generators.acuse_declaracion import AcuseDeclaracionGenerator


class AcuseDeclaracion(Resource):
    def __init__(self):
        self.parser: RequestParser = RequestParser(bundle_errors=True)
        self.parser.add_argument('id', type=str, required=True, help='id is required')
        self.parser.add_argument('declaracion', type=dict, required=True, help='declaracion is required')
        self.parser.add_argument('preliminar', type=bool, required=False)
        self.parser.add_argument('publico', type=bool, required=False, default=False)

    def post(self):
        API_KEY: str = config('API_KEY', default='')
        if request.headers['X-Api-Key'] != API_KEY:
            logging.error('Unauthorized Intent with API_KEY: {}'.format(request.headers['X-Api-Key']))
            return { 'success': False, 'message': 'BAD REQUEST' }, 400

        try:
            raw_data: Dict[str, Any] = self.parser.parse_args()
            report: AcuseDeclaracionGenerator = AcuseDeclaracionGenerator(
                id=raw_data['id'],
                data=raw_data['declaracion'],
                preliminar=raw_data['preliminar'],
                publico=raw_data['publico'],
            )

            pdf_filename = report.make_pdf()
            response = make_response(pdf_filename)
            response.headers.set('Content-Type', 'application/pdf')
            return response#send_file(pdf_filename, attachment_filename=pdf_filename)
        except Exception as e:
            logging.exception(e)
            return { 'sucess': False, 'message': 'BAD REQUEST' }, 400
