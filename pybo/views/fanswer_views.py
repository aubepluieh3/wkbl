from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import FanswerForm
from pybo.models import Free, Fanswer
from pybo.views.auth_views import login_required

bp = Blueprint('fanswer', __name__, url_prefix='/fanswer')


@bp.route('/create/<int:free_id>', methods=('POST',))
@login_required
def create(free_id):
    form = FanswerForm()
    free = Free.query.get_or_404(free_id)
    if form.validate_on_submit():
        content = request.form['content']
        fanswer = Fanswer(content=content, create_date=datetime.now(), user=g.user)
        free.fanswer_set.append(fanswer)
        db.session.commit()
        return redirect('{}#fanswer_{}'.format(
            url_for('free.detail', free_id=free_id), fanswer.id))
    return render_template('free/free_detail.html', free=free, form=form)


@bp.route('/modify/<int:fanswer_id>', methods=('GET', 'POST'))
@login_required
def modify(fanswer_id):
    fanswer = Fanswer.query.get_or_404(fanswer_id)
    if g.user != fanswer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('free.detail', free_id=fanswer.free.id))
    if request.method == "POST":
        form = FanswerForm()
        if form.validate_on_submit():
            form.populate_obj(fanswer)
            fanswer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#fanswer_{}'.format(
                url_for('free.detail', free_id=fanswer.free.id), fanswer.id))
    else:
        form = FanswerForm(obj=fanswer)
    return render_template('fanswer/fanswer_form.html', form=form)


@bp.route('/delete/<int:fanswer_id>')
@login_required
def delete(fanswer_id):
    fanswer = Fanswer.query.get_or_404(fanswer_id)
    free_id = fanswer.free.id
    if g.user != fanswer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(fanswer)
        db.session.commit()
    return redirect(url_for('free.detail',free_id=free_id))


@bp.route('/vote/<int:fanswer_id>/')
@login_required
def vote(fanswer_id):
    fanswer = Fanswer.query.get_or_404(fanswer_id)
    if g.user == fanswer.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        fanswer.voter.append(g.user)
        db.session.commit()
    return redirect('{}#fanswer_{}'.format(
                url_for('free.detail', free_id=fanswer.free.id), fanswer.id))