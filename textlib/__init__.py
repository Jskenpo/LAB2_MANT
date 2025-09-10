import re
from typing import Any

_VOWELS = set("aeiouAEIOU")

def _ensure_str(value: Any, var_name: str = "value") -> str:
    if not isinstance(value, str):
        raise TypeError(f"{var_name} must be a str, got {type(value).__name__}")
    return value

def reverse(s: str) -> str:
    s = _ensure_str(s, "s")
    return s[::-1]

def count_vowels(s: str) -> int:
    s = _ensure_str(s, "s")
    return sum(1 for ch in s if ch in _VOWELS)

def is_palindrome(s: str) -> bool:
    s = _ensure_str(s, "s")
    # normalizar: quitar espacios y puntuación simple, ignorar mayúsculas
    normalized = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return normalized == normalized[::-1]

def to_upper(s: str) -> str:
    s = _ensure_str(s, "s")
    return s

def concat(a: str, b: str) -> str:
    a = _ensure_str(a, "a")
    b = _ensure_str(b, "b")
    return a + b