from apps.analytics.mecab import Wakati
from apps.app import db
from apps.crud.forms import MemoForm
from apps.crud.models import Memo
from flask import Blueprint, redirect, render_template, request, url_for

crud = Blueprint(
    "crud",
    __name__,
    template_folder="templates",
    static_folder="static/crud",
)


@crud.route("/")
def index():
    memo_list = Memo.query.all()
    form = MemoForm()
    return render_template("crud/index.html", memo_list=memo_list, form=form)


@crud.route("/new", methods=["GET", "POST"])
def create_memo():
    form = MemoForm()
    if form.validate_on_submit():
        memo = Memo(title=form.title.data, text=form.text.data)
        db.session.add(memo)
        db.session.commit()
        return redirect(url_for("crud.index"))
    return render_template("crud/create.html", form=form)


@crud.route("/<memo_id>", methods=["GET", "POST"])
def edit_memo(memo_id):

    default_value = ""
    input_value = request.form.get("mecab", default_value)

    form = MemoForm()
    wakati = Wakati()

    memo = Memo.query.filter_by(id=memo_id).first()

    if not input_value == "分かち書き" and form.validate_on_submit():
        memo.title = form.title.data
        memo.text = form.text.data
        db.session.add(memo)
        db.session.commit()
        return redirect(url_for("crud.index"))

    wakati_text = form.text.data
    if wakati_text:
        res = wakati.wakati(wakati_text)
        memo.text = form.text.data
    else:
        res = ""

    return render_template("crud/edit.html", memo=memo, form=form, wakati=res)


@crud.route("/<memo_id>/delete", methods=["POST"])
def delete_memo(memo_id):
    memo = Memo.query.filter_by(id=memo_id).first()
    db.session.delete(memo)
    db.session.commit()
    return redirect(url_for("crud.index"))
