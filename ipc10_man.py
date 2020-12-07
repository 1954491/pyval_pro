#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""

from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
from queue import Empty
import multiprocessing as mp
from multiprocessing.managers import Namespace
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 22222.0

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, ns: Namespace) -> None:
    """
    Évalue une expression.
    Retour (sérialisé) via pipe
    """
    try:
        evaluation = safe_eval(expr)
    except BaseException as ex:
        evaluation = ex
    ns.evaluation = evaluation


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        man = mp.Manager()
        ns = man.Namespace()
        ps = mp.Process(target=pyval, args=(expr, ns))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        evaluation = ns.evaluation
        if isinstance(evaluation, BaseException):
            raise evaluation
        print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, evaluation)
    except Empty:
        exexit(TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé"))

    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
