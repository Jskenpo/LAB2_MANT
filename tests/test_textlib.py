import pytest
from textlib import reverse, count_vowels, is_palindrome, to_upper, concat

# reverse: 2 happy + 1 error/borde
def test_reverse_basic():
    assert reverse("hola") == "aloh"

def test_reverse_with_spaces():
    assert reverse("abc def") == "fed cba"

def test_reverse_type_error():
    with pytest.raises(TypeError):
        reverse(123)  # type: ignore

# count_vowels: 2 happy + 1 borde
def test_count_vowels_mixed_case():
    assert count_vowels("AEiou") == 5

def test_count_vowels_no_vowels():
    assert count_vowels("rhythms") == 0

def test_count_vowels_type_error():
    with pytest.raises(TypeError):
        count_vowels(None)  # type: ignore

# is_palindrome: 2 happy + 1 borde
def test_is_palindrome_phrase_ignores_spaces_and_punct():
    assert is_palindrome("Anita lava la tina!") is True

def test_is_palindrome_false_case():
    assert is_palindrome("OpenAI") is False

def test_is_palindrome_type_error():
    with pytest.raises(TypeError):
        is_palindrome(3.1416)  # type: ignore

# to_upper: 2 happy + 1 borde
def test_to_upper_basic():
    assert to_upper("hola") == "HOLA"

def test_to_upper_accents_preserved():
    # Se preservan tildes (no translitera)
    assert to_upper("canción") == "CANCIÓN"

def test_to_upper_type_error():
    with pytest.raises(TypeError):
        to_upper(["x"])  # type: ignore

# concat: 2 happy + 1 borde
def test_concat_basic():
    assert concat("Appoint", "Me") == "AppointMe"

def test_concat_empty():
    assert concat("", "GT") == "GT"

def test_concat_type_error_if_any_arg_not_str():
    with pytest.raises(TypeError):
        concat("hola", 5)  # type: ignore