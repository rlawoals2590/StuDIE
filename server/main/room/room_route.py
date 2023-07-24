from flask import Blueprint, request, session, redirect, url_for, render_template
from markupsafe import escape

room_route = Blueprint("room_route", __name__, url_prefix='/room')


@room_route.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['room'] = request.form['room']
        return redirect(url_for('room_route.chat'))
    return render_template('index.html')


@room_route.route('/chat/')
def chat():
    name = escape(session['name'])
    room = escape(session['room'])
    # if name == '' or room == '':
    #     return redirect(url_for('room_route.index'))
    return render_template('chat.html', name=name, room=room)


@room_route.route('/stream/')
def stream():
    return render_template('cam.html')

