from apps.app import db
from apps.crud.forms import MemoForm
from apps.crud.models import Memo
from flask import Blueprint, redirect, render_template, url_for

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@crud.route("/")
def index():
    return render_template("crud/index.html")


@crud.route("/memo/new")
def create_memo():
    form = MemoForm()
    if form.validate_on_submit():
        memo = Memo(title=form.title.data, text=form.text.data)
        db.session.add(memo)
        db.session.commit()
        return redirect(url_for("crud.list"))
    return render_template("crud/create.html", form=form)


@crud.route("/list")
def memo_list():
    memo_list = Memo.query.all()
    return render_template("crud/index.html", memo_list=memo_list)
