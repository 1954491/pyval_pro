#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
from multiprocessing import Process
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 2.0

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, retour: list) -> None:
    """
    Évalue une expression.
    Reour via via argument
    """
    try:
        assert retour[0] == 99
        retour[0] = safe_eval(expr)
        print(expr, '=', retour[0])
    except BaseException as ex:
        exexit(ex)


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        retour = [99]
        ps = Process(target=pyval, args=(expr, retour))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        if not ps.exitcode:
            print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, retour[0])
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
