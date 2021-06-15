# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.

Flavien Galbez TD J
"""

transactions = [
                    {1, 2, 5}, 
                    {1, 3 ,5},
                    {1, 2},
                    {1, 2, 3, 4, 5},
                    {1, 2, 4, 5},
                    {2, 3, 5},
                    {1, 5},
                ]
                    
def Apriori (transactions, occurences_min):
    
    L=set()
    # création de L1 :
    frequences = {}
    for transa in transactions:
        for valeur in transa : 
            frequences[valeur]=frequences.get(valeur,0)+1 # nous permet d'enregistrer et de compter chaque valeur
    Lk= {frozenset([x]) for x in frequences if frequences[x] >= occurences_min} # On selectionne seulement les valeurs d'occurences >= occurences_min pour construire L1
    L.update(Lk) # On rajoute L1 à L
    
    #creation de Lk+1 :
    while len(Lk)>0 :
        
        # Construction de Ck+1 :
        Ck = set()
        for a in Lk:
            for b in Lk:
                if(len(a & b) == (len(a) - 1)): #si l'intersection de a et b = à la taille de a - 1 alors ils ont une unique valeur de différence
                        Ck.add(frozenset(a | b)) #On rajoute à Ck l'union des deux ensembles (il s'agit un ensemble de taille de a + 1)
        
        #Construction de Lk+1 :
        frequences = {}
        for transa in transactions:
            D = {c for c in Ck if c <= transa}
            for d in D:
                frequences[d] = frequences.get(d, 0) + 1
            Lk = {x for x in frequences if frequences[x] >= occurences_min}
        L.update(Lk) #On rajoute Lk à L
    return L

print (Apriori(transactions, 3))
            