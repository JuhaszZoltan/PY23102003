def feladat01() -> None:
    x:int = int(input('x értéke: '))
    y:int = int(input('y értéke: '))
    print(f'abszolút különbség: {abs(x - y)}')


def feladat02() -> None:
    a:int = int(input('a értéke: '))
    b:int = int(input('b értéke: '))
    c:int = int(input('c értéke: '))
    if a+b>c and a+c>b and b+c>a: print('szerkeszthető')
    else: print('nem szerkeszthető')


def feladat03() -> None:
    nev:str = input('írd be a neved: ')
    for k in nev: print(k)


def feladat04() -> None:
    valami:str = input('írj be valamit: ')
    print((len(valami)+2) * '*')
    print(f'*{valami}*')
    print((len(valami)+2) * '*')