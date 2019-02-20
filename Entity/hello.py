#from conect import * #connect to database

#$export FLASK_APP=hello.py
#$export FLASK_DEBUG=1
#$flask run

#user_agent=request.headers.get('User-Agent')

from flask import Flask
from flask import render_template #render index
from flask import request
from flask import session, redirect, url_for, flash

##manejo de vistas
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY'] = 'hard to guess string'#si se desea encriptar la info


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
        return render_template('404.html'),400 

@app.errorhandler(500)
def internal_server_error(e):
        return render_template('500.html'),500

#creacion de un formulario 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit') 

