def is_text_equal(text1, text2):
    return text1 == text2


def check_text_equal(text1, text2):
    assert (is_text_equal(text1, text2)), 'The text on the page is different than expected'


def check_text_contains(text1, text2):
    assert (text2 in text1), f'Text {text2} is not substring of {text1}'
