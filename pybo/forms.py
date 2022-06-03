from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class FreeForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class NewsForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired()])
    content = TextAreaField('내용', validators=[DataRequired()])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class FanswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])


class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    phone = StringField('전화번호', validators=[DataRequired(), Length(min=10, max=11)])
    birth = StringField('생년월일', validators=[DataRequired(), Length(min=8, max=8)])


class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


class MyPageForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    phone = StringField('전화번호', validators=[DataRequired(), Length(min=10, max=11)])
    birth = StringField('생년월일', validators=[DataRequired(), Length(min=8, max=8)])

#class IntroductionForm(FlaskForm):
 #   subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
  #  content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])