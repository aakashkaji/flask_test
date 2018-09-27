from flask import Flask
from core.controller.routes import sheet_blueprint
apps = Flask(__name__, instance_relative_config=True)
apps.register_blueprint(sheet_blueprint)


if __name__ == '__main__':

    apps.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
