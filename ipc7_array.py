#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
import multiprocessing as mp
import pickle
import ctypes
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 2.0
ARRAY_SIZE = 2048

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, retour: mp.Array) -> None:
    """
    Évalue une expression.
    Reour via via Multiprocessing.Value (shared memory)
    Type supporté: c_double = python float
    """
    try:
        evaluation = safe_eval(expr)
    except BaseException as ex:
        evaluation = ex
    serialisation: bytes = pickle.dumps(evaluation)
    retour[:len(serialisation)] = serialisation


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        retour = mp.Array(ctypes.c_char, ARRAY_SIZE)
        ps = mp.Process(target=pyval, args=(expr, retour))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        evaluation = pickle.loads(bytes(retour[:]))
        if isinstance(evaluation, BaseException):
            raise evaluation
        print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, evaluation)
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
