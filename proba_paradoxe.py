import matplotlib.pylab as pl

# Pour des raisons de simplification et de clarté, nous avons opté pour la formule telle quelle sans faire d'approximation!

def calcule_proba(n):
    # n pour le nombre de personnes
    # Nous avons ici d = 365, mais il est possible de généraliser.

    p = 1
    for i in range(1,n):
        p *= (365 - i) / 365
    return 1 -p


def generer_graphe():
    valeurs = list(range(2,101))

    proba = [calcule_proba(n) for n in valeurs]
    pl.figure(figsize=(10,8))
    pl.plot(valeurs, proba)

    pl.xticks(range(0,101,10))
    pl.yticks([i/100 for i in range(0, 101,10)])

    pl.xlabel('Nombre de personnes n')
    pl.ylabel('Probabilité')
    pl.title("Probabilité d'avoir au moins 2 personnes avec la meme date d'anniversaire")
    pl.grid(True)

    # ajout d'une ligne pour monter la probabilité de n = 23
    pl.axvline(x=23, label='n=23', color='green', linestyle="--")
    pl.legend()

    pl.show()

if __name__ == "__main__":

    # affichage la probabilité pour un n entre 2 et 100 personnes
    for n in range(2,101):
        print(f'Pour {n} personnes, la probabilité d avoir au moins 2 personnes avec la meme date est: {calcule_proba(n):.3f}')

    # gnénération du graphe
    generer_graphe()


