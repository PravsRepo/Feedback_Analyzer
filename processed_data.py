import pandas as pd
import re
import contractions
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk.download('stopwords')


class DataProcessor():
    """
        This class used to analyze the feeback submitted by students.
    """

    def __init__(self, file_name, sheet_name) -> None:
        self.file_name = file_name
        self.sheet_name = sheet_name

    def read_excel(self):
        df = pd.read_excel(
            self.file_name, sheet_name=self.sheet_name, index_col=False)
        # print(f'read_excel: {type(df)}')
        return df

    def column_to_text(self, df, column_name):
        text_df = df[column_name]
        # print(len(text_df))
        # print(f'column_to_text: {type(text_df)}')
        return text_df

    def make_lowercase(self, reqd_df):
        reg_exp = r'^[-_,.\s0-9]+$'
        reqd_df = reqd_df[~reqd_df.astype(str).str.contains(reg_exp)]
        reqd_df_lc = reqd_df.str.strip().str.lower()
        # print(reqd_df_lc[20:27])
        # print(f'make_lowercase: {type(reqd_df_lc)}')
        return reqd_df_lc

    def remove_spl_chars(self, reqd_df):
        reg_exp = re.compile(r"[’]")
        spl_char_regex = re.compile(r"[^A-Za-z0-9' ]+")
        for index, text in enumerate(reqd_df):
            if reg_exp.search(text):
                reqd_df[index] = reg_exp.sub("'", text)
            else:
                reqd_df[index] = text
            reqd_df[index] = spl_char_regex.sub(" ", reqd_df[index].strip())
        return reqd_df

    def contraction_values(self):
        contractions_dict = {
            "it's": "it is",
            "can't": "cannot",
            "didn't": "did not", "i'd": "i had / i would", "i'm": "i am", "i've": "i have",
            "don't": "do not"
            # Add more contractions as needed
        }
        con_keys = contractions_dict.keys()
        return con_keys

    def handle_contractions(self, reqd_df, con_keys):
        print(con_keys)
        reqd_df_hc = reqd_df.copy()
        for index, text in enumerate(reqd_df_hc):
            if any(key in text for key in con_keys):
                reqd_df_hc[index] = contractions.fix(text)
            else:
                reqd_df_hc[index] = text
        return reqd_df_hc

    # remove stop words
    def remove_stop_words(self, token_words):
        stop_words = set(stopwords.words("english"))
        filtered_list = []
        stop_words_list = []
        for token in token_words:
            # print(token)
            for word in token:
                if word not in stop_words:
                    filtered_list.append(word)
                else:
                    stop_words_list.append(word)
        return filtered_list

    def sentence_tokenize(self, reqd_df):
        stop_words = set(stopwords.words("english"))
        token_sents = []
        words_list = []
        sentence_list = []
        for text in reqd_df:
            token_sents.extend(sent_tokenize(text))
        for i in token_sents[0:]:
            token_words = word_tokenize(i)
            words_list.clear()
            for j in token_words:
                if j not in stop_words:
                    words_list.append(j)
            sentence = " ".join(words_list)
            sentence_list.append(sentence)
        return sentence_list
    
    def tokenize_words(self, sentence_list):
        token_words = []
        for sentence in sentence_list[0:]:
            token_words.append(word_tokenize(sentence))
        # print(token_words)
        return token_words
  
    def correct_spelling(self, df):
        pass

    def processed_excel(self, reqd_df):
        reqd_df.to_excel("Processed_data_readyto_analyze.xlsx",
                         sheet_name="Processed data", header=True, index=False)
