from flask import render_template, Blueprint

index_route = Blueprint('index_route', __name__, url_prefix='/')


@index_route.route('/')
# @user_validation()
def index():
    print('test')
    return render_template('index.html')
