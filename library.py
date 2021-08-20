import pygame.mixer
from tinytag import TinyTag
import os.path
import os
import time

pygame.mixer.init()


def newlibrarie(name):        #installe la bibliothèque de sons correspondant (internet) hors dict
    path, file = os.path.split(os.path.abspath(__file__))
    with open(path+r"\library\libraries.txt","a") as libfile:
        libfile.write(name+",")
    os.system("powershell -c curl https://github.com//Scrpi0/SoundBoard/raw/main/library/"+name+"/listaudio.txt -o "+path+r"\UpDate\listaudio.txt")
    time.sleep(3)
    with open(path+r"\UpDate\listaudio.txt","r") as currentfile:
        list=currentfile.readline().split(",")
        list.pop()
    for filesurladress in list:
        filesadress=""
        for letter in filesurladress:
            if letter == "/":
                filesadress+="\\"
            else:
                filesadress+=letter
        if not os.path.isdir(path+"\\library\\"+name+"\\"+filesadress.split("\\")[0]):
            os.system("mkdir "+path+"\\library\\"+name+"\\"+filesadress.split("\\")[0])
        os.system("powershell -c curl 'https://github.com/Scrpi0/SoundBoard/raw/main/library/"+name+"/"+filesurladress+"' -o '"+path+"\\library\\"+name+"\\"+filesadress+"'")
        print("téléchargement ",path+"\\library\\"+name+"\\"+filesadress)



def checklibraries():        #test la presence et la non-presence des dossiers
    path, file = os.path.split(os.path.abspath(__file__))
    print(path)
    missing_folders=[]
    checked_folders=[]
    with open(path+r"library\libraries.txt","r") as libfile:
        list=libfile.readline().split(",")
        list.pop()
    li=os.listdir(path)
    for dir in list:
        if dir in li:
            #ici devrait être une fonction qui check la prescence des fihiers audios et des sous dossiers correspondants
            checked_folders.append(dir)
        else:
            missing_folders.append(dir)

    return missing_folders, checked_folders


def checklibrariesfiles(path=os.path.split(os.path.abspath(__file__))[0]):
    print("ici sera le code")


def initialisation_data_sounds(cat):   #charge tous les fichiers audios d'une catégorie (hors dict)
    path,file = os.path.split(os.path.realpath(__file__))
    path+=cat
    soundfiles=[]
    soundlist=os.listdir(path)
    soundlistb=[]

    for el in soundlist:     #conserve les noms sans extensions (les dossiers)
        if "." in el:
            soundlistb.append(el)
    for el2 in soundlistb:
        soundlist.remove(el2)

    for el3 in soundlist:   #boucle pour récupérer les noms dans chacun des sous dossiers
        soundlist2=os.listdir(path+"\\"+el3)
        soundlist2b=[]

        for el4 in soundlist2:  # suprime les noms sans extensions .wav
            if ".wav" not in el4:
                soundlist2b.append(el4)
        for el5 in soundlist2b:
            soundlist2.remove(el5)

        for el6 in soundlist2:   #ajoute les tuples contenant l'audio + infos
            tagel6=TinyTag.get(path+"\\"+el3+"\\"+el6)
            soundfiles.append((pygame.mixer.Sound(path+"\\"+el3+"\\"+el6),el6,tagel6.artist,tagel6.title,tagel6.album,tagel6.duration))
    return soundfiles

