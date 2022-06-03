from datetime import datetime

from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import NewsForm
from pybo.models import News,User
from pybo.views.auth_views import login_required

bp = Blueprint('news', __name__, url_prefix='/news')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    news_list = News.query.order_by(News.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        #sub_query = db.session.query(News.id, News.content, User.username) \
            #.join(User,News.id == User.id).subquery()

        news_list = news_list \
            .join(User) \
            .filter(News.subject.ilike(search) |  # 뉴스제목
                    News.content.ilike(search) |  # 뉴스내용
                    User.username.ilike(search)   # 뉴스작성자
                    ) \
            .distinct()
    news_list = news_list.paginate(page, per_page=10)
    return render_template('news/news_list.html', news_list=news_list, page=page, kw=kw)



@bp.route('/detail/<int:news_id>/')
def detail(news_id):
    news = News.query.get_or_404(news_id)
    return render_template('news/news_detail.html', news=news)

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = NewsForm()
    if request.method == 'POST' and form.validate_on_submit():
        news = News(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('news/news_form.html', form=form)

@bp.route('/modify/<int:news_id>', methods=('GET', 'POST'))
@login_required
def modify(news_id):
    news = News.query.get_or_404(news_id)
    if g.user != news.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('news.detail', news_id=news_id))
    if request.method == 'POST':  # POST 요청
        form = NewsForm()
        if form.validate_on_submit():
            form.populate_obj(news)
            news.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('news.detail', news_id=news_id))
    else:  # GET 요청
        form = NewsForm(obj=news)
    return render_template('news/news_form.html', form=form)

@bp.route('/vote/<int:news_id>/')
@login_required
def vote(news_id):
    news = News.query.get_or_404(news_id)
    if g.user == news.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        news.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('news.detail', news_id=news_id))

@bp.route('/delete/<int:news_id>')
@login_required
def delete(news_id):
    news = News.query.get_or_404(news_id)
    if g.user != news.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('news.detail', news_id=news_id))
    db.session.delete(news)
    db.session.commit()
    return redirect(url_for('news._list'))