#!/usr/bin/env python3

"""
Programme pour évaluer une expression python
(version sécurtaire et modulaire)

2020, Xavier Gagnon
"""
from typing import NoReturn

from m_safe_eval import safe_eval as eval  # noqa
import sys

import colorama
from colorama import Fore

colorama.init()


def main() -> None:
    """Fonction pricipale"""
    try:
        evaluation = eval(' '.join(sys.argv[1:]) or "None")
        print(Fore.CYAN + "Selon Xavier Gagnon:", Fore.RESET, evaluation)
    except BaseException as ex:
        exexit(ex)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rapporte une erreur et termine le programme"""
    print(Fore.YELLOW, "[XG] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
