from tkinter import *
from random import*

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Définition de la fenêtre

root = Tk()
root.title("Affichage d'images")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

canvas = Canvas(root, width=675, height=300, bg="white")
canvas.grid(row=0, column=0, columnspan=2, sticky="nsew")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Définition des variables

liste_images = ['LaJoconde.png', 'LeCri.png', 'LaNuitEtoilee.png','SaturneDevorantUnDeSesFils.png','PelerinsAllantALaMecque.png','LaJeuneFilleALaPerle.png','AmericanGothic.png','Guernica.png','ImpressionSoleilLevant.png','LaNaissanceDeVenus.png','LaTristesseDuRoi.png','Le Baiser.png']
liste_Nom = ['De Vinci', 'Munch', 'Gogh','De Goya','Belly','Vermeer','Wood','Picasso','Monet','Botticelli','Matisse','Klimt']
liste_Oeuvre = ['La Joconde', 'Le Cri', 'La Nuit Etoilée','Saturne Dévorant un de ses Fils','Pelerins Allant à la Mecque','La Jeune Fille à la Perle','American Gothic','Guernica','Impression, Soleil Levant','La Naissance de Vénus','La Tristesse du Roi','Le Baiser']

radioValue = IntVar()
saisie = StringVar()  # Déclarez saisie en tant que variable de chaîne
indice = randint(0,len(liste_images)-1)
indice0 = indice
f = ''


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Définition des fonctions

def afficher_image_suivante():
    '''Cette fonction permet d'afficher une image différente de celle déjà visible
    assert len(liste_image)>0'''
    global saisie, indice, indice0, f, liste_images, fichier_image
    while indice == indice0 :
        indice = randint(0, len(liste_images)-1)
    indice0 = indice
    f = liste_images[indice]
    fichier_image = PhotoImage(file=f)
    canvas.create_image(25, 50, image=fichier_image, anchor=NW)
    texterep['text'] = ''
    return indice


def Verrif():
    '''Cette fonction permet de Verrifier si le résultat que le joueur a donné est bien la bonne réponse en fonction de si il a voulu donner le nom de l'artiste
    ou le nom de l'oeuvre'''
    ValeurRadio = radioValue.get()
    if ValeurRadio == 0:
        texterep['text'] = "Appuyer sur un bouton radio"
        raise("Appuyer sur un bouton radio")
    if ValeurRadio == 1:
        texte_saisi = saisie.get()
        if texte_saisi == liste_Nom[indice]:
            texterep['text'] = "Réponse Vraie : " + texte_saisi
        else:
            texterep['text'] = "Réponse Fausse : c'était :" + liste_Nom[indice]
    if ValeurRadio==2:
        texte_saisi = saisie.get()
        if texte_saisi == liste_Oeuvre[indice]:
            texterep['text'] = "Réponse Vraie : " + texte_saisi
        else:
            texterep['text'] = "Réponse Fausse : c'était :" + liste_Oeuvre[indice]


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Définition des bouttons

fichier_image = PhotoImage(file=liste_images[indice])
canvas.create_image(25, 50, image=fichier_image, anchor=NW)

afficher_image_suivante_boutton = Button(root, text="Image suivante", command=afficher_image_suivante, width=20, height=2)
afficher_image_suivante_boutton.grid(row=1, column=0, columnspan=2, pady=10)

Radioboutton_arsiste = Radiobutton(root, text="Artiste", width=20, variable=radioValue, value=1)
Radioboutton_arsiste.place(x=400, y=5)

Radioboutton_titre = Radiobutton(root, text="Titre", width=20, variable=radioValue, value=2)
Radioboutton_titre.place(x=400, y=35)

texte = Label(root, text="Entrer votre réponse : ")
texte.place(x=400, y=70)

entree = Entry(root, textvariable=saisie)
entree.place(x=400, y=100)

boutontexte = Button(root, text="Entrée", width=20, command=Verrif)
boutontexte.place(x=400, y=130)

texterep = Label(root, text="")
texterep.place(x=400, y=160)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

root.mainloop()