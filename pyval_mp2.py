#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""

import pyval_safe
from multiprocessing import Process
import sys
DELAI_SEC = 5.0


def main() -> None:
    """Fonction principale"""
    try:
        p = Process(target=pyval_safe.main)
        p.start()

        increment = 0.1
        temps = 0.0

        while p.is_alive() and temps < DELAI_SEC:
            if temps > 0.2:
                print('.', end='', flush=True)
            p.join(increment)
            temps += increment
        if p.is_alive():
            p.terminate()
            raise TimeoutError(f"le délai de {DELAI_SEC} secondes est écouler")
    except Exception as ex:
        print()
        pyval_safe.exexit(ex)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()
