import re

processing_rules = [
    (r'\s+', ' '),
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
