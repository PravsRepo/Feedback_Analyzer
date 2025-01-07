'''
    LEAP Bootcamp feedback analysis.

    Author: praveen@leap.respark.itm.ac.in
    Date: 28-12-2023
    Version: 1.0

'''

from processed_data import DataProcessor
from feedback_analyze import Feedback_Analyzer



file_name = "D:/Python Projects/feedback_analysis/_LPB02S5_GRD Students_Feedback form (Responses).xlsx"
sheet_name = "Form Responses 1"
column_name = "Please give three suggestions to improve the effectiveness of the course:"
    
# print(file_name)
# Dataprocessor methods
processor_obj = DataProcessor(file_name, sheet_name)
df = processor_obj.read_excel()
reqd_text_df = processor_obj.column_to_text(df, column_name)
reqd_lc_df = processor_obj.make_lowercase(reqd_text_df)
reqd_rsc_df = processor_obj.remove_spl_chars(reqd_lc_df)
con_keys = processor_obj.contraction_values()
reqd_hc_df = processor_obj.handle_contractions(reqd_rsc_df, con_keys)
# processor_obj.tokenize_words(reqd_hc_df)
# processor_obj.processed_excel(reqd_df)
sentence_list = processor_obj.sentence_tokenize(reqd_hc_df)
token_words = processor_obj.tokenize_words(sentence_list)


# Feedback_Analyzer methods
analyzer = Feedback_Analyzer(file_name, sheet_name)
# dataframe = analyzer.read_excel()
# analyzer.data_of_satisfaction_enjoyment(dataframe)
# course_structure = analyzer.data_of_course_structure(dataframe)
# expert_lecture_effectiveness = analyzer.data_of_expert_lecture_effectiveness(dataframe)
# practical_effectivness = analyzer.data_of_practical_effectivness(dataframe)
# pos_list = analyzer.parts_of_speech(token_words)
# analyzer.dup_lemmatizing(pos_list)
# lemmatized_sentence_list, lemmatized_words_list = analyzer.lemmatizing(pos_list)
# analyzer.get_freq_distribution(lemmatized_words_list)
# sentence_bigrams, sentence_trigrams = analyzer.get_ngrams(lemmatized_sentence_list)
# analyzer.ngrams_counter(sentence_bigrams, sentence_trigrams)