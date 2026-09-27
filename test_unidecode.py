# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from text_unidecode import unidecode
import pytest


@pytest.mark.parametrize(("text", "result"), [
    ("Programmes de publicité - Solutions d'entreprise", "Programmes de publicite - Solutions d'entreprise"),
    ("Транслитерирует и русский", "Transliteriruet i russkii"),
    ("kožušček", "kozuscek"),
    ("北亰", "Bei Jing "),
])
def test_transliterate(text, result):
    assert unidecode(text) == result


@pytest.mark.parametrize("code", range(128))
def test_7bit_purity(code):
    ch = chr(code)
    assert unidecode(ch) == ch


def test_7bit_text_purity():
    txt = "".join([chr(x) for x in range(128)])
    assert unidecode(txt) == txt


def test_table_loaded_lazily():
    import text_unidecode
    text_unidecode._replaces = None
    assert unidecode("plain ascii") == "plain ascii"
    if text_unidecode._HAS_ISASCII:
        assert text_unidecode._replaces is None
    assert unidecode("kožušček") == "kozuscek"
    assert text_unidecode._replaces is not None
