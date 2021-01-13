from tkinter import*
from tkinter import filedialog
import os
import module2
from os.path import basename

#creation de la fenetre et ses paramètres
fenetre = Tk()
fenetre.title('publication')
fenetre.geometry('700x500')
fenetre.configure(bg='white') 
chemin1 = ''
chemin2 = ''
chemin3 = ''
chemin4 = ''
chemin1F = ''
chemin2F = ''
chemin3F = ''
chemin4F = ''
testeur = 0

#recupère un fichier 
def openfile1():
    global chemin1
    #Ouverture de la boite de dialogue pour selection du fichier
    rep_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #Récupération du nom complet du fichier avec l'attribut .name du module "os"
    chemin1 = os.path.abspath(rep_file)
    return chemin1

#recupère un fichier
def openfile2():
    global chemin2
    #Ouverture de la boite de dialogue pour selection du fichier
    rep_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #Récupération du nom complet du fichier avec l'attribut .name du module "os"
    chemin2 = os.path.abspath(rep_file)
    return chemin2

#recupère un fichier
def openfile3():
    global chemin3
    #Ouverture de la boite de dialogue pour selection du fichier
    rep_file =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    #Récupération du nom complet du fichier avec l'attribut .name du module "os"
    chemin3 = os.path.abspath(rep_file)
    return chemin3

#recupère un dossier 
def openfile4():
    global chemin4
    chemin4 = filedialog.askdirectory()
    return chemin4

bienvenue=Label(fenetre,text='BIENVENUE DANS VOTRE ESPACE DE PUBLICATION',background='#6be1e3',relief='flat',foreground='white',height=5,width=65,font=('Candara Light', 15))
bienvenue.grid(column=0,row=0,rowspan=2,columnspan=4)
explication=Label(fenetre, text='Veuillez séléctionner vos 3 fichiers csv et le dossier principal',height=5,width=50,font=('5'),bg='white')
explication.grid(column=0,row=3,rowspan=2,columnspan=4)

explication1=Label(fenetre, text='CSV Module',font=('Arial','6'),bg='white')
explication1.grid(column=0,row=5,pady=4)
ouvrir1 = Button(fenetre, text="Ouvrir1", command=openfile1,bg='#aab8b6',foreground='white')
ouvrir1.grid(column=0,row=6)

explication2=Label(fenetre, text='CSV Structure',font=('8'),bg='white')
explication2.grid(column=1,row=5)
ouvrir2 = Button(fenetre, text="Ouvrir2", command=openfile2,bg='#aab8b6')
ouvrir2.grid(column=1,row=6)

explication3=Label(fenetre, text='CSV Description',font=('8'),bg='white')
explication3.grid(column=2,row=5)
ouvrir3 = Button(fenetre, text="Ouvrir3", command=openfile3,bg='#aab8b6')
ouvrir3.grid(column=2,row=6)

explication4=Label(fenetre, text='Dossier principal',bg='white',font=('8'))
explication4.grid(column=3,row=5)
ouvrir4 = Button(fenetre, text="Ouvrir4", command=openfile4,bg='#aab8b6')
ouvrir4.grid(column=3,row=6)

blanc=Label(fenetre,text='                 ',bg='white',height=7,width=8)
blanc.grid(column=1,row=7)

fermer = Button(fenetre, text="Valider", command=fenetre.destroy,activebackground='plum',bd=6,bg='#646c6b',height=3,width=13,font=('Times','12'),cursor='hand1',relief=RIDGE,takefocus='shift-tab')
fermer.grid(column=1,row=8, columnspan=2,rowspan=2)


fenetre.mainloop()


while testeur == 0:
    if chemin1 != '':
        chemin1F = chemin1
        chemin1 = ''
    if chemin2 != '':
        chemin2F = chemin2
        chemin2 = ''
    if chemin3 != '':
        chemin3F = chemin3
        chemin3 = ''
    if chemin4 != '':
        chemin4F = chemin4
        chemin4 = ''
    if chemin1F != '' and chemin2F != '' and chemin3F != '' and chemin4F != '':
        testeur = 1

print('Chemin1', chemin1F)
print('Chemin2', chemin2F)
print('Chemin3', chemin3F)
print('Chemin4', chemin4F)


nom1 = basename(chemin1F)
nom2 = basename(chemin2F)
nom3 = basename(chemin3F)
nom4 = basename(chemin4F)

print(nom1)
print(nom2)
print(nom3)
print(nom4)

module2.uploadfichier(chemin1F, nom1)
module2.uploadfichier(chemin2F, nom2)
module2.uploadfichier(chemin3F, nom3)
module2.uploaddossier(chemin4F, nom4)
