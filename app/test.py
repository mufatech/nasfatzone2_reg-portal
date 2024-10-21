from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mufatech@localhost/nasfat'
db = SQLAlchemy(app)

@app.route('/test-database')
def test_database_connection():
    try:
        # Perform a simple query to retrieve data from a table (e.g., User)
        result = db.session.query(User).first()
        return f"Database Connection Successful! Retrieved: {result}"
    except Exception as e:
        return f"Database Connection Failed: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

