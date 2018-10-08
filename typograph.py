import re

processing_rules = [
    # replace quotes " with french quotes
    (r'"([^>]*?)"(?![^<]*>)', u'\u00ab\\1\u00bb'),
    # replace quotes ' with french quotes
    (r'\'(.*?)\'', u'\u00ab\\1\u00bb'),
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
