from flask import Flask, render_template, request, redirect, url_for
from flask import session as web_session
app = Flask(__name__)


#SQLAlchemy stuff
from database import Base, Contact
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
#APP CODE GOES HERE

@app.route('/')
def main_page():
	return render_template('main_page.html')

@app.route('/bio')
def bio_page():
	return render_template('bio_page.html')

@app.route('/hobbies')
def hobbies_page():
	return render_template('hobbies_page.html')

@app.route('/education')
def education_page():
	return render_template('education_page.html')

@app.route('/contact')
def contact_page():
    return render_template('contact_page.html')

@app.route('/sent', methods = ['POST'])
def sent_page():
    user_name = request.form['name']
    user_email = request.form['email']
    user_message = request.form['messege']    
    msg = Contact(name = user_name, email = user_email, messege = user_message)
    session.add(msg)
    session.commit()
    return render_template('sent_page.html')


if __name__ == "__main__":
    app.run(debug=True)