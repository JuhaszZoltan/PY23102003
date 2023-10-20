def keretez(szo:str) -> str:
    keretezett:str = ''
    keretezett += (len(szo)+2) * '*'
    keretezett += f'\n*{szo}*\n'
    keretezett += (len(szo)+2) * '*'
    return keretezett


def szerkesztheto_e(a:float, b:float, c:float) -> bool:
    return a+b>c and a+c>b and c+b>a


def szam_bekeres(valtozo_nev:str) -> int:
    atalakitando = input(f'{valtozo_nev} értéke: ')
    return int(atalakitando)