#!/usr/bin/env python3

"""
Autheur Xavier Gagnon
"""

import pyval_safe
from multiprocessing import Process
import sys
DELAI_SEC = 2.0


def main() -> None:
    """Fonction principale"""
    try:
        ps = Process(target=pyval_safe.main)
        ps.start()
        ps.join(DELAI_SEC)
        if ps.is_alive():
            ps.terminate()
            raise TimeoutError(f"le délai de {DELAI_SEC} secondes est écouler")
    except Exception as ex:
        pyval_safe.exexit(ex)
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == '__main__':
    main()