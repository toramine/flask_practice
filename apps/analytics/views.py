from apps.analytics.mecab import Wakati
from flask import Blueprint, redirect, render_template, url_for

analytics = Blueprint(
    "analytics",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@analytics.route("/")
def index():
    return render_template("analytics/index.html")


@analytics.route("/mecab", methods=["GET", "POST"])
def mecab_analysis(memo_text):
    wakati = Wakati()
    res = wakati.parse(memo_text).split()
    return res


@analytics.route("/analysis")
def analysis():
    return redirect(url_for("analytics.index"))
