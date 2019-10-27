import spacy

nlp = spacy.load("en_core_web_sm")

def get_segments(text):
    doc = nlp(text)

    return [sent.text for sent in doc.sents]

# def get_custom_segment(text, delimiter):
#     doc = nlp(text)
#     doc = set_custom_boundary(doc, delimiter)
#     nlp.add_pipe(set_custom_boundary, before='parser')
#     print(nlp.pipe_names)

# def set_custom_boundary(doc, delimiter):
#     for token in doc[:-1]:
#         if token.text == delimiter:
#             print('DELIMITER: ', token.text)
#             doc[token.i+1].is_sent_start = True

#     return doc