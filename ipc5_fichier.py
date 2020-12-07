#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
from multiprocessing import Process
import pickle
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 2.0

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, filename: str) -> None:
    """
    Évalue une expression.
    Reour via via Multiprocessing.Value (shared memory)
    Type supporté: c_double = python float
    """
    try:
        evaluation = safe_eval(expr)
        print(expr, '=', evaluation)
        with open(filename, 'w+b') as f:
            pickle.dump(evaluation, f)

    except BaseException as ex:
        exexit(ex)


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        filename = "ipc5.bin"
        ps = Process(target=pyval, args=(expr, filename))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        if not ps.exitcode:
            with open(filename, "r+b") as f:
                evaluation = pickle.load(f)
                print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, evaluation)
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
