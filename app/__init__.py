import os 
from flask import Flask
from custom.converter import RegexConverter
from ext import db

config_mode = {
    'development': "dev.py",
    'product': "prod.py",
    'testing': "test.py",
    'default': "dev.py",
}

def create_app(config_mode_name:str):
    """ 工厂函数，用于延迟创建 Flask 实例，可用于创建多个实例.

    :param config_name: 配置名称，可根据开发环境、测试环境、生产环境区分
    :return: Flask 示例
    """

    app = Flask(__name__)
    config_file_abspath = "config/settings"+ config_mode[config_mode_name]
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),config_file_abspath)
    if not os.path.exists(config_file_path):
        raise Exception(f"{config_file_path} 不存在. 请添加该配置文件或是更换配置")
    app.config.from_pyfile(config_file_path)
    app.url_map.converters['regex']=RegexConverter
    db.init_app(app)
    # Scanner(app).run()
    return app
