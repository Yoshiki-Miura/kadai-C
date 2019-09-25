class WordFilter:
    def __init__(self, words):
        self.words = words

    def detect(self, message):
        for i in range(len(self.words)):
            if message.find(self.words[i]) != -1:
                return True
        return False

    def censor_free(self, message):
        for i in range(len(self.words)):
            freeword = input(f"置換したい文字列を入力してください ({self.words[i]}) : ")
            message = message.replace(self.words[i], freeword)

        return message


def main():
    words = input("NGワードを入力してください: ").split()
    my_filter = WordFilter(words)

    # NGワードが含まれている場合
    print(my_filter.censor_free("昨日のアーセナルの試合アツかった！"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    print(my_filter.censor_free("昨日のリバプールの試合アツかった！"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！


if __name__ == '__main__':
    main()
