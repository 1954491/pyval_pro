#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
from typing import Optional

from m_safe_eval import safe_eval
from pyval_safe import exexit
import sys
from multiprocessing import Process, Pipe
from multiprocessing.connection import Connection
import colorama
from colorama import Fore

colorama.init()

DELAI_SEC = 2.0
ARRAY_SIZE = 2048

EVALUATION = None
"""Variable globale utilisée pour récupérer le résultat"""


def pyval(expr: str, pipe: Connection) -> None:
    """
    Évalue une expression.
    Retour (sérialisé) via pipe
    """
    try:
        evaluation = safe_eval(expr)
    except BaseException as ex:
        evaluation = ex
    pipe.send(evaluation)
    pipe.close()


def main() -> None:
    """Fonction principale"""
    ps: Optional[Process] = None
    try:
        expr = ' '.join(sys.argv[1:]) or "None"
        parent_conn, child_conn = Pipe()
        ps = Process(target=pyval, args=(expr, child_conn))
        ps.start()
        ps.join(DELAI_SEC)
        if not parent_conn.poll(DELAI_SEC):
            raise TimeoutError(f"Le délai de {DELAI_SEC} seconde est écoulé")
        evaluation = parent_conn.recv()
        if isinstance(evaluation, BaseException):
            raise evaluation
        print(Fore.CYAN + "Selon Xavier Gagnon:" + Fore.RESET, evaluation)
    except Exception as ex:
        exexit(ex)
    except KeyboardInterrupt:
        pass
    finally:
        ps and ps.terminate()


if __name__ == '__main__':
    main()
