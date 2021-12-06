#!/usr/bin/env python
# -*- coding: utf-8 -*-


# AGOPIAN Paul
# RODRIGUEZ Clément

#################################################  BIENVENUE DANS MUSICSTUDIO - LOGICIEL D'EDITION MUSICALE   #######################################

# Pour toutes explications, se référer au Mode d'emploi 


################ IMPORTATION DES MODULES ##################

import fluidsynth                   # Module permettant de gérer le son
from tkinter import*                # Module permettant de gérer la partie graphique
import time                         # Module permettant de gérer le temps
import numpy as np                  # Module nécessaire à la création de matrices

    
##################  INITIALISATION FLUIDSYNTH ################


time.sleep(0.2)

# Variable indiquant le nombre d'instruments chargés
nb_instru=0

# Création d'une liste qui comportera des objets fluidsynth.Synth() nécessaires à l'écoute des instruments
fs=[]

# On ajoute des éléments à la liste fs auxquels on applique la méthode Synth()
fs.append(fluidsynth.Synth())
fs.append(fluidsynth.Synth())
fs.append(fluidsynth.Synth())
fs.append(fluidsynth.Synth())
fs.append(fluidsynth.Synth())



############### FENETRE PRINCIPALE  ######################

# On crée une méthode qui va gérer le dimensionnement de la fenetre principale

class FullScreenApp(object):
    #On initialise la taille de la fenetre. En cas de clic sur Echap, on exécute la fonction toggle_geom.
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            

    # Cette fonction permet de redimensionner la fenetre.
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


# On créé un objet fenetre à partir de la Classe Tk()
fenetre=Tk()

#On lui applique la méthode définie ci-dessus
app=FullScreenApp(fenetre)

# On lui donne un titre
fenetre.title("MusicStudio")



####################  MENU HAUT  ##############################

# Ce menu en haut de la fenetre est purement esthétique car manque de temps (hormis le bouton Quitter)

def Reverb():
    print('Reverb non disponible, nos équipes y travaillent !')

def Equalizer():
    print('Equalizer non disponible, nos équipes y travaillent !')
def Limiter():
    print('Limiter non disponible, nos équipes y travaillent !')


def enregistrer():
    print('')
def ouvrir():
    print('')
def convertir():
    print('')

def aide():
    print('')

# Pour créer le menu supérieur, on crée des objets avec la classe Menu()
# On assigne à ces objets différentes méthodes.

menubar = Menu(fenetre)                                            

menu1 = Menu(menubar, tearoff=0)                    
menu1.add_command(label="Ouvrir", command=ouvrir)                      
menu1.add_command(label="Enregistrer", command=enregistrer)
menu1.add_command(label="Convertir en fichier audio", command=convertir)
menu1.add_separator()
menu1.add_command(label="Quitter", command=fenetre.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)

menu2.add_command(label="Reverb", command=Reverb)
menu2.add_command(label="Equalizer", command=Equalizer)
menu2.add_command(label="Limiter", command=Limiter)

menubar.add_cascade(label="Effets", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=aide)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)


###################  FRAMES  ##########################


# Les Frames contiendront les boutons, canvas, scales et dessins.
# Pour chaque frame, on créé un objet à l'aide de la classe LabelFrame(). On spécifie le titre, les dimensions.
# Bien entendu, elles sont toutes contenues dans l'objet fenetre.
# On les place avec grid() en indiquant la colonne avec column et la ligne avec row. Ou avec pack() en indiquant le coté dans side.
# grid_propagate(False) permet d'étaler la frame même si on y positionne un widget comme un bouton.

fenetre['bg']='white'

lf1 = LabelFrame(fenetre, text="Liste d'instruments",height=450,width=668)
lf1.grid(row=1,column=3)
lf1.grid_propagate(False)

lf2 = LabelFrame(fenetre, text="Menu",height=450,width=250)
lf2.grid(row=1,sticky='nw',ipady=0)
lf2.grid_propagate(False)

lf3 = LabelFrame(fenetre, text="Partition",height=450,width=1000)
lf3.grid(row=1,column=2)
lf3.grid_propagate(False)

lf4 = LabelFrame(fenetre, text="Editeur", height=100,width=1920)
lf4.grid(row=2,sticky='ew',columnspan=4)

lf5 = LabelFrame(lf4,height=450,width=250)
lf5.pack(side=LEFT)

lf6 = LabelFrame(fenetre,height=120,width=1920)
lf6.grid(row=3,columnspan=4)
lf6.grid_propagate(False)


##################### Liste d'instru (dans lf1)######################


# Voici la liste des instruments. 
# Lorsqu'on clique sur le bouton, l'instrument correspondant se charge grâce à sa fonction qui lui est propre.
# On a mis une condition sur le nombre d'instruments chargés, car le système ralentit fortement au bout de 4 instruments chargés

#--------------------PIANO

def chargepiano():
    
    global nb_instru
    if nb_instru<3:                                             
        fs[0].start(driver='alsa', midi_driver='alsa_seq')      # Avec la méthode start() on lance le serveur son alsa pour l'instrument
        pia_charge = fs[0].sfload("piano.sf2")                  # On charge le fichier sf2 qui contient les données du son et on l'attribue à l'instrument dans la case correspondante de la liste fs.
        fs[0].program_select(0,pia_charge, 0, 0)                # On sélectionne le programme (ce sera toujours le deuxième)
        butpiano.config(state = DISABLED)                       # Le bouton est grisé
        nb_instru+=1
    else:
        print('Plus de 3 instruments font ralentir le système !')
        
# Pour créer un bouton, on créer un objet avec la classe Button.
# On indique où on le place (ici lf1).
# On indique après command= la fonction à exécuter en cas de clic sur le bouton.

butpiano=Button(lf1, text='Piano', bg='gray80', command= chargepiano)
butpiano.grid(ipadx=10,ipady=10)

#------------ORGUE

def chargeorgan():

    global nb_instru
    if nb_instru<3:
        fs[1].start(driver='alsa', midi_driver='alsa_seq')
        org_charge = fs[1].sfload("organ.sf2")
        fs[1].program_select(0,org_charge, 0, 0)
        butorgan.config(state = DISABLED)
        nb_instru+=1
    else:
        print('Plus de 3 instruments font ralentir le système !')
butorgan=Button(lf1, text='Organ', bg='gray80', command=chargeorgan)
butorgan.grid(ipadx=10,ipady=10)

#----------DRUMS

def chargedrums():

    global nb_instru
    if nb_instru<3:
        fs[2].start(driver='alsa', midi_driver='alsa_seq')
        dru_charge = fs[2].sfload("drums_perc.sf2")
        fs[2].program_select(0,dru_charge, 0, 0)
        butdrums.config(state = DISABLED)
        nb_instru+=1
    else:
        print('Plus de 3 instruments font ralentir le système !')
butdrums=Button(lf1, text='Drums', bg='gray80', command=chargedrums)
butdrums.grid(ipadx=10,ipady=10)

#----------------BASS

def chargebass():

    global nb_instru
    if nb_instru<3:
        fs[3].start(driver='alsa', midi_driver='alsa_seq')
        bass_charge = fs[3].sfload("Squierbass.sf2")
        fs[3].program_select(0,bass_charge, 0, 0)
        butbass.config(state = DISABLED)
        nb_instru+=1
    else:
        print('Plus de 3 instruments font ralentir le système !')
butbass=Button(lf1, text='Bass', bg='gray80', command=chargebass)
butbass.grid(ipadx=10,ipady=10)

#-------------------TRUMPET

def chargetrumpet():

    global nb_instru
    if nb_instru<3:
        fs[4].start(driver='alsa', midi_driver='alsa_seq')
        tru_charge = fs[4].sfload("trumpet.sf2")
        fs[4].program_select(0,tru_charge, 0, 0)
        buttrumpet.config(state = DISABLED)
        nb_instru+=1
    else:
        print('Plus de 3 instruments font ralentir le système !')
buttrumpet=Button(lf1, text='Trumpet', bg='gray80', command=chargetrumpet)
buttrumpet.grid(ipadx=10,ipady=10)



# On va maintenant créer 5 canvas pour indiquer l'emplacement des pistes propres à chaque instrument

canpiano = Canvas(lf2, width=240, height=85, background='Cyan')
txt = canpiano.create_text(100, 43, text="Piano", font="Arial 16", fill="black")
canpiano.grid()

canorgan = Canvas(lf2, width=240, height=85, background='Red')
txt = canorgan.create_text(100, 43, text="Organ", font="Arial 16", fill="black")
canorgan.grid()

candrums = Canvas(lf2, width=240, height=85, background='Green')
txt = candrums.create_text(100, 43, text="Drums", font="Arial 16", fill="black")
candrums.grid()

canbass = Canvas(lf2, width=240, height=85, background='Yellow')
txt = canbass.create_text(100, 43, text="Bass", font="Arial 16", fill="black")
canbass.grid()

cantrumpet = Canvas(lf2, width=240, height=85, background='Purple')
txt = cantrumpet.create_text(100, 43, text="Trumpet", font="Arial 16", fill="black")
cantrumpet.grid()



###########################   EDITEUR   ##################



# On va créer une grille de 64x64 case (même si on apercevra une grille 64x24).
nbcase=64

# Le coté d'une case sera de 17 pixels.
case=17

#def des variables contenant la durée d'une note. Le tempo de base est pris à 100bpm (100 battements par minutes)
# Donc la durée d'une noire (la durée de note unitaire) doit être de 0.6s. Ainsi:
double=0.15   #en seconde
croche=0.3
noire=0.6
blanche=1.2


x0,y0=1,1

last_note=0


# Création du canvas contenant la grille d'édition
canvas = Canvas(lf4, width=1088, height=410, bg="white")
canvas.pack(side=LEFT)

# Initialisation du curseur de lecture pour l'éditeur
curseur1 = canvas.create_line(0, 0, 0, 0)


class Notes:
    "Permet de creer un objet présentant les caractéristiques d'une note via divers attributs (cf def creer_double() )"


fInfos=Toplevel() # Initialisation de la fenetre de dialogue avec la methode Toplevel()


note=np.full(shape=(5,6,24,64),fill_value=0,dtype=object) 


# C'est cette matrice qui comportera les notes. On l'initialise avec des 0.
# Elle est de "dimension" 4. Elle comporte:
# -5 cases pour indiquer l'instrument;
# -6 cases pour indiquer de quel bloc instrument il s'agit
# -24 cases pour indiquer la hauteur de la note
# -64 cases pour indiquer l'emplacement de la note en abscisse
#Les éléments de cette matrice sont de types objets puisque chaque case contenant une note sera une instance de la classe Notes()

                                                        

#-------------------------------------- Fonctions d'attribution des notes 

 
def creer_double(ev,m,l):  # Cette fonction récupère en arguments les coordonnées du clic dans l'éditeur et les coordonnées m et l du bloc de la partition en question (cf partie sur la partition)
    fInfos.destroy()
    global last_note
    last_note=1
    [i,j]=correspond1(ev.x,ev.y) # On récupère les coordonnées dans la grille avec la fonction correspond1
    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+1),y0+case*(i+1),fill='blue') # Apparition d'un rectangle dont les dimensions dependent de la longueur de la note
        
    note[l,m,i,j]=Notes()   # On créé une instance de la classe Notes() pour la case correspondante 
    note[l,m,i,j].h=i       # On crée l'attribut h qui fait référence à la hauteur de la note. La hauteur de la note sera la coordonnée i (ordonnée)
    note[l,m,i,j].p=j       # L'emplacement de la note en abscisse sera j
    note[l,m,i,j].t=double  # La durée de la note (ici double)

def correspond1(x,y):                   # Cette fonction retourne les nouvelles coordonnées en accord avec la taille des cases.
    return [(y-y0)/case,(x-x0)/case]

def creer_croche(ev,m,l):
    fInfos.destroy()
    global last_note
    last_note=2
    [i,j]=correspond2(ev.x,ev.y)

    #if i in range(64) and j in range (64):   # on ne fait rien si le click est hors grille
    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+2),y0+case*(i+1),fill='blue')
    print("clic detecte en case : " + str(i+1) + " et case : " + str(j+1))

    note[l,m,i,j]=Notes()
    note[l,m,i,j].h=i
    note[l,m,i,j].p=j
    note[l,m,i,j].t=croche

    

def correspond2(x,y):
    return [(y-y0)/case,(x-x0)/case]

def creer_noire(ev,m,l):
    fInfos.destroy()
    global last_note
    last_note=3
    [i,j]=correspond3(ev.x,ev.y)
#if i in range(64) and j in range (64):   # on ne fait rien si le click est hors grille
    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+4),y0+case*(i+1),fill='blue')
    print("clic detecte en case : " + str(i+1) + " et case : " + str(j+1))

    note[l,m,i,j]=Notes()
    note[l,m,i,j].h=i
    note[l,m,i,j].p=j
    note[l,m,i,j].t=noire


def correspond3(x,y):
    return [(y-y0)/case,(x-x0)/case]

def creer_blanche(ev,m,l):
    fInfos.destroy()
    global last_note
    last_note=4
    [i,j]=correspond4(ev.x,ev.y)
    #if i in range(64) and j in range (64):   # on ne fait rien si le click est hors grille
    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+8),y0+case*(i+1),fill='blue')
    print("clic detecte en case : " + str(i+1) + " et case : " + str(j+1))

    note[l,m,i,j]=Notes()
    note[l,m,i,j].h=i
    note[l,m,i,j].p=j
    note[l,m,i,j].t=blanche
         
def correspond4(x,y):
    return [(y-y0)/case,(x-x0)/case]



#-----------------------------------------------  Menu contextuel choix durée de la note


# Cette fonction permet de demander à l'utilisateur la durée de la note

def choix_note(event,m,l):
    global last_note
    global cours
    global fInfos
    global choixtab
    cours=1
    fInfos.destroy()            #On fait apparaitre la fenetre de dialogue (d'abord on supprime la précédente, puis on affiche la nouvelle)
    fInfos = Toplevel()
    fInfos.geometry('300x300')      
    fInfos.title("Longueur de la note")
    Button(fInfos, text='Double croche', command= lambda ev=event: creer_double(ev,m,l)).pack(padx=10, pady=10)    
    Button(fInfos, text='Croche', command= lambda ev=event: creer_croche(ev,m,l)).pack(padx=10, pady=10)
    Button(fInfos, text='Noire', command= lambda ev=event: creer_noire(ev,m,l)).pack(padx=10, pady=10)    
    Button(fInfos, text='Blanche', command= lambda ev=event: creer_blanche(ev,m,l)).pack(padx=10, pady=10)

    canvas.bind("<Button-1>", lambda event: dern_note(event,m,l)) # Avec le clic gauche, on peut créer une note de durée égale à cele de la note précédente

    fInfos.transient(canvas)     #affichage au milieu



def dern_note(event,m,l):   
    
    if last_note==1:
        creer_double(event,m,l)
    if last_note==2:
        creer_croche(event,m,l)
    if last_note==3:
        creer_noire(event,m,l)
    if last_note==4:
        creer_blanche(event,m,l)


#####################################  PARTITION  ###################

# Notre partition comportera une grille et des blocs (en cas d'édition de bloc)

hcasep=85                   # Largeur d'une case
lcasep=2*hcasep             #Longueur d'une case
nbcasep=12                  # Nombre de case

# Ces 3 variables permettent de colorer la grille en accord avec le piano rolls (cf partie piano rolls)
scales = 2
white_keys = 7 * scales
black2 = [0,1,0,1,0,1,0,0,1,0,1,0]*2

# On créé un canvas pour la partition
canvas2=Canvas(lf3, width=1000, height=429,bg='white')
canvas2.pack()

instru=int


# On créé la grille de la partition
for i in range(nbcasep):
    canvas2.create_line(x0+lcasep*i, y0,x0+lcasep*i,y0 + nbcasep*hcasep)
    canvas2.create_line(x0, y0+hcasep*i,x0+nbcasep*hcasep ,y0+hcasep*i)



def reinit_ed(m,l):
    #la grille est crée dans l'éditeur à chaque appel de cette fonction
    
    global curseur1
    for i in range (24):
        if black2[i]:
            canvas.create_rectangle(0,case*i,case*nbcase,case*(i+1),fill='gray90')
        else:
            canvas.create_rectangle(0,case*i,case*nbcase,case*(i+1),fill='white')
     
    for i in range(nbcase):
        if i%4==0:
            canvas.create_line(x0+case*i, y0,x0+case*i,y0 + nbcase*case,width=2)

        if i%16!=0:
            canvas.create_line(x0+case*i, y0,x0+case*i,y0 + nbcase*case)
    
        else:
            canvas.create_line(x0+case*i, y0,x0+case*i,y0 + nbcase*case,width=4)

        canvas.create_line(x0, y0+case*i,x0+nbcase*case ,y0+case*i)
    
     # on va afficher les rectangles correspondants aux notes si jamais le bloc a déja été édité.
    for i in range(24):
        for j in range(64):
            if note[l,m,i,j]!=0:
                if note[l,m,i,j].t==double:
                    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+1),y0+case*(i+1),fill='blue')
                if note[l,m,i,j].t==croche:
                    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+2),y0+case*(i+1),fill='blue')
                if note[l,m,i,j].t==noire:
                    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+4),y0+case*(i+1),fill='blue')
                if note[l,m,i,j].t==blanche:
                    canvas.create_rectangle(x0 +case*j,y0+case*i,x0 +case*(j+8),y0+case*(i+1),fill='blue')

    curseur1 = canvas.create_line(0, 0, 0, 410,fill="Red",width=4) # On crée le curseur de lecture du bloc édité




def clic_partition(ev):  

    global instru
    global vol_piano

    
    print('yegf')
    global choixtab
    [l,m]=correspond(ev.y,ev.x)  #cf plus haut

    instru=l
    
    print("clic detecte en case : " + str(l+1) + " et case : " + str(m+1))

    opt_edit(m,l)
    
    #Dès que l'on clique, on exécute la fonction suivante pour réinitialiser la grille:
    
    reinit_ed(m,l)

#Cette fonction récupère les coordonnées du clic sur la partition et définit les nouvelles coordonnées en fonction des cases de la grille de la partition
def correspond(y,x):
    return [(y-y0)/hcasep,(x-x0)/lcasep]


canvas2.bind("<Button-1>", clic_partition) 
# Avec bind(), on exécute une certaine fonction en cas de clic dans le canvas avec le bouton de la souris indiqué (ici clic gauche)



compt_edit=0
bout_play_ed=Button()
bout_stop_ed=Button()

def opt_edit(m,l):     #Cette fonction permettra de choisir l'action à effectuer lors du clic sur la partition: Soit on édite le bloc, soit on le supprime.
    
    global bout_play_ed
    global bout_stop_ed
    global fInfos
    global curseur1

    fInfos = Toplevel()

    fInfos.geometry('300x300')

    
    fInfos.title("Options d'édition")
    
    #Grace à lambda, la fonction ne s'exécute qu'au moment ou l'on clique sur le bouton ET transmet m et l en arguments:
    
    Button(fInfos, text='Editer le bloc', command=lambda: edit_bloc(m,l)).pack(padx=10, pady=10)  
    Button(fInfos, text='Supprimer le bloc', command= lambda: sup_bloc(m,l)).pack(padx=10, pady=10)
    fInfos.transient(canvas) 


        #On fait apparaitre le bouton pour jouer le bloc édité. Au moment du cilc sur le bouton on exécutera play_one avec en arguments m,l.
    
    bout_play_ed.destroy()
    bout_play_ed=Button(lf6, text='Jouer le bloc édité',command=lambda: start_playing(m,l))
    bout_play_ed.grid(column=1,row=1)
    curseur1 = canvas.create_line(0, 0, 0, 410,fill="Red",width=4)
    bout_stop_ed.destroy()
    bout_stop_ed=Button(lf6,text='Stopper la lecture du bloc édité',command=lambda :stop_playing())
    bout_stop_ed.grid(column=1,row=2)


def edit_bloc(m,l):     # C'est lorsqu'on fait appel à cette fonction que l'on peut éditer le bloc souhaité.
    
    if l==0:
        canvas2.create_rectangle(x0 +lcasep*m,y0+hcasep*l,x0 +lcasep*(m+1),y0+hcasep*(l+1),fill='cyan')
    if l==1:
        canvas2.create_rectangle(x0 +lcasep*m,y0+hcasep*l,x0 +lcasep*(m+1),y0+hcasep*(l+1),fill='red')
    if l==2:
        canvas2.create_rectangle(x0 +lcasep*m,y0+hcasep*l,x0 +lcasep*(m+1),y0+hcasep*(l+1),fill='green')
    if l==3:
        canvas2.create_rectangle(x0 +lcasep*m,y0+hcasep*l,x0 +lcasep*(m+1),y0+hcasep*(l+1),fill='yellow')
    if l==4:
        canvas2.create_rectangle(x0 +lcasep*m,y0+hcasep*l,x0 +lcasep*(m+1),y0+hcasep*(l+1),fill='purple')   
  
    #C'est seulement maintenant que l'on peut creer des notes dans l'editeur. On "autorise" l'appuie avec clic droit. Dès le clic, on exécute la fonction choix_note
    # avec en arguments les coord du clic (event), m et l.
    canvas.bind("<Button-3>", lambda event: choix_note(event,m,l))

    fInfos.destroy()  # On détruit la fenetre de dialogue


def sup_bloc(m,l):
    
    global fInfos
    global note
    for i in range(24):
        for j in range(64):
            note[l,m,i,j]=0   

    canvas2.create_rectangle(x0 +lcasep*m,y0+hcasep*l,x0 +lcasep*(m+1),y0+hcasep*(l+1),fill='white')

    #Après suppression du bloc, la grille de l'éditeur est réinitialisée
    reinit_ed(m,l)

    fInfos.destroy()


##############  Faders de volumes   ################"""

# Nous avons pu créer les faders de volumes, mais malheureusement nous n'avons pas réussi à transmettre les variables de volumes aux autres fonctions.

#Variables des volumes
vol_piano=None
vol_instru=0
vol_organ=0
vol_drums=0
vol_bass=0
vol_trumpet=0


#------------Piano


def fader_piano(newvalue):
    global vol_piano
    vol_piano = newvalue
 
# On créer le fader avec la classe Scale()
value = DoubleVar()
scale_pia = Scale(lf4, variable=value, orient ='vertical', from_ = 0, to= 100,
              resolution = 1, tickinterval= 5, length=400, label='Piano',command=fader_piano)
scale_pia.pack(side=LEFT)

def fader_organ(newvalue):
    global vol_organ
    vol_organ = newvalue
      
#------Organ

value = DoubleVar()
scale_org= Scale(lf4, variable=value, orient ='vertical', from_ = 0, to= 100,
              resolution = 1, tickinterval= 5, length=400, label="Organ",command=fader_organ)
scale_org.pack(side=LEFT)

#--------Drums

def fader_drums(newvalue):
    global vol_drums
    vol_drums = newvalue

value = DoubleVar()
scale_dru= Scale(lf4, variable=value, orient ='vertical', from_ = 0, to= 100,
              resolution = 1, tickinterval= 5, length=400, label='Drums',command=fader_drums)
scale_dru.pack(side=LEFT)

#-----Bass

def fader_bass(newvalue):
    global vol_bass
    vol_bass = newvalue

value = DoubleVar()
scale_bas = Scale(lf4, variable=value, orient ='vertical', from_ = 0, to= 100,
              resolution = 1, tickinterval= 5, length=400, label='Bass',command=fader_bass)
scale_bas.pack(side=LEFT)

#-------Trumpet

def fader_trumpet(newvalue):
    global vol_trumpet
    vol_trumpet = newvalue

value = DoubleVar()
scale_tru = Scale(lf4, variable=value, orient ='vertical', from_ = 0, to= 100,
              resolution = 1, tickinterval= 5, length=400, label='Trumpet',command=fader_trumpet)
scale_tru.pack(side=LEFT)



####################  PIANO_ROLLS  ####################"

# Cette fonction joue les notes corespondantes lorsqu'on clique sur les touches du piano rolls (le petit piano à gauche)

def JouerNote(x):
    global vol_instru
    vol_instru=127

    if instru==0:
        fs[0].noteon(0,x,vol_instru)
        time.sleep(0.4)
        fs[0].noteoff(0,x)
    
    if instru==1:
        fs[1].noteon(0,x,vol_instru)
        time.sleep(0.4)
        fs[1].noteoff(0,x)

    if instru==2:
        x=x-13
        fs[2].noteon(0,x,vol_instru)
        time.sleep(0.4)
        fs[2].noteoff(0,x)
        
    if instru==3:
        fs[3].noteon(0,x,vol_instru)
        time.sleep(0.4)
        fs[3].noteoff(0,x)
        
    if instru==4:
        fs[4].noteon(0,x,vol_instru)
        time.sleep(0.4)
        fs[4].noteoff(0,x)
        
scales = 2  # Il y deux octaves...
white_keys = 7 * scales #... donc 14 touches blanches en tout.
black = [1, 1, 1, 0, 1, 1, 0] * scales # Cette variable va nous permettre d'afficher les notes noires au bon endroit


#######  APPARITION DU PIANO ROLLS #############

#WHITE_KEYS------------------

#On crée ici le piano rolls, c'est la piano à gauche qui nous permet de savoir quelle note est jouée.
# D'abord on crée les notes blanches
# On insère différent cas. A chaque fois on transmet la note à jouer à la fonction Jouer_Note().
 

for i in range(white_keys):
    if i<8:
        if i==7:
            b1=Button(lf5, bg='white', activebackground='gray87',command=lambda i=i: JouerNote(59)) 
        elif (i==4) or (i==6) or (i==5):
            b1=Button(lf5, bg='white', activebackground='gray87',command=lambda i=i: JouerNote(72-2*i))
        else:
            b1=Button(lf5, bg='white', activebackground='gray87',command=lambda i=i: JouerNote(71-2*i))
    else: 
        if (i==11) or (i==12) or (i==13):
            b1=Button(lf5, bg='white', activebackground='gray87',command=lambda i=i: JouerNote(74-2*i))
        else:
            b1=Button(lf5, bg='white', activebackground='gray87',command=lambda i=i: JouerNote(73-2*i))

    b1.grid(row=i*3, column=0, rowspan=3, columnspan=4, sticky='nsew')
        
# BLACK KEYS-------------------------

# On crée maintenant les notes noires
for k in range(white_keys - 1):
    if black[k]:
        if k<6:
            if (k==4) or (k==5):
                b2=Button(lf5, bg='black', activebackground='gray35', command=lambda k=k: JouerNote(71-2*k))     
            else:
                b2=Button(lf5, bg='black', activebackground='gray35', command=lambda k=k: JouerNote(70-2*k))     
        else:
            if (k==11) or (k==12):
                b2=Button(lf5, bg='black', activebackground='gray35', command=lambda k=k: JouerNote(73-2*k))
            else:
                b2=Button(lf5, bg='black', activebackground='gray35', command=lambda k=k: JouerNote(72-2*k))

        b2.grid(row=(k*3)+2, column=0, rowspan=2, columnspan=2, sticky='nsew')




######## FONCTION PLAY POUR  INSTRUMENT (=JOUER L'EDITEUR)  #########

# Les deux dernières parties concerne la lecture de l'éditeur et du morceau


#def check():

  
a=0
playing = False


def play_one(m,l,i):           #On regarde de quel instrument il s'agit(si l=0, il s'agit du piano)
    global playing
    global case
    global curseur1
    global vol_piano, vol_organ, vol_drums, vol_bass, vol_trumpet
    vol_piano= vol_organ=vol_drums= vol_bass=vol_trumpet=127 # Cette ligne ne serait pas apparu si on avait réussi à changer les volumes.

    i+=1
    if playing==True and i<63:
                                                            #On parcours toutes les cases en longueur/toutes les colonnes
        for j in range(24):                                 #Pour chaque colonne, on parcours toutes les lignes
                                                            # EN TOUT IL YA DONC 64*24 NOTES POSSIBLES
                                                            # S'il s'agit de la batterie (drums) on redéfinit la hauteur de la note
                                  
            if note[l,m,j,i-1]!=0:                          # Si la case précédente possède une note...
                if note[l,m,j,i-1].t==double:               #...on vérifie qu'il s'agit d'une double-croche...
                    if l==2:                                                                                    #( S'il s'agit de la batterie (drums) on redéfinit la hauteur de la note)
                        fs[l].noteoff(0, 58-note[l,m,j,i-1].h)  #... et dans ce cas on l'arrete.
                    else:
                        fs[l].noteoff(0, 71-note[l,m,j,i-1].h)

            if note[l,m,j,i-2]!=0:                          #idem pour les croches (on regarde 2 cases en arrière)...
                if note[l,m,j,i-2].t==croche:
                    if l==2:
                        fs[l].noteoff(0, 58-note[l,m,j,i-2].h)
                    else:
                        fs[l].noteoff(0, 71-note[l,m,j,i-2].h)

            if note[l,m,j,i-4]!=0:                          #...les noires (on regarde 4 cases en arrière)...
                if note[l,m,j,i-4].t==noire:
                    if l==2:
                        fs[l].noteoff(0, 58-note[l,m,j,i-4].h)
                    else:
                        fs[l].noteoff(0, 71-note[l,m,j,i-4].h)
                        
            if note[l,m,j,i-8]!=0:                          #...ou les blanches(on regarde 8 cases en arrière).
                if note[l,m,j,i-8].t==blanche:
                    if l==2:
                        fs[l].noteoff(0, 58-note[l,m,j,i-8].h)
                    else:
                        fs[l].noteoff(0, 71-note[l,m,j,i-8].h)

            if note[l,m,j,i]!=0:                            #C'est ici que l'on vérifie que la case en question contient une note.
                                                            #Si c'est le cas, on lance la note.
                if l==0:
                    fs[l].noteon(0,71-note[l,m,j,i].h,vol_piano)
                
                if l==1:
                    fs[l].noteon(0,71-note[l,m,j,i].h,vol_organ)    
                if l==2:
                    fs[l].noteon(0,58-note[l,m,j,i].h,vol_drums)
                if l==3:
                    fs[l].noteon(0,71-note[l,m,j,i].h,vol_bass)
                if l==4:
                    fs[l].noteon(0,71-note[l,m,j,i].h,vol_trumpet)
    
        canvas.coords(curseur1,(i-4)*case, 0, (i-4)*case, 410)
        fenetre.after(150, play_one,m,l, i)                    # On utilise after() pour exécuter une fonction après une certaine durée.
                                                               # Comme chaque case correspond à la durée unitaire d'une double croche, on fait une pause de la durée d'une double croche avant de
                                                               # réexécuter la fonction play_one pour une nouvelle colonne.
    else:
        playing=False


def start_playing(m,l):
    global playing
    if not playing:
        print('start playing')
        playing = True
        i=-1
        play_one(m,l,i)
    else:
        print('already playing')

def stop_playing():
    global playing
    if playing:
        playing = False
        print('stop playing')
    else:
        print('nothing playing')


######## FONCTION PLAY PRINCIPALE (=JOUER LA PARTITION/LE MORCEAU)  #########


play=False

def play_all(m,l,i):  # C'est la fonction qui permet de jouer le morceau que l'on a créé
    
#On reproduit exactement les mêmes cas de figures en prenant en compte tous les instruments et tous les blocs.
    
    global play
    global vol_piano, vol_organ, vol_drums, vol_bass, vol_trumpet
    vol_piano= vol_organ=vol_drums= vol_bass=vol_trumpet=127 # Cette ligne ne serait pas apparu si on avait réussi à changer les volumes.

    i+=1
    if m<6:
        if play and i<64:
            
            for j in range(24):
                for l in range(5):
                                                            
                    if note[l,m,j,i-1]!=0:                     
                        if note[l,m,j,i-1].t==double:
                            if l==2:
                                fs[l].noteoff(0, 58-note[l,m,j,i-1].h)
                            else:
                                fs[l].noteoff(0, 71-note[l,m,j,i-1].h)
                            
                    if note[l,m,j,i-2]!=0:                   
                        if note[l,m,j,i-2].t==croche:
                            if l==2:
                                fs[l].noteoff(0, 58-note[l,m,j,i-2].h)
                            else:
                                fs[l].noteoff(0, 71-note[l,m,j,i-2].h)
                            
                    if note[l,m,j,i-4]!=0:                   
                        if note[l,m,j,i-4].t==noire:
                            if l==2:
                                fs[l].noteoff(0, 58-note[l,m,j,i-4].h)
                            else:
                                fs[l].noteoff(0, 71-note[l,m,j,i-4].h)

                    if note[l,m,j,i-8]!=0:                  
                        if note[l,m,j,i-8].t==blanche:
                            if l==2:
                                fs[l].noteoff(0, 58-note[l,m,j,i-8].h)
                            else:
                                fs[l].noteoff(0, 71-note[l,m,j,i-8].h)
                            
                    if note[l,m,j,i]!=0:
                        if l==0:
                            fs[l].noteon(0,71-note[l,m,j,i].h,vol_piano)
                        if l==1:
                            fs[l].noteon(0,71-note[l,m,j,i].h,vol_organ)    
                        if l==2:
                            fs[l].noteon(0,58-note[l,m,j,i].h,vol_drums)
                        if l==3:
                            fs[l].noteon(0,71-note[l,m,j,i].h,vol_bass)
                        if l==4:
                            fs[l].noteon(0,71-note[l,m,j,i].h,vol_trumpet)
                        
            fenetre.after(150, play_all,m,l, i)
        else:
            m+=1
            i=0
            fenetre.after(150, play_all,m,l, i)
    else:
        play=False


def start_all():
    global play
    if not play:
        print('start playing')
        play = True
        i=-1
        m=0
        l=0
        play_all(m,l,i)
    else:
        print('already playing')

def stop_all():
    global play
    if play:
        play = False
        print('stop playing')
    else:
        print('nothing playing')

# On crée enfin les boutons pour lancer et arreter la lecture du morceau
Button(lf6, text='Jouer le morceau',command= start_all).grid(row=1,column=2)
Button(lf6, text='Stopper la lecture du morceau',command=stop_all).grid(row=2,column=2)






#########################################################################################################

fenetre.mainloop()







