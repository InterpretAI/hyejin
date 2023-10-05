from flask import Blueprint, url_for
from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_iai():
    return 'Hello, Interpret AI!'




@bp.route('/')
def index():
    return redirect(url_for('prompt._list'))