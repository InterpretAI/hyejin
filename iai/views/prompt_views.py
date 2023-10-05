from flask import Blueprint, render_template
from iai.models import Prompt
from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from .. import db
from ..models import Prompt
from ..forms import PromptForm, AnswerForm
from iai.views.auth_views import login_required

bp = Blueprint('prompt', __name__, url_prefix='/prompt')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    prompt_list = Prompt.query.order_by(Prompt.create_date.desc())
    prompt_list = prompt_list.paginate(page=page, per_page=15)
    return render_template('prompt/prompt_list.html', prompt_list=prompt_list)


@bp.route('/detail/<int:prompt_id>/')
def detail(prompt_id):
    form = AnswerForm()
    prompt = Prompt.query.get(prompt_id)
    return render_template('prompt/prompt_detail.html', prompt=prompt, form=form)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = PromptForm()
    if request.method == 'POST' and form.validate_on_submit():
        prompt = Prompt(component=form.component.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(prompt)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('prompt/prompt_form.html', form=form)

@bp.route('/modify/<int:prompt_id>', methods=('GET', 'POST'))
@login_required
def modify(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    if g.user != prompt.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('prompt.detail', prompt_id=prompt_id))
    if request.method == 'POST':  # POST 요청
        form = PromptForm()
        if form.validate_on_submit():
            form.populate_obj(prompt)
            prompt.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('prompt.detail', prompt_id=prompt_id))
    else:  # GET 요청
        form = PromptForm(obj=prompt)
    return render_template('prompt/prompt_form.html', form=form)


@bp.route('/delete/<int:prompt_id>')
@login_required
def delete(prompt_id):
    prompt = Prompt.query.get_or_404(prompt_id)
    if g.user != prompt.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('prompt.detail', prompt_id=prompt_id))
    db.session.delete(prompt)
    db.session.commit()
    return redirect(url_for('prompt._list'))