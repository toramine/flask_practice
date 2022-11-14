from apps.app import db
from apps.crud.forms import MemoForm
from apps.crud.models import Memo
from flask import Blueprint, redirect, render_template, url_for

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static/crud",
)


@crud.route("/")
def index():
    memo_list = Memo.query.all()
    return render_template("crud/index.html", memo_list=memo_list)


@crud.route("/new", methods=["GET", "POST"])
def create_memo():
    form = MemoForm()
    if form.validate_on_submit():
        memo = Memo(title=form.title.data, text=form.text.data)
        db.session.add(memo)
        db.session.commit()
        return redirect(url_for("crud.index"))
    return render_template("crud/create.html", form=form)
