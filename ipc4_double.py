#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
from multiprocessing import Process, Value
import ctypes
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 2.0

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, retour: Value) -> None:
    """
    Évalue une expression.
    Reour via via Multiprocessing.Value (shared memory)
    Type supporté: c_double = python float
    """
    try:
        assert retour.value == 99
        retour.value = float(safe_eval(expr))
        print(expr, '=', retour.value)
    except BaseException as ex:
        exexit(ex)


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        retour = Value(ctypes.c_double, 99.0)
        ps = Process(target=pyval, args=(expr, retour))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        if not ps.exitcode:
            print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, retour.value)
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
