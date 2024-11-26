from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    value = db.Column(db.Float)

@app.route('/')
def index():
    data = Data.query.all()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add_data():
    name = request.form['name']
    value = float(request.form['value'])
    new_data = Data(name=name, value=value)
    db.session.add(new_data)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)