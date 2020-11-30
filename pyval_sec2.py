#!/usr/bin/env python3

"""
Programme pour évaluer une expression python
(version sécurtaire et modulaire)

2020, Xavier Gagnon
"""
from typing import NoReturn

from m_timeout_eval import timeout_eval as eval  # noqa
import sys

import colorama
from colorama import Fore

colorama.init()


def main() -> None:
    """Fonction pricipale"""
    try:
        evaluation = eval(' '.join(sys.argv[1:]) or "None", delai_sec=2.0)
        print(Fore.CYAN + "Selon Xavier Gagnon:", Fore.RESET, evaluation)
    except TimeoutError:
        # Pour afficher un message d'erreur personalisé
        exexit(TimeoutError("Le délai de 2 secondes est dépassé."))
    except Exception as ex:
        exexit(ex)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rappoert une erreur et termine le programme"""
    print(Fore.YELLOW, "[XG] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
