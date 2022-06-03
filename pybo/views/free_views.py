from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import FreeForm, FanswerForm
from pybo.models import Free, Fanswer, User
from pybo.views.auth_views import login_required

bp = Blueprint('free', __name__, url_prefix='/free')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    free_list = Free.query.order_by(Free.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Fanswer.free_id, Fanswer.content, User.username) \
            .join(User, Fanswer.user_id == User.id).subquery()
        free_list = free_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.free_id == Free.id) \
            .filter(Free.subject.ilike(search) |  # 질문 제목
                    Free.content.ilike(search) |  # 질문 내용
                    User.username.ilike(search) |  # 질문 작성자
                    sub_query.c.content.ilike(search) |  # 답변 내용
                    sub_query.c.username.ilike(search)  # 답변 작성자
                    ) \
            .distinct()
    free_list = free_list.paginate(page, per_page=10)
    return render_template('free/free_list.html', free_list=free_list, page=page, kw=kw)


@bp.route('/detail/<int:free_id>/')
def detail(free_id):
    form = FanswerForm()
    free = Free.query.get_or_404(free_id)
    return render_template('free/free_detail.html', free=free, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = FreeForm()
    if request.method == 'POST' and form.validate_on_submit():
        free = Free(subject=form.subject.data, content=form.content.data,
                            create_date=datetime.now(), user=g.user)
        db.session.add(free)
        db.session.commit()
        return redirect(url_for('free._list'))
    return render_template('free/free_form.html', form=form)


@bp.route('/modify/<int:free_id>', methods=('GET', 'POST'))
@login_required
def modify(free_id):
    free = Free.query.get_or_404(free_id)
    if g.user != free.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('free.detail', free_id=free_id))
    if request.method == 'POST':  # POST 요청
        form = FreeForm()
        if form.validate_on_submit():
            form.populate_obj(free)
            free.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('free.detail', free_id=free_id))
    else:  # GET 요청
        form = FreeForm(obj=free)
    return render_template('free/free_form.html', form=form)


@bp.route('/delete/<int:free_id>')
@login_required
def delete(free_id):
    free = Free.query.get_or_404(free_id)
    if g.user != free.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('free.detail', free_id=free_id))
    db.session.delete(free)
    db.session.commit()
    return redirect(url_for('free._list'))


@bp.route('/vote/<int:free_id>/')
@login_required
def vote(free_id):
    free = Free.query.get_or_404(free_id)
    if g.user == free.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        free.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('free.detail', free_id=free_id))