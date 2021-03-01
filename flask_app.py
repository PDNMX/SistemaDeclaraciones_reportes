import logging
from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from api.acuse_declaracion import AcuseDeclaracion


class App:
    def __init__(self):
        self.port: int = config('PORT', default=3001, cast=int)
        self.app: Flask = Flask(__name__)
        self.api: Api = Api(self.app)
        self._setup()

    def _setup(self):
        CORS(self.app)
        self.api.add_resource(AcuseDeclaracion, '/acuse-declaracion')

    def run(self):
        self.app.run(port=self.port, debug=True, host='0.0.0.0')

if __name__ == '__main__':
    logging.info('Initializing Reports API')
    App().run()
