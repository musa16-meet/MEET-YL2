from flask import Flask, render_template, request, redirect, url_for
from flask import session as web_session
app = Flask(__name__)

#SQLAlchemy stuff
from database_setup import Base, User, Interests #<--- Import your tables here!!
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///Webpage.db')
Base.metadata.create_all(engine) 
DBSession = sessionmaker(bind=engine)
session = DBSession()
#APP CODE GOES HERE

@app.rout('/')
def main_page():
	return render_template('main_page.html')

@app.rout('/bio')
def thename():
	return render_template('bio_page.html')

@app.rout('/hobbies')
def thename():
	return render_template('hobbies_page.html')

@app.rout('/education')
def thename():
	return render_template('education_page.html')

@app.rout('/contact')
def thename():
	return render_template('contact_page.html')
