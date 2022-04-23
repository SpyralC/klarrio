from crypt import methods
from flask import render_template, request, flash, redirect, url_for

from demo import app         
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='jimmy',
    password='741111.As',
    db='klarrio'
)

class SubmitForm(FlaskForm):
    name    = StringField('Name', validators=[DataRequired()])
    age     = IntegerField('Age', validators=[DataRequired()])
    submit  = SubmitField('Submit')

@app.route('/', methods=["POST", "GET"])
def index():
    form = SubmitForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            cur = conn.cursor()

            sql = "INSERT INTO `peopleAge` (`name`, `age`) VALUES (%s, %s)"
            val = (form.name.data,form.age.data)
            cur.execute(sql,val)
            conn.commit()
            flash('name: {}, age: {} has been submitted successfully'.format(form.name.data, form.age.data), 'success')

            sql = "select * from peopleAge"
            cur.execute(sql)
            content = cur.fetchall()

            sql = "SHOW FIELDS FROM peopleAge"
            cur.execute(sql)
            labels = cur.fetchall()
            labels = [l[0] for l in labels]

            return redirect(url_for('index'))
        else:
            name = form.name.data
            name_t = type(name)
            age = form.age.data
            age_t = type(age)

            return "submit failed, name is {}, type is {}; age is {}, type is {}.".format(name,name_t,age,age_t)

    else:
        cur = conn.cursor()
        sql = "select * from peopleAge"
        cur.execute(sql)
        content = cur.fetchall()

        sql = "SHOW FIELDS FROM peopleAge"
        cur.execute(sql)
        labels = cur.fetchall()
        labels = [l[0] for l in labels]

        conn.commit()
        return render_template('index.html', labels=labels, content=content, html_form=form)
