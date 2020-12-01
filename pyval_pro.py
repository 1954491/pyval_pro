#!/usr/bin/env python3

"""
Programme pour évaluer une expression python
(version sécuritaire, avec durée limitée, et professionnelle)

2020, Xavier Gagnon
"""
from timeit import default_timer as timer
import argparse
from typing import NoReturn
from m_timeout_eval import timeout_eval as eval  # noqa
import sys
import colorama
from colorama import Fore

colorama.init()

DELAI_PAR_DEFAULT = 2.0


def main() -> None:
    """Fonction principale"""
    debut = timer()
    args = args_parse()
    try:
        delai = args.delai if args.delai is not None else DELAI_PAR_DEFAULT
        if delai > 5:
            raise ValueError("Le délai doit être au plus 5 secondes")
        if delai <= 0:
            raise ValueError("Le délai doit être supéreur à 0")

        evaluation = eval(' '.join(args.code) or "None", delai_sec=delai)
        print(Fore.CYAN + "Selon Xavier Gagnon:", Fore.RESET, evaluation)
    except TimeoutError:
        # Pour afficher un message d'erreur personalisé
        delaiaffichage = args.delai if args.delai else DELAI_PAR_DEFAULT
        delaiaffichage = int(delaiaffichage) if delaiaffichage % 1 == 0 else float(delaiaffichage)
        exexit(TimeoutError(f"Le délai d'exécution de {delaiaffichage} secondes est écoulé."))
    except KeyboardInterrupt:
        exexit(KeyboardInterrupt("Interrompu par l'utilisateur"))
    except Exception as ex:
        exexit(ex)
    finally:
        if args.minute:
            print(Fore.MAGENTA + "Durée:", timer() - debut, "sec", Fore.RESET)


def exexit(ex: BaseException, exit_code: int = 1) -> NoReturn:
    """Rappoert une erreur et termine le programme"""
    print(Fore.YELLOW, "[XG] ",
          Fore.RED, ex.__class__.__name__,
          Fore.YELLOW, ": ", ex,
          file=sys.stderr, sep='')
    sys.exit(exit_code)


def args_parse() -> argparse.Namespace:
    """Fonciton qui récupère les argument de la commande"""
    parser = argparse.ArgumentParser(description="Évaluateur d'expression Python -- ©2020, par Xavier Gagnon")
    parser.add_argument("-d", "--délai", metavar="DÉLAI", dest="delai", help="délai pour le calcul (défaut 2 sec)",
                        default=None, type=float)
    parser.add_argument("-m", "--minuté", action="store_true", dest="minute",
                        help="minuté la durée d'execution")
    parser.add_argument("code", help="Expression à évaluer", nargs='+', type=str)

    return parser.parse_args()


if __name__ == '__main__':
    main()
