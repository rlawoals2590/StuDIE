from flask import render_template, Blueprint

index_route = Blueprint('index_route', __name__, url_prefix='/')


@index_route.route('/')
# @user_validation()
def index():
    return render_template('index.html')


@index_route.route('/studyTimer')
# @user_validation()
def studyTimer():
    return render_template('studyTimer.html')
