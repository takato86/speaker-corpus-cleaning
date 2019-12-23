import xlrd
import pandas as pd


class SentenceManager:
    def __init__(self, file_path):
        self.content_df = self._load_text(file_path)

    def __iter__(self):
        sentence_list = self.content_df["発話内容"].tolist()
        for sentence in sentence_list:
            yield sentence
        raise StopIteration()

    def _load_text(self, file_path):
        wb = xlrd.open_workbook(file_path)
        sheet = wb.sheets()[0]
        columns = [column.replace(" ", "")
                   for column in sheet.row_values(2, 3, 8)]
        contents = [sheet.row_values(x, 3, 8)
                    for x in range(3, sheet.nrows)
                    if sheet.row_values(x, 3, 8)[0] != '']
        df = pd.DataFrame(contents, columns=columns)
        df.set_index("ライン番号", inplace=True)
        df["発話内容"] = df["発話内容"].apply(lambda f: Sentence(f))
        return df

    def export(self, file_path):
        self.content_df.to_csv(file_path)


class Sentence:
    def __init__(self, content):
        self.content = content

    def delete_only_symbol(self, symbols=[]):
        """記号のみ削除する

        Keyword Arguments:
            symbols {list} -- [description] (default: {[]})
        """
        pass

    def delete_text_in_symbol(self, symbol=()):
        """記号に囲まれたテキストと記号を削除する

        Keyword Arguments:
            symbol {tuple} -- [description] (default: {()})
        """
        pass

    def delete_specific_text(self, text):
        """textで与えられた文字列を削除する．

        Arguments:
            text {[type]} -- [description]
        """
        pass
