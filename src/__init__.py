from .lemmatize import get_lemmas

from .entities import add_named_entity
from .entities import get_named_entities
from .entities import get_named_entities_metadata
from .entities import get_named_entity_label_explanations
from .entities import get_named_entities_by_label
from .entities import get_number_of_named_entities_by_label

from .segment import get_segments
from .segment import get_custom_segment

from .tokenize import get_tokens
from .tokenize import get_base_noun_phrases

from .visualize import serve_dependency_viz
from .visualize import render_dependency_html

from .vocab import check_is_stop_word
from .vocab import write_url_html_to_file
from .vocab import get_text_match
from .vocab import get_part_of_speech_counts
from .vocab import get_raw_part_of_speech_counts