import logging

from app.app import app
import os.path

def init():
    # if not os.path.isdir(app.config['UPLOAD_FOLDER']):
    #     os.makedirs(app.config['UPLOAD_FOLDER'])
    #     app.logger.info("[init]:Create dirs \"{dir}\" for Uploading.".format(dir=app.config['UPLOAD_FOLDER']))
    pass

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=5123)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
