def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 883 
    q = 420081950226850128248692851991601350080273340164506171827655619205207262970152510180348796505124767464242665020800947927733394952113269891642345810494634814313973093980673242569260034672614354104148733853237542522594850741968784204772768475971691615704355550292807697820390238429368224361672628906376706504645993816869176491478803946508268705042284404422885468879649180114992922463905571594234244653778444803477900403550657045468554957572843198803229672812265922068202650970235811595521876015559005484806054477208351212429806816305371322777162133306362631876104005617 
    e = 3
    ct = 2205316413931134031046440767620541984801091216351222789180593875373829950860542792110364325728088504479780803714561464250589795961097670884274813261496112882580892020487261058118157619586156815531561455215290361274334977137261636930849125

    # compute n
    n = p * q
    print n

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a
    d = d % phi
    if (d < 0):
        d += phi

    print( "d:  " + str(d) )

    # pt =int(pow(ct, d, n))
  #  pt = pow(ct, d, n)
    # print( "flag: " + str(pt) )

if __name__ == "__main__":
     main()