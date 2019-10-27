import spacy

nlp = spacy.load("en_core_web_sm")

def get_segments(text):
    doc = nlp(text)

    return [sent.text for sent in doc.sents]