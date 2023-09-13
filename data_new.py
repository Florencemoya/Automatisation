
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def data_new(data):
    
     # Supprimer les lignes contenant des valeurs manquantes (None)
    data = data.dropna()
    
    noms_variables_liste = data.columns.tolist()
    liste1=['DT_quadsupg','DT_quadinfg']
    liste2=['DT_quadsupd','DT_quadinfd']
    liste3=['DT_dis_quadsupg','DT_dis_quadinfg']
    liste4=['DT_dis_quadsupd','DT_dis_quadinfd']
    liste5=['DT_quadsupg','DT_quadinfg','DT_quadsupd','DT_quadinfd']
    liste6=['DT_dis_quadsupg','DT_dis_quadinfg','DT_dis_quadsupd','DT_dis_quadinfd']
    
    if all(element in  noms_variables_liste for element in liste1)==True:
        data['DT_gauche'] = data['DT_quadsupg'] + data['DT_quadinfg']
        #data = pd.concat([data, pd.Series(data['DT_gauche'], name='DT_gauche')], axis=1)
    else:
        print('impossible')
        
    if all(element in  noms_variables_liste for element in liste2)==True:
        data['DT_droite'] = data['DT_quadsupd'] + data['DT_quadinfd']
        #data = pd.concat([data, pd.Series(data['DT_droite'], name='DT_droite')], axis=1)
    else:
        print('impossible')
        
    if all(element in  noms_variables_liste for element in liste3)==True:
        data['DT_dis_gauche'] = data['DT_dis_quadsupg'] + data['DT_dis_quadinfg']
        #data = pd.concat([data, pd.Series(data['DT_dis_gauche'], name='DT_dis_gauche')], axis=1)
    else:
        print('impossible')
        
    if all(element in  noms_variables_liste for element in liste4)==True:
        data['DT_dis_droite'] = data['DT_dis_quadsupd'] + data['DT_dis_quadinfd']
        #data = pd.concat([data, pd.Series(data['DT_dis_droite'], name='DT_dis_droite')], axis=1)
    else:
        print('impossible')
        
    if all(element in  noms_variables_liste for element in liste5)==True:
        data['DT_laterales'] = data['DT_quadsupg'] + data['DT_quadinfg'] + data['DT_quadsupd']+ data['DT_quadinfd']
        #data = pd.concat([data, pd.Series(data['DT_laterales'], name='DT_laterales')], axis=1)
    else:
        print('impossible')
        
    if all(element in  noms_variables_liste for element in liste6)==True:
        data['DT_dis_laterales'] = data['DT_dis_quadsupd'] + data['DT_dis_quadinfd'] + data['DT_dis_quadsupg'] + data['DT_dis_quadinfg']
        #data = pd.concat([data, pd.Series(data['DT_dis_laterales'], name='DT_dis_laterales')], axis=1)
    else:
        print('impossible')
        
        
    # Comparaison et création de nouvelles colonnes
    data['Resultat_DT_laterales'] = np.where(data['DT_laterales'] < 8, 1, 0)
    data['Resultat_DT_dis_laterales'] = np.where(data['DT_dis_laterales'] < 17, 1, 0)
    data['Resultat_ST'] = np.where(data['ST'] < 3, 1, 0)
    data['Resultat_DT_centrale'] = np.where(data['DT_centrale'] < 10, 1, 0)
    data['Resultat_DT_dis_centrale'] = np.where(data['DT_dis_centrale'] < 7, 1, 0)
    
    # selection des variables pour la formation de "combinaison"
    data_restr = data.loc[:,['Resultat_DT_laterales', 'Resultat_DT_dis_laterales','Resultat_ST','Resultat_DT_centrale','Resultat_DT_dis_centrale']]
    
    # Création d'une colonne pour la combinaison des numéros
    data_restr['Combinaison'] = data_restr.apply(lambda row: tuple(row), axis=1)
    
    # Création d'un dictionnaire pour stocker les combinaisons uniques et les chiffres attribués
    dictionnaire_combinaisons = {
    (0, 0, 0, 0, 0): 0,
    (1, 1, 1, 1, 1, 1): 1
    }

# Parcourir les lignes du dataframe
    for index, row in data_restr.iterrows():
        combinaison = row['Combinaison']
    
        # Vérifier si la combinaison existe déjà dans le dictionnaire
        if combinaison in dictionnaire_combinaisons:
            # Si oui, attribuer le chiffre existant
            chiffre_attribue = dictionnaire_combinaisons[combinaison]
        else:
            if combinaison == (1, 1, 1, 1, 1):
                chiffre_attribue = 32
            elif combinaison == (0, 0, 0, 0, 0):
                chiffre_attribue = 0
            else:
                chiffre_attribue = 0
                for i, num in enumerate(combinaison[::-1]):
                    if num == 0:
                        chiffre_attribue += 2 ** i
        
            dictionnaire_combinaisons[combinaison] = chiffre_attribue
    
        # Mettre à jour la colonne 'Valeur_attribuée' du dataframe
        data_restr.at[index, 'Valeur_attribuée'] = chiffre_attribue

# Affichage du dataframe avec les combinaisons et les valeurs attribuées

    data['Combinaison'] = data_restr['Combinaison']
    data['Valeur_attribuée'] = data_restr['Valeur_attribuée']

    return data
    