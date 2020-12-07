#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
from multiprocessing import Process, Queue
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 2.0
ARRAY_SIZE = 2048

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, queue: Queue) -> None:
    """
    Évalue une expression.
    Retour (sérialisé) via pipe
    """
    try:
        evaluation = safe_eval(expr)
    except BaseException as ex:
        evaluation = ex
    queue.put(evaluation)


def main() -> None:
    """Fonction principale"""
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        queue = Queue()
        ps = Process(target=pyval, args=(expr, queue))
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        evaluation = queue.get()
        if isinstance(evaluation, BaseException):
            raise evaluation
        print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, evaluation)
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
