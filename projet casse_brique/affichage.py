import time
from upemtk import *
dimension_fenetre=400
##################################################################################
#########################  AFFICHAGE DU JEU ######################################
##################################################################################

def perdu():
    texte(dimension_fenetre//2,dimension_fenetre//2,"Perdu!","red","center")
    attente_clic()

def gagne():
    texte(dimension_fenetre//2,dimension_fenetre//2,"Gagné!","red","center")
    attente_clic()

def affichage(score,temps,liste):
	temps=int(time.clock())
	ligne(dimension_fenetre+1, 0, dimension_fenetre+1, dimension_fenetre, couleur='black', epaisseur=2, tag='')
	texte(dimension_fenetre+10,10 , "Score : "+str(score)+"\n\nTemps : "+str(temps)+"\n\nBriques restantes :"+str(len(liste))+"\n\n\n\n\n\n           : Bonus score\n\n           : 3 coups\n\n           : 2 coups\n\n           : 1 coups",couleur='black', ancrage='nw', police="", taille=12, tag='')
	rectangle(410,197,460,217,'blue','',epaisseur=2,tag='')
	rectangle(410,235,460,255,'black','yellow',epaisseur=1,tag='')

	rectangle(410,275,460,295,'black','orange',epaisseur=1,tag='')

	rectangle(410,315,460,335,'black','red',epaisseur=1,tag='')



def creer_balle():
	x=dimension_fenetre/2
	y=(2*dimension_fenetre)/3
	cercle(x,y,5,couleur='red',remplissage='red',epaisseur=1,tag='')
	return [x,y]


def afficher_balle(balle):
	cercle(balle[0],balle[1],5,couleur='red',remplissage='red',epaisseur=1,tag='')
	return balle


def creer_raquette():
	ext1=(4*dimension_fenetre)/10
	ext2=(6*dimension_fenetre)/10
	rectangle((4*dimension_fenetre)/10,dimension_fenetre-10,(6*dimension_fenetre)/10,dimension_fenetre-20,'black','black',epaisseur=0,tag='')
	return ext1,ext2

def afficher_raquette(a,ext1,ext2):
	# Affiche la raquette après un déplacement.
	rectangle(ext1+a,dimension_fenetre-10,ext2+a,dimension_fenetre-20,'black','black',epaisseur=0,tag='')



def afficher_briques(liste):
	# Affiche les briques en fonction de leur résistance 
	for brique in liste:
		if brique[4]==3 and brique[5]==1:
			rectangle(brique[0],brique[1],brique[2],brique[3],'blue','yellow',epaisseur=2,tag='')
		if brique[4]==3 and brique[5]!=1:
			rectangle(brique[0],brique[1],brique[2],brique[3],'black','yellow',epaisseur=1,tag='')
		if brique[4]==2 and brique[5]==1:
			rectangle(brique[0],brique[1],brique[2],brique[3],'blue','orange',epaisseur=2,tag='')
		if brique[4]==2 and brique[5]!=1:
			rectangle(brique[0],brique[1],brique[2],brique[3],'black','orange',epaisseur=1,tag='')
		if brique[4]==1 and brique[5]==1:
			rectangle(brique[0],brique[1],brique[2],brique[3],'blue','red',epaisseur=2,tag='')
		if brique[4]==1 and brique[5]!=1:
			rectangle(brique[0],brique[1],brique[2],brique[3],'black','red',epaisseur=1,tag='')
		if brique[4]==0:
			return None


def afficher_raquette_auto(balle):
	# Affichage de la raquette pour le mode auto, elle suit la balle.
	if balle[0]<=dimension_fenetre-40 and balle[0] >= 40:
		rectangle(balle[0]-40,dimension_fenetre-10,balle[0]+40,dimension_fenetre-20,'black','black',epaisseur=0,tag='')
	elif balle[0]>dimension_fenetre-40 :
		rectangle(dimension_fenetre-80,dimension_fenetre-10,dimension_fenetre,dimension_fenetre-20,'black','black',epaisseur=0,tag='')
	else :
		rectangle(0,dimension_fenetre-10,80,dimension_fenetre-20,'black','black',epaisseur=0,tag='')