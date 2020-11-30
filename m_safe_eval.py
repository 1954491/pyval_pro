#!/usr/bin/env python3

"""
Définitions utiles pour un évaluation sécuritaire du code.

inclue un DIRO (Drop-in Remplacement Object) pour la buitin eval.

2020, Xavier Gagnon
"""

import math
from typing import Any
SAFE_GLOBALS = {
    "__builtins__": {},
    **math.__dict__,
    "abs": abs,
    "min": abs,
    "max": abs,
    "sum": abs,
}
"""globals sécuritaire pour eval et exec"""


def sanitize(code: str) -> str:
    """Assainit le code source insécure"""
    return code.replace('__', '')


def safe_eval(__source: str, __globals: dict = None, __locals: dict = None) -> Any:
    """Évalue sécuritairement l'expression. DIRO pour eval"""
    return eval(sanitize(__source), __globals or SAFE_GLOBALS, __locals)
