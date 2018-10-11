import re

processing_rules = [
    # remove redundant spaces
    (r'[ ]{2,}', ' '),
    # remove redundant line breaks
    (r'(?:\r\n){2,}', '\r\n'),
    # replace quotes " with french quotes
    (r'"([^>]*?)"(?![^<]*>)', '\u00ab\\1\u00bb'),
    # replace quotes ' with french quotes
    (r'\'(.*?)\'', '\u00ab\\1\u00bb'),
    # replace hyphen with m-dash
    (r'(\s)-(\s)', '\\1\u2014\\2'),
    # replace hyphen with n-dash in phone numbers
    (r'(\b\d{1,4}\b)-(?=\b\d{1,4}\b)', '\\1\u2013'),
    # bind numbers with next words using a non-breaking space
    (r'(\b\d+\b)\s(\b[а-яА-ЯёЁ]+\b)', '\\1\u00a0\\2'),
    # bind words of 1-2 characters with next words using a non-breaking space
    (r'(\b[а-яА-ЯёЁ]{1,2}\b)\s(\b[а-яА-ЯёЁ]+\b)', '\\1\u00a0\\2'),
]


def get_processed_text(source_text):
    processed_text = source_text

    for searched_pattern, applied_pattern in processing_rules:
        processed_text = re.sub(
            searched_pattern,
            applied_pattern,
            processed_text,
        )

    return processed_text
