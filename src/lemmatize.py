import spacy

nlp = spacy.load("en_core_web_sm")

def get_lemmas(text):
    doc = nlp(text)
    parse_string = ''

    for token in doc:
        parse_string = f'{token.text:{12}} | {token.pos_:{5}} | {token.lemma_}'
        print(parse_string)

    return parse_string