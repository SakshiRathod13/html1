from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# db=SQLAlchemy()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@server/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Rathod@@13server/Tourism'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
# db.init_app(app)
db=SQLAlchemy(app)




# class Tourism(db.Model):
#     sno=db.Column(db.Integer,primary_key=True)
#     tittle=db.Column(db.String(200),nullable=False)
#     desc=db.Column(db.String(500),nullable=False)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)
    
#     def __repr__(self) -> str:
#         return f"{self.sno}-{self.tittle}"

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, unique=True, nullable=False)
#     email = db.Column(db.String)

# with app.app_context():
#     db.create_all()
 

# db = SQLAlchemy()
# class students(db.Model):
#    id = db.Column('student_id', db.Integer, primary_key = True)
#    name = db.Column(db.String(100))
#    city = db.Column(db.String(50))  
#    addr = db.Column(db.String(200))
#    pin = db.Column(db.String(10))

# def __init__(self, name, city, addr,pin):
#    self.name = name
#    self.city = city
#    self.addr = addr
#    self.pin = pin



@app.route('/')   
def hello_world():
    todo=todo(title="first todo",desc="yfdwyeftwruefeiu")
    db.session.add(todo)
    db.session.commit()
    return render_template("index.html")
    return 'Hello, World!'

@app.route('/sakshi')
def sakshi():
    allTodo=sakshi.query.all()
    return "this is sakshi's page"
if __name__=="__main__" :
    app.run(debug=True)