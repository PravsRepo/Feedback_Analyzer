'''
    LEAP Bootcamp feedback analysis.

    Author: Praveenkumar
    Date: 28-12-2023
    Version: 1.0

'''
import nltk
import pandas as pd
from nltk import sent_tokenize, word_tokenize
from nltk import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk import ngrams
from nltk.lm import NgramCounter

class Feedback_Analyzer():
    """
        This class used to analyze the feeback submitted by students.
    """

    def __init__(self, file_name, sheet_name) -> None:
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.wnl = WordNetLemmatizer()

    def read_excel(self):
        df = pd.read_excel(self.file_name, sheet_name=self.sheet_name, index_col=False)
        return df

    def data_of_satisfaction_enjoyment(self, df):
        satenj_responses = df.value_counts("How much satisfied are you with the course and enjoyed the experience?")
        satenj_responses = satenj_responses.to_dict()
        # satenj_responses["Question"] = "How much satisfied are you with the course and enjoyed the experience?"
        # print(satenj_responses)
        return satenj_responses
    
    def data_of_course_structure(self, df):
        course_structure = df.value_counts("Structure of the course was:")
        course_structure = course_structure.to_dict()
        # print(course_structure)
        return course_structure
    
    def data_of_expert_lecture_effectiveness(self, df):
        expert_lecture_effectiveness = df.value_counts("Effectiveness of the expert lectures:")
        expert_lecture_effectiveness = expert_lecture_effectiveness.to_dict()
        # print(expert_lecture_effectiveness)
        return expert_lecture_effectiveness
    
    def data_of_practical_effectivness(self, df):
        practical_effectivness = df.value_counts("Effectiveness of the Practical /Hands-on activities:")
        practical_effectivness = practical_effectivness.to_dict()
        # print(practical_effectivness)
        return practical_effectivness

    def parts_of_speech(self, token_words):
        pos_list = []
        for token in token_words[0:]:
            pos_list.append(nltk.pos_tag(token))
        # print(pos_list[0:5])
        return pos_list
    
    def dup_lemmatizing(self, pos_list):
        for index, (word, _) in enumerate(pos_list):
            pos_list[index] = self.wnl.lemmatize(word)
        # print(pos_list[0:])
        return pos_list
    
    def lemmatizing(self, pos_list):
        lemmatized_sentence_list, lemmatized_words_list = [],[]
        for i in pos_list[0:]:
            for index, (word, word_tag) in enumerate(i):
                # print(index, f"word:{word}\t word_tag:{word_tag}")
                if word_tag in {"NN", "NNS", "NNP", "NNPS"}:
                    pos_list[index] = self.wnl.lemmatize(word, 'n')
                elif word_tag in {"VB", "VBD", "VBG", "VBN", "VBP", "VBZ"}:
                    pos_list[index] = self.wnl.lemmatize(word, 'v')
                elif word_tag in {"JJ", "JJR", "JJS"}:
                    pos_list[index] = self.wnl.lemmatize(word, 'a')
                elif word_tag in {"RB", "RBR", "RBS"}:
                    pos_list[index] = self.wnl.lemmatize(word, 'r')
                else:
                    pos_list[index] = self.wnl.lemmatize(word)
            lemmatized_words_list.extend(pos_list[0:index+1])
            lemmatized_sentence_list.append(pos_list[0:index+1])
        # print(pos_list_lemmatized)
        return lemmatized_sentence_list, lemmatized_words_list
    
    
    def get_freq_distribution(self, input_data):
        freq_distribution = FreqDist(input_data)
        # print(freq_distribution.most_common(40))
        return freq_distribution

    def get_ngrams(self, lemmatized_sentence_list):
        sentence_bigrams, sentence_trigrams = [], []
        for sentence in lemmatized_sentence_list[0:]:
           sentence_bigrams.extend(list(ngrams(sentence, 2)))
           sentence_trigrams.extend(list(ngrams(sentence, 3)))
        freq_distribution_bigrams = FreqDist(sentence_bigrams)
        freq_distribution_trigrams = FreqDist(sentence_trigrams)
        # print(freq_distribution_bigrams.most_common(40))
        # print(freq_distribution_trigrams.most_common(20))
        return sentence_bigrams, sentence_trigrams
    
    
    def ngrams_counter(self, sentence_bigrams, sentence_trigrams):
        bigram_counts = NgramCounter(sentence_bigrams).N()
        trigram_counts = NgramCounter(sentence_trigrams).N()
        # print(f"bigram_counts: {bigram_counts}, trigram_counts: {trigram_counts}")
        return bigram_counts, trigram_counts

    def visualize_data(self):
        pass

    def data_of_improve_course(self, df):
        pass

    






