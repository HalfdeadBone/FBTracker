from colorama import Fore, Back, Style


def ErrorMsg(*args):
    temp = '['+ Back.RED + Fore.WHITE + 'ERROR' + Fore.RESET + Back.RESET +']\t    ' + ' '.join(args)
    return temp

def SuccessMsg(*args):
    temp = '['+ Back.GREEN + Fore.BLACK + 'SUCCESS' + Fore.RESET + Back.RESET +']   ' + ' '.join(args)
    return temp

def InfoMsg(*args):
    temp = '[' + Back.BLUE + Fore.WHITE + 'INFO' + Fore.RESET + Back.RESET +']\t    ' + ' '.join(args)
    return temp

def WarnningMsg(*args):
    temp = '['+ Back.YELLOW + Fore.BLACK + 'WARRNING!' + Fore.RESET + Back.RESET +'] ' + ' '.join(args)
    return temp

def UniqueMsg(*args):
    temp = '[' + Back.CYAN + Fore.WHITE + '???????' + Fore.RESET + Back.RESET +']   ' + ' '.join(args)
    return temp

