#
#
# Importations :

from copy import *

from pylab import *
from numpy import *

import time

# Fin des importations.
#
#
### Fonction d'affichage :

def AfficheSauv ( TableB , adresse, affiche, N ) :
        """ Affiche un nuage de points qui traduit les concentrations donnees par le tableau
        @param : une liste TableB de listes de nombres positifs, et l'adresse adresseFichier
        @result : affiche le nuage de points correspondant apres avoir efface l'ancien et l'enregistre si adresseFichier n'est pas ''  """

        X=[]
        Y=[]
        SizeB=[]
        
        for i in range (len(TableB)):
                
                for j in range (len(TableB[i])):
                        
                        Y=Y+[i]
                        X=X+[j]
                        if  TableB[i][j] >= 0 :
                                SizeB = SizeB + [  TableB[i][j]  ]
                        else :
                                SizeB = SizeB + [0]
        
        
        
        clf()  ## Efface l'acien nuage de points.
        
        
        scatter(X,Y, SizeB)  ## Cree le nuage de points, Size indique la taille de chaque point.

        adresse = adresse + str(N)
        
        savefig( adresse, dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None)
        
        if affiche == True :
                show()

        return 1

### Fin affichage.
#
#
#
#
#
### Autres Fonctions :



### Fin des Autres Fonctions.
#
#
#
#
#
#
#
#
#
#
#
#
#### Programme Principal :

print("")
print("--#--#--   Projet d'informatique  --#--#--")
print("")
print("--#--#--   Taches de Turing  --#--#--")
print("")
print("Saisissez l'adresse du fichier de sauvegarde")
print("( saisir N pour sauvegarder dans D:\ProjetInfo\\ ) :")

Demande1 = input("")

if Demande1 == 'N' :
        adresse = 'D:\ProjetInfo\\'   # Adresse d'enregistrement des images
else :
        adresse = Demande1


longTableX = 100   # Longueur des tableaux de valeurs
longTableY = 100   # Hauteur des tableaux de valeurs



# Creation du tableau de valeurs (et première initialisation).

TableA = []
TableB = []
TableTempA = []

TableTempB = []

for i in range (0, longTableX, 1):
	TableTempA=TableTempA+[1]
	TableTempB=TableTempB+[0]

for i in range (0, longTableY, 1):
	TableA=TableA+[TableTempA[:] ]
	TableB=TableB+[TableTempB[:] ]



#   Fin de creation du tableau de valeurs.


TableB[50][50]=1
#TableB[50][51]=1
#TableB[51][50]=1
#TableB[51][51]=1

TableB[40][70]=1
TableB[40][10]=1
TableB[80][30]=1
TableB[10][90]=1


AfficheSauv( TableB, adresse, 'False', 0 )

TableA2 = deepcopy(TableA) # Ces 2 tableaux correspondent aux tableaux a l'instant t+dt
TableB2 = deepcopy(TableB)


### Caracteristiques chimiques :

DispersionA = 0.2097
DispersionB = 0.105

F= 0.03
k= 0.057

###

Netape = 0


while 1==1:
        
        
        # TotalA=0
        
        for i in range (longTableY):
                
                for j in range (longTableX):
                        
                                if i == 0 :
                                        imoins1 = longTableY-1
                                else :
                                        imoins1 = i-1
                                
                                
                                
                                if i == longTableY-1 :
                                        iplus1 = 0
                                else :
                                        iplus1 = i+1
                                if j == 0 :
                                        jmoins1 = longTableX-1
                                else :
                                        jmoins1 = j-1
                                
                                if j == longTableX-1 :
                                        jplus1 = 0
                                else :
                                        jplus1 = j+1
                                 

                                # Dispersion de A :
                                TableA2[i][j] = TableA[i][j] + DispersionA * ( (  TableA[iplus1][j] + TableA[imoins1][j]  -  (2 * TableA[i][j])  )  +  (  TableA[i][jplus1] + TableA[i][jmoins1]  -  (2 * TableA[i][j])  ) )  /   4
                                        
                                # Explication de  " / 4 " : compense le fait qu'on multiplie la quantité totale par 2 (avec le calcul de la dispersion selon X) et par 2 (avec le calcul de la dispersion selon Y).
                                        
                                # Evolution chimique de la concentration de A :
                                TableA2[i][j] = TableA2[i][j] -  TableA[i][j] * (TableB[i][j])*(TableB[i][j])  +   F * (1- TableA[i][j] )
                                        
                                        
                                        
                                        
                                        
                                # Dispersion de B :
                                TableB2[i][j] = TableB[i][j] +    DispersionB * ( (  TableB[iplus1][j] + TableB[imoins1][j]  -  (2 * TableB[i][j])  )  +  (  TableB[i][jplus1] + TableB[i][jmoins1]  -  (2 * TableB[i][j])  ) )  /   4                 ## A Completer
                                
                                # Evolution chimique de la concentration de B :
                                TableB2[i][j] = TableB2[i][j] +   TableA[i][j] * (TableB[i][j])*(TableB[i][j])  -  (F+k) * TableB[i][j]

                                # A priori, B est l'espece inhibitrice.


                                
                                if TableA2[i][j] < 0.0000000000001 :
                                        TableA2[i][j] = 0

                                if TableA2[i][j] > 10 :
                                        TableA2[i][j] = 10
                                
                                # TotalA = TotalA+TableA[i][j]
                                
                                if TableB2[i][j] < 0.0000000000001 :
                                        TableB2[i][j] = 0
                                
                                if TableB2[i][j] > 10 :
                                        TableB2[i][j] = 10
        
        
        Netape = Netape + 1

        
        # print(TotalA) # Permet de vérifier que la quantite sur tout le plan est conservee (dans le cas ou on a seulement la dispersion).
        
        TableA=deepcopy(TableA2)
        TableB=deepcopy(TableB2)
        
        
        if Netape % 5000 == 0 :
                AfficheSauv(TableB, adresse, True, Netape)

        if Netape % 50 == 0 :
                print("nombre d'etapes realisées : ")
                print(Netape)
                AfficheSauv(TableB, adresse, False, Netape)
                
                
