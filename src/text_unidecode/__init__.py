# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
import pkgutil

# The table is ~3 MB once decoded; load it on first use, not at import.
_replaces = None

# 7-bit ASCII maps to itself, so it never needs the table (Python 3.7+).
_HAS_ISASCII = hasattr(str, 'isascii')


def _get_replaces():
    global _replaces
    if _replaces is None:
        _replaces = pkgutil.get_data(__name__, 'data.bin').decode('utf8').split('\x00')
    return _replaces


def unidecode(txt):
    if _HAS_ISASCII and type(txt) is str and txt.isascii():
        return txt
    replaces = _get_replaces()
    chars = []
    for ch in txt:
        codepoint = ord(ch)

        if not codepoint:
            chars.append('\x00')
            continue

        try:
            chars.append(replaces[codepoint-1])
        except IndexError:
            pass
    return "".join(chars)
