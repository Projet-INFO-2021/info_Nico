import ftplib
import os.path, os
ftp = ftplib.FTP('127.0.0.1', 'Nico', 'projetinfo')     #connexion au serveur ftp (adresseIP, User, mdp)
                                



def existerepftp(ftp, cheminftp):
    """dit si un chemin ftp est un répertoire existant (True) ou non (False)
    """
    repcourantftp = ftp.pwd()
    try:
        ftp.cwd(cheminftp) # tentative de changement de répertoire
        ftp.cwd(repcourantftp) # si ok, revenir au répertoire courant
        return True
    except ftplib.error_perm:
        return False

def uploadrepftp(ftp, repertloc, repertftp, affiche=False):
    """uploade sur FTP les fichiers du répertoire et de ses sous-répertoires
       - ftp: connecteur sur une connexion FTP ouverte
       - repertloc: répertoire local disque (sans '\' ni '/' à la fin)
       - repertftp: répertoire existant sur serveur FTP (sans '/' à la fin)
       - affiche: si True, affiche les fichiers téléchargés
       retourne la liste des fichiers téléchargés avec leur chemin disque
    """
    # rend absolu le chemin disque (s'il n'y est pas déjà)
    repertloc = os.path.abspath(os.path.expanduser(repertloc))
 
    # ajoute le nom du répertoire à copier au répertoire FTP
    repertftp = repertftp + '/' + os.path.basename(repertloc)
    # crée le nouveau répertoire FTP s'il n'existe pas encore
    if not existerepftp(ftp, repertftp):
        if affiche:
            print("Crée le nouveau répertoire FTP:", repertftp)
        ftp.mkd(repertftp) 
 
    fichiers = []
    # navigation récursive dans l'arborescence du répertoire local
    for repert, sreps, fics in os.walk(repertloc):
        # construit le chemin du nouveau répertoire sur FTP
        repftp = repertftp + repert[len(repertloc):].replace('\\', '/')
        # crée le nouveau répertoire sur FTP s'il n'existe pas encore
        if not existerepftp(ftp, repftp):
            if affiche:
                print("Crée le nouveau répertoire FTP:", repftp)
            ftp.mkd(repftp) 
        # upload des fichiers de ce nouveau répertoire
        for fic in fics:
            fichierloc = os.path.join(repert, fic)
            # construit le chemin destination sur FTP
            fichierftp = repftp + "/" + fic
            # télécharge le fichier local sur le serveur FTP
            with open(fichierloc, "rb") as fs:
                if affiche:
                    print("télécharge le fichier:", fichierloc)
                ftp.storbinary("STOR " + fichierftp, fs)
 
            # ajoute le fichier local téléchargé avec son chemin
            fichiers.append(fichierloc)
    # retourne la liste de tous les fichiers téléchargés
    return fichiers



def uploaddossier(chemin,nomfichier):

    cheminF = chemin.replace('/','//')
    print(cheminF)
    ftp.mkd(nomfichier) 
    repertloc = cheminF
    repertftp = nomfichier # ce répertoire doit déjà exister. 
    fichiers = uploadrepftp(ftp, repertloc, repertftp, True)

    


def uploadfichier(chemin, nomfichier):
    fichier = nomfichier
    file = open(chemin, 'rb')
    ftp.storbinary('STOR ' + fichier, file)