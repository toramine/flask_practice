from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class MemoForm(FlaskForm):
    title = StringField(
        "title",
        validators=[
            DataRequired(message="タイトルは必須です"),
            length(max=20, message="20文字以内で入力してください"),
        ],
    )

    text = StringField("text", validators=[length(max=50, message="50文字以内で入力してください")])

    submit = SubmitField("保存")
