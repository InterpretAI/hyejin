from datetime import datetime

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

from .. import db
from ..forms import AnswerForm
from ..models import Prompt, Answer, Rating
from iai.views.auth_views import login_required
from ..utils import generate_answer

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:prompt_id>', methods=('POST',))
def create(prompt_id):
    prompt = Prompt.query.get(prompt_id)
    # content = request.form['content']
    generated_content = generate_answer(prompt.content)
    # answer = Answer(content=content, create_date=datetime.now(), user=g.user)
    new_answer = Answer(content=generated_content, create_date=datetime.now(), user=g.user)
    prompt.answer_set.append(new_answer)
    db.session.commit()

    # form = AnswerForm()
    # prompt = Prompt.query.get(prompt_id)
    # if form.validate_on_submit():
    #     content = request.form['content']
    #     answer = Answer(content=content, create_date=datetime.now())
    #     prompt.answer_set.append(answer)
    #     db.session.commit()
    #     return redirect('{}#answer_{}'.format(
    #         url_for('prompt.detail', prompt_id=prompt_id), answer.id))
    return render_template('prompt/prompt_detail.html', prompt=prompt)
    # return render_template('prompt/prompt_detail.html', prompt=prompt, form=form)




@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
@login_required
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    if g.user != answer.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('prompt.detail', prompt_id=answer.prompt.id))
    if request.method == "POST":
        form = AnswerForm()
        if form.validate_on_submit():
            form.populate_obj(answer)
            answer.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect('{}#answer_{}'.format(
                url_for('prompt.detail', prompt_id=answer.prompt.id), answer.id))
    else:
        form = AnswerForm(obj=answer)
    return render_template('answer/answer_form.html', form=form)


@bp.route('/delete/<int:answer_id>')
@login_required
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    prompt_id = answer.prompt.id
    if g.user != answer.user:
        flash('삭제권한이 없습니다')
    else:
        db.session.delete(answer)
        db.session.commit()
    return redirect(url_for('prompt.detail', prompt_id=prompt_id))


@bp.route('/submit_rating/<int:answer_id>', methods=['POST'])
@login_required
def submit_rating(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    rating_value = int(request.form['rating'])
    
    existing_rating = Rating.query.filter_by(answer=answer, user=g.user).first()
    if existing_rating:
        return "이미 이 답변에 대해 평가하셨습니다."

    new_rating = Rating(answer=answer, user=g.user, rate=rating_value)
    db.session.add(new_rating)
    db.session.commit()
    return redirect('{}#answer_{}'.format(
                url_for('prompt.detail', prompt_id=answer.prompt.id), answer.id))