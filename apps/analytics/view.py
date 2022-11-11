import MeCab
from flask import Blueprint, redirect, render_template, url_for

# sys.setdefaultencoding("utf-8")

analytics = Blueprint(
    "analytics",
    __name__,
    template_folder="templates",
    static_folder="static",
)


def mecab_analysis():
    text = "今日は天気が良い"
    wakati = MeCab.Tagger("-Owakati")
    res = wakati.parse(text).split()
    return res


@analytics.route("/")
def index():
    return render_template("analytics/index.html")


@analytics.route("/mecab")
def mecab_res():
    return mecab_analysis()


@analytics.route("/analysis")
def analysis():
    return redirect(url_for("analytics.index"))
