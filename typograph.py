import re

processing_rules = [
    # replace quotes " with french quotes
    (r'"([^>]*?)"(?![^<]*>)', u'\u00ab\\1\u00bb'),
    # replace quotes ' with french quotes
    (r'\'(.*?)\'', u'\u00ab\\1\u00bb'),
    # replace hyphen with m-dash
    (r'(\s)-(\s)', u'\\1\u2014\\2'),
    # replace hyphen with n-dash in phone numbers
    (r'(\b\d{1,4}\b)-(?=\b\d{1,4}\b)', u'\\1\u2013'),
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
