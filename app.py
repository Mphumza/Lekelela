from flask import *
from flask_sqlalchemy import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_data.db'
app.config['SECRET_KEY']='Lekelela'

db = SQLAlchemy(app)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def _repr_(self):
        return f'<Submission {self.id}>'


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # Handle form submission here
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create a new Contact object
        contact = Submission(name=name, email=email, phone=phone, message=message)

        # Add the Contact object to the database session
        db.session.add(contact)

        # Commit the changes to the database
        db.session.commit()

    # Return a response to the client (you can customize this as needed)
    return render_template("index.html")
    

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')



with app.app_context():
    db.create_all()
    #mssql+pyodbc://mphumza:M10061960_%40s@10.0.0.4/lekelela.db?driver=ODBC+Driver+17+for+SQL+Server'


if __name__ == '_main_':
    app.run(debug=True)