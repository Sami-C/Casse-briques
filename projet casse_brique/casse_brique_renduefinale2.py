from upemtk import *
import time
from random import randint
from affichage import *
############### Constantes programme ######################
dimension_fenetre=400
###########################################################


##################################### Balle ####################################
def rebond_balle_mur(balle,mx,my):
	if balle[0]+5>=dimension_fenetre:
		if my==-1:
			mx=-1
			my=-1
		else :
			mx=-1
			my=1
		return mx,my
	if balle[0]-5<=0:
		if my==-1:
			mx=1
			my=-1
		else:
			mx=1
			my=1
		return mx,my
	if balle[1]-5<=0:
		if mx ==1:
			mx=1
			my=1
		else :
			mx=-1
			my=1
		return mx,my
	return mx,my

######################################################################################################


##################################################### Raquettes ###########################################################

def mise_a_jour_direction(dir):
    nouvelle_dir=dir
    ev=donne_evenement()
    type_ev=type_evenement(ev)
    if type_ev=="Touche":
        t=touche(ev)
        if t=="Right":
            nouvelle_dir='droite'
        elif t=="Left":
            nouvelle_dir='gauche'
    return nouvelle_dir

def deplace_raquette(dir,a):
	if dir =='droite':
		if ((6*dimension_fenetre)/10)+a <=390:
			a+=10  
	if dir=='gauche' :
		if ((4*dimension_fenetre)/10)+a >=10:
			a-=10
	return a

def rebond_raquette(balle,mx,my,a,ext1,ext2):
	# mx et my sont les mouvements de la balle selon l'axe des abscisses et des ordonnées. 
	if ext1+a<= int(balle[0]) < ((ext1+ext2)/2)+a and int(balle[1]+5)>=dimension_fenetre-20:
		mx=-1
		my=-1
	if ((ext1+ext2)/2)+a < int(balle[0]) <= ext2+a and int(balle[1]+5)>=dimension_fenetre-20:
		mx=1
		my=-1
	if int(balle[0]) == ((ext1+ext2)/2)+a and int(balle[1]+5)>=dimension_fenetre-20:
		mx=0
		my=-1

	return mx,my

#####################################################################################################
###################################### Affichage Jeu ##############################################

########################################  Briques ###################################################


def initialiser_briques():
	lst=[]
	y=20
	x=0
	while y<dimension_fenetre/3:
		x=0
		while x<dimension_fenetre :
			resistance=randint(1,3)
			bonus_score=randint(1,5)
			lst.append([x,y,x+50,y+20,resistance,bonus_score])
			x+=50
		y+=20
	return lst
	

def rebondballe_briques(balle):
	# renvoie la brique que rencontre la balle et un nombre pour définir le rebond de la balle et le channgement de la résistance de la brique dans la fonction suivante.
	for brique in liste_brique:
		# rebond face basse de la brique 
		if (brique[3]==int(balle[1]-5)) and (brique[0]<=balle[0]<=brique[2]):
			return 1, brique
		# rebond face haute de la brique
		if (brique[1]==int(balle[1]+5)) and (brique[0]<=balle[0]<=brique[2]):
			return 1, brique
			
		# rebond face gauche de la brique
		if (brique[1]<=balle[1]<=brique[3]) and (brique[0]==int(balle[0]+5)) :
			return 2 , brique
		# rebond face droite de la brique 
		if (brique[1]<=balle[1]<=brique[3]) and (brique[2]==int(balle[0]-5)):
			return 2, brique

		# Rebondit sur un coin dès que le carré dans lequel est inscrit la balle rencontre le coin d'une brique
		if balle[0]-4<=brique[0]<=balle[0]+4 and balle[1]-4<=brique[1]<=balle[1]+4:
			print(balle)
			return 3,brique
		if balle[0]-4<=brique[0]<=balle[0]+4 and balle[1]-4<=brique[3]<=balle[1]+4:
			print(balle)
			return 3,brique	
		if balle[0]-4<=brique[2]<=balle[0]+4 and balle[1]-4<=brique[1]<=balle[1]+4:
			print(balle)
			return 3,brique
		if balle[0]-4<=brique[2]<=balle[0]+4 and balle[1]-4<=brique[3]<=balle[1]+4:
			print(balle)
			return 3,brique

	return 0,[]

def rebond_balle_face_brique(i,mx,my,brique,balle,score):
	# Défini le rebond de la balle selon l'endroit de la balle touché et baisse la résistance de la brique.
	if brique != [] :
		brique[4]=brique[4]-1
		if brique[4]== 0 :
			if brique[5]==1:
				score+=50
			else:
				score+=10
			liste_brique.remove(brique)
	if i == 1:
		mx=mx
		my=-my
	if i ==2:
		mx=-mx
		my=my
	if i==3: 
		mx=-mx
		my=-my
	return mx,my,score

#########################################################################################

################################# Mode ordinateur ####################################

def rebond_raquette_auto(balle,mx,my):
	# Rebond différent du mode normal sinon la balle rebondissait seulement au centre de la raquette et donc seulement verticalement.
	if int(balle[1]+5)== dimension_fenetre-20:
		if mx==1:
			mx=1
			my=-1
		else:
			mx=-1
			my=-1
		return mx,my
	return mx,my
#########################################################################################

if __name__ == "__main__":
	# Pour choisir le mode avant de lancer le programme.
	cree_fenetre(1.5*dimension_fenetre,dimension_fenetre)
	rectangle(0,0,300,400,'black','blue',epaisseur=1,tag='')
	rectangle(300,0,600,400,'black','orange',epaisseur=1,tag='')
	texte(65,180,"Mode normal",couleur='white',taille=20)
	texte(380,180,"Mode auto",couleur='white',taille=20)
	clic=attente_clic()
	if 0<=clic[1]<=400 and 0<= clic[0]<= 300:
		score=0  # initialisations nécessaires pour l'affichage
		temps=0
		liste_brique=initialiser_briques()
		affichage(score,temps,liste_brique)
		balle=creer_balle()
		ext1,ext2=creer_raquette()
		mx=0
		my=1
		a=0 # sert pour l'affichage de la raquette après un déplacement
		v=1 # pour définir la vitesse 
		briques=[]
		while True:	
			efface_tout()
			affichage(score,temps,liste_brique)
			if liste_brique ==[]:
				gagne()
				ferme_fenetre()
			dir=mise_a_jour_direction(dir)
			a=deplace_raquette(dir,a)
			dir='haut' 			# pour que la raquette s'arrete après un déplacement.
			afficher_raquette(a,ext1,ext2)
			afficher_briques(liste_brique)
			balle=afficher_balle(balle)
			i,briques=rebondballe_briques(balle)
			mx,my=rebond_raquette(balle,mx,my,a,ext1,ext2)
			mx,my=rebond_balle_mur(balle,mx,my)
			mx,my,score=rebond_balle_face_brique(i,mx,my,briques,balle,score)
			balle[0]+=(mx/v)
			balle[1]+=(my/v)
			mise_a_jour()
			if balle[1]+5 > 400:
				perdu()
				ferme_fenetre()
		attente_clic()
		ferme_fenetre()


################################### Mode Ordinateur #################################
	if 0<=clic[1]<=400 and 300<= clic[0]<= 600:
		score=0
		temps=0
		liste_brique=initialiser_briques()
		affichage(score,temps,liste_brique)
		balle=creer_balle()
		ext1,ext2=creer_raquette()
		mx=0
		my=1
		a=0
		v=1# pour définir la vitesse 
		i=0
		briques=[]
		while True:	
			efface_tout()
			affichage(score,temps,liste_brique)
			if liste_brique ==[]:
				gagne()
				ferme_fenetre()
			afficher_raquette_auto(balle)
			afficher_briques(liste_brique)
			balle=afficher_balle(balle)
			i,briques=rebondballe_briques(balle)
			mx,my=rebond_raquette_auto(balle,mx,my)
			mx,my=rebond_balle_mur(balle,mx,my)
			mx,my,score=rebond_balle_face_brique(i,mx,my,briques,balle,score)
			balle[0]+=(mx/v)
			balle[1]+=(my/v)
			mise_a_jour()
			if balle[1]+5 > 400:
				perdu()
				ferme_fenetre()
		attente_clic()
		ferme_fenetre()