from flask import Flask
from flask_script import Manager
from web.model import db
from web.view import blue

app = Flask(__name__)
app.register_blueprint(blueprint=blue)

#配置数据库连接信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ww19940820@127.0.0.1:3306/flask1'
db.init_app(app)

manage = Manager(app)

if __name__ == "__main__":
    manage.run()
