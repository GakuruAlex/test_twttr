import pytest
from twttr import shorten
@pytest.mark.parametrize("word, short",[
    ("hello", "hll"),
    ("john", "jhn"),
    ("hello world", "hll wrld")
    
])
def test_shorten_with_lowercase_str(word, short):
    assert shorten(word) == short
    

@pytest.mark.parametrize("word, short",[
    ("HELLO", "HLL"),
    ("JOHN", "JHN"),
    ("HELLO WORLD", "HLL WRLD")
    
])
def test_shorten_with_uppercase_str(word, short):
    assert shorten(word) == short

@pytest.mark.parametrize("word, short",[
    ("HELL0", "HLL0"),
    ("J0HN", "J0HN"),
    ("HELL0, W0RLD!", "HLL0, W0RLD!")
    
])
def test_shorten_with_digits_and_punctuation_str(word, short):
    assert shorten(word) == short