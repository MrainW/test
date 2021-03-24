from app.models import db
from app.views import app

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)#项目启动，默认5000端口，可以自己修改
