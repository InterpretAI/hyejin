from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
 

class PromptForm(FlaskForm):
    component = StringField('Component', validators=[DataRequired('Universe Component를 입력해주세요.')])
    content = TextAreaField('Prompt', validators=[DataRequired('전송하고자 하는 프롬프트를 입력해주세요.')])

 
class AnswerForm(FlaskForm):
    content = TextAreaField('Prompt', validators=[DataRequired('답변을 생성하고자 합니다.')])


class UserCreateForm(FlaskForm):
    username = StringField('ID', validators=[DataRequired(), Length(min=3, max=10)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('ID', validators=[DataRequired(), Length(min=3, max=10)])
    password = PasswordField('비밀번호', validators=[DataRequired()])