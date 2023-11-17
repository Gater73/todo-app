from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

@app.route('/')
def index():
    incomplete = Task.query.filter_by(complete=False).all()
    complete = Task.query.filter_by(complete=True).all()
    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    task = Task(text=request.form['todoitem'], complete=False)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    task = Task.query.get_or_404(id)
    if task is not None:
        task.complete = True
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_completed():
    Task.query.filter_by(complete=True).delete()
    db.session.commit()
    return redirect(url_for('index'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)