import logging

from app.app import app


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True, port=5123)
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
