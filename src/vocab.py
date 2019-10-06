import spacy
import urllib
import html2text

nlp = spacy.load("en_core_web_sm")

def check_is_stop_word(text):
    return nlp.vocab[text].is_stop

def write_url_html_to_file(url, file_name):
    page = urllib.request.urlopen(url)
    html_content = page.read().decode('utf-8')
    rendered_content = html2text.html2text(html_content)
    file = open(file_name, 'w')
    file.write(rendered_content)
    file.close()

def get_text_match(text, phrase_list, start_context, end_context):
    phrase_patterns = [nlp(text) for phrase in phrase_list]
    print(phrase_patterns)