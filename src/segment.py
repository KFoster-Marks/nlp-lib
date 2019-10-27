import spacy

nlp = spacy.load("en_core_web_sm")

def get_segments(text):
    doc = nlp(text)

    return [sent.text for sent in doc.sents]

def get_custom_segment(text):
    nlp.add_pipe(set_custom_boundary, before='parser')
    doc = nlp(text)

    return [sent.text for sent in doc.sents]

def set_custom_boundary(doc):
    for token in doc[:-1]:
        if token.text == ';':
            doc[token.i+1].is_sent_start = True

    return doc