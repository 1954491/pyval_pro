#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""
import time
from setproctitle import setproctitle
import os
import pyval_safe
from multiprocessing import Process
import sys
DELAI_SEC = 5.0


def main() -> None:
    """Fonction principale"""
    setproctitle(f"XG main {DELAI_SEC}")
    try:
        ps_eval = Process(target=eval_ini)
        ps_eval.start()
        ps_dot = Process(target=print_forever, args=('.', 0.1))
        ps_dot.start()

        print('délai', DELAI_SEC,
              '__', 'main:', os.getpid(),
              '__', 'ps_eval', ps_eval.pid,
              '__', 'ps_dot:', ps_dot.pid)
        os.system(f"pstree -U {os.getpid()} | grep --color=always \\\\w ")
        ps_eval.join(DELAI_SEC)
        ps_dot.terminate()

        if ps_eval.is_alive():
            ps_eval.terminate()
            raise TimeoutError(f"le délai de {DELAI_SEC} secondes est écouler")
    except Exception as ex:
        print()
        pyval_safe.exexit(ex)
    except KeyboardInterrupt:
        sys.exit(1)


def eval_ini() -> None:
    """rederct ver pyval_safe.main"""
    setproctitle(f"eval {' '.join(sys.argv[1:])}")
    pyval_safe.main()


def print_forever(ceci: str, delai_sec: float) -> None:
    """Afficher répétitivement quelqu chose, sans arrêt"""
    setproctitle(f"print {ceci} {delai_sec}")
    try:
        while True:
            time.sleep(delai_sec)
            print(ceci, end='', flush=True)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
