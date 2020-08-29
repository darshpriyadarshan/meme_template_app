import os
from forms import  AddForm, FindForm
from flask import Flask, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Template(db.Model):

    __tablename__ = 'templates'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    actor = db.Column(db.Text)
    movie = db.Column(db.Text)
    link = db.Column(db.Text)

    def __init__(self,name,actor,movie,link):
        self.name = name
        self.actor = actor
        self.movie = movie
        self.link = link
    def __repr__(self):
        return "Template name: {}".format(self.name)

############################################

        # Fetching list of actors and movies

##########################################
actors = Template.query.with_entities(Template.actor).all()
actors_set = set()
actors_list = []
#print("Actors from db are: {}".format(actors))
for actor in actors:
    #removing quotes and comma
    actor = str(actor)[2:-3]
    actors_set.add(actor)
    actors_list = list(actors_set)
    actors_list.sort()

#print("Actors: {}".format(actors_list))

movies = Template.query.with_entities(Template.movie).all()
movies_set = set()
movies_list = []
for movie in movies:
    movie = str(movie)[2:-3]
    movies_set.add(movie)
    movies_list = list(movies_set)
    movies_list.sort()

#print(movies_list)
############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():

    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_template():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        actor = form.actor.data
        movie = form.movie.data
        link = form.link.data
        # Add new Template to database
        new_temp = Template(name,actor,movie,link)
        db.session.add(new_temp)
        db.session.commit()

        return redirect(url_for('list_all_templates'))

    return render_template('add.html',form=form)

@app.route('/list')
def list_all_templates():
    # Grab a list of templates from database.
    templates = Template.query.all()
    return render_template('list.html', templates = templates)

@app.route('/find', methods=['GET', 'POST'])
def find_template():

    form = FindForm()
    
    if form.validate_on_submit():
        session['actor'] = form.actor.data
        session['movie'] = form.movie.data
        # pup = Template.query.get(id)
        # db.session.delete(pup)
        # db.session.commit()

        return redirect(url_for('result_template'))
    return render_template('find.html',form=form,actors_list=actors_list,movies_list=movies_list)


@app.route('/result', methods=['GET', 'POST'])
def result_template():

    actor = session['actor']
    movie = session['movie']

    if movie == '':
        result = Template.query.filter_by(actor=actor).all()
    elif actor == '':
        result = Template.query.filter_by(movie=movie).all()
    else:
        result1 = Template.query.filter_by(actor=actor).all()
        result2 = Template.query.filter_by(movie=movie).all()
        result = [res for res in result1 if res in result2]
    return render_template('result.html',result=result)


@app.route('/find/actor/<actor>', methods=['GET', 'POST'])
def find_template_actor(actor):

    form = FindForm()

    session['actor'] = actor
    form.actor.data = actor

    if form.validate_on_submit():
        session['actor'] = form.actor.data
        session['movie'] = form.movie.data
        # pup = Template.query.get(id)
        # db.session.delete(pup)
        # db.session.commit()

        return redirect(url_for('result_template'))
    return render_template('find.html', form=form)


@app.route('/find/movie/<movie>', methods=['GET', 'POST'])
def find_template_movie(movie):

    form = FindForm()

    session['movie'] = movie
    form.movie.data = movie

    if form.validate_on_submit():
        session['actor'] = form.actor.data
        session['movie'] = form.movie.data
        # pup = Template.query.get(id)
        # db.session.delete(pup)
        # db.session.commit()

        return redirect(url_for('result_template'))
    return render_template('find.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
