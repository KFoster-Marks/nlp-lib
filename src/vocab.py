import spacy

nlp = spacy.load("en_core_web_sm")

def check_is_stop_word(text):
    return nlp.vocab[text].is_stop