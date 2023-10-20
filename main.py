from module import *

# szavak:list[str] = ['cica', 'kutya', 'bicikli', 'krikettütő']
# for szo in szavak: print(keretez(szo)+'\n')

a:int = szam_bekeres('a')
b:int = szam_bekeres('b')
c:int = szam_bekeres('c')
if szerkesztheto_e(a, b, c): print('szerkeszthető')
else: print('nem szerkeszthető')