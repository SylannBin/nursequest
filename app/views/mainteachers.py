from pprint import pprint

from flask import render_template, request, redirect, url_for
from sqlalchemy import or_
from sqlalchemy.exc import IntegrityError
import datetime

from app import app, db
from app.models.speakers import Speaker

@app.route('/mainteacher/dashboard/<int:id>')
def get_mainteacher_dashboard(id):
    print('cc je passe par mainteacher')
    mainteacher = Speaker.query.get(id)
    print(mainteacher)

    return render_template('mainteachers/main-teacher-dashboard.html',
                           data={'mainteacher': mainteacher})

@app.route('/mainteachers')
def get_mainteachers():
    q = Patient.query
    page = request.args.get('page', default=1, type=int)
    searched = request.args.get('search', default='')
    if searched:
        q = q.filter(or_(
            Patient.first_name.ilike('%' + searched + '%'),
            Patient.last_name.ilike('%' + searched + '%'),
            Patient.email.ilike('%' + searched + '%'),
            Patient.social_number.ilike('%' + searched + '%')
        ))
    patients = q.paginate(page, 10, False)
    return render_template(
        'patients.html',
        current_route='get_patients',
        title='List of admitted patients',
        subtitle='',
        data=patients,
        searched=searched
    )