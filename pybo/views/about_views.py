from flask import Blueprint, render_template

bp = Blueprint('about', __name__, url_prefix='/about')
#About
@bp.route('/intro/')
def intro():
    return render_template('about/intro.html')

@bp.route('/gamerule/')
def gamerule():
    return render_template('about/gamerule.html')