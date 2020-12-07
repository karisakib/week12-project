from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from scraper import scrape

data = scrape()
app = Flask(__name__)
app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # rank = db.Column(db.Integer, nullable=False)
    # company = db.Column(db.String(255), nullable=False)
    # country = db.Column(db.String(255), nullable=False)
    # percentage = db.Column(db.String(255), nullable=False)
    row = db.Column(db.String(255), nullable=False)
    
    def __init__(self):
        self.id = id
        self.row = row

    def __repr__(self):
        # return f"<Data {self.id} {self.rank} {self.company} {self.percentage}>"
        return f"<Data {self.id} {self.row}>" 

    def add_to_db():


@app.route('/')
def home():
    dat = Database.query.all()
    return render_template('index.html', rows = dat)

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)
