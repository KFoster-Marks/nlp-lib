import spacy
import urllib
import html2text
import os.path

from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)

# TODO: Turn these into classes; consider renaming

def check_is_stop_word(text):
    # TODO: practice error handling
    return nlp.vocab[text].is_stop

def write_url_html_to_file(url, file_name):
    file_exists = os.path.exists(file_name)

    if (file_exists == False):
        page = urllib.request.urlopen(url)
        html_content = page.read().decode('utf-8')
        rendered_content = html2text.html2text(html_content)
        file = open(file_name, 'w')
        file.write(rendered_content)
        file.close()
    else:
        print('File already exists.')

def get_text_match(input_text, phrase_list, start_context, end_context):
    text_matches = []
    doc = nlp(input_text)
    phrase_patterns = [nlp(text) for text in phrase_list]
    matcher.add('TestMatcher', None, *phrase_patterns)
    found_matches = matcher(doc)

    for match_id, start, end in found_matches:
        span = doc[start-start_context:end+end_context]
        text_matches.append(span.text)

    return text_matches

def get_raw_part_of_speech_counts(text):
    doc = nlp(text)
    pos_counts = doc.count_by(spacy.attrs.POS)

    return pos_counts

def get_part_of_speech_counts(text):
    pos_dict = {}
    doc = nlp(text)
    raw_counts = get_raw_part_of_speech_counts(text)

    for pos, count in raw_counts.items():
        pos_dict[doc.vocab[pos].text] = count

    return pos_dict
