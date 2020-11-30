#!/usr/bin/env python3

"""
Programme pour évaluer une expression python
(version non sécurtaire et modulaire)

2020, Xavier Gagnon
"""

from math import * # noqa
from typing import NoReturn
import sys
import colorama
from colorama import Fore
colorama.init()


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rappoert une erreur et termine le programme"""
    print(Fore.YELLOW, "[XG] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def main() -> None:
    """Fonction pricipale"""
    try:
        evaluation = eval(' '.join(sys.argv[1:]) or "None")
        print(Fore.CYAN + "Selon Xavier Gagnon:", Fore.RESET, evaluation)
    except BaseException as ex:
        exexit(ex)


if __name__ == '__main__':
    main()
