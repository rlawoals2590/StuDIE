from flask import Blueprint, request, session, redirect, url_for, render_template
from ..user.func.auth import user_validation

room_route = Blueprint("room_route", __name__, url_prefix='/room')


@room_route.route('/', methods=['GET','POST'])
@user_validation()
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['room'] = request.form['room']
        return redirect(url_for('room_route.chat'))
    return render_template('index.html')


@room_route.route('/stream/')
@user_validation()
def stream():
    return render_template('cam.html')