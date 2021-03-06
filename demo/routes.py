from crypt import methods
from flask import render_template, request, flash, redirect, url_for

from demo import app         
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
import pymysql

class SubmitForm(FlaskForm):
    name    = StringField('Name', validators=[DataRequired()])
    age     = IntegerField('Age', validators=[DataRequired(),NumberRange(min=0,max=200)])
    submit  = SubmitField('Submit')

def pymysqlsafeconn():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='jimmy',
        password='741111.As',
        db='klarrio'
    )
    return conn

@app.route('/', methods=["POST", "GET"])
def index():
    form = SubmitForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            conn = pymysqlsafeconn()
            cur = conn.cursor()

            sql = "INSERT INTO `peopleAge` (`name`, `age`) VALUES (%s, %s)"
            val = (form.name.data,form.age.data)
            cur.execute(sql,val)
            conn.commit()
            flash('name: {}, age: {} has been submitted successfully'.format(form.name.data, form.age.data), 'success')

            conn.close()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

    else:
        conn = pymysqlsafeconn()
        cur = conn.cursor()
        sql = "select * from peopleAge"
        cur.execute(sql)
        content = cur.fetchall()

        labels = ["ID", "Name", "Age"]

        conn.commit()
        conn.close()
        return render_template('index.html', labels=labels, content=content, html_form=form)
