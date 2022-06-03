from flask import Blueprint, render_template

bp = Blueprint('wkbl', __name__, url_prefix='/wkbl')
#team
@bp.route('/home/')
def home():
    return render_template('wkbl/home.html')