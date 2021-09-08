#fonction qui affiche la suite de fibanochi a 'n' entier
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    return

#plusieurs maniere d'afficher les la sortie de la fonction en terminal
#methode 1
#fib(10)
#methode 2
print(fib(10))