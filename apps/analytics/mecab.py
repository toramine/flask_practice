import MeCab


class Wakati:
    def wakati(self, memo_text):
        wakati = MeCab.Tagger("-Owakati")
        res = wakati.parse(memo_text).split()
        return res


# def mecab_analysis(memo_text):
#     # text = "今日は天気が良い"
#     wakati = MeCab.Tagger("-Owakati")
#     res = wakati.parse(memo_text).split()
#     return res
