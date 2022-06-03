from flask import Blueprint, render_template

bp = Blueprint('team', __name__, url_prefix='/team')
#team
@bp.route('/woori/')
def woori():
    return render_template('team/woori.html')

@bp.route('/samsung/')
def samsung():
    return render_template('team/samsung.html')

@bp.route('/hana/')
def hana():
    return render_template('team/hana.html')

@bp.route('/bnk/')
def bnk():
    return render_template('team/bnk.html')

@bp.route('/kb/')
def kb():
    return render_template('team/kb.html')

@bp.route('/shinhan/')
def shinhan():
    return render_template('team/shinhan.html')