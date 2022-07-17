from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(275), nullable=False)
    password = db.Column(db.String(175), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.email}"

@app.route('/', methods=['GET', 'POST'])
def mainLogic():
    if request.method== "POST":
        userTitle= request.form['title']
        userTodo = request.form['desc']
        todo = Todo(email=userTitle, password=userTodo)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)
if __name__ == "__main__":
    app.run(debug=True)