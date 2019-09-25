class WordFilter:
    def __init__(self, word):
        self.word = word

    def detect(self, message):
        if message.find(self.word) != -1:
            return True
        else:
            return False

    def censor(self, message):
        return message.replace(self.word, "<censored>")


def main():
    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    print(my_filter.censor("昨日のアーセナルの試合アツかった！"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    print(my_filter.censor("昨日のリバプールの試合アツかった！"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！


if __name__ == '__main__':
    main()
