a = 4
b = 7
if a < b:
    print("Je suis Aladin.")
    print("Je n'aime pas Jafar")
else:
    print("Je suis Jafar.")
    print("Je n'aime pas Aladin.")
print("En revanche, j'aime le Python.")

#Explication :

	#1.	Initialisation des variables :
	#•	a est assigné à la valeur 4.
	#•	b est assigné à la valeur 7.
	#2.	Instruction conditionnelle (if a < b):
	#•	La condition a < b est vraie parce que 4 est inférieur à 7.
	#3.	Exécution du bloc if :
	#•	Étant donné que la condition est vraie, le programme exécute les instructions à l’intérieur du bloc if :
	#•	print("Je suis Aladin."); affiche : Je suis Aladin.
	#•	print("Je n'aime pas Jafar") affiche : Je n’aime pas Jafar
	#4.	Bloc else ignoré :
	#•	Le bloc else n’est pas exécuté parce que la condition du if est vraie.
	#5.	Instruction finale :
	#•	L’instruction print("En revanche, j'aime le Python.") est en dehors des blocs if et else, elle est donc toujours exécutée.
	#•	Elle affiche : En revanche, j’aime le Python.

#Résumé :

	#•	Le programme compare deux variables et, en fonction du résultat, exécute le bloc correspondant.
	#•	La dernière instruction print s’exécute indépendamment de la condition et affiche toujours son message.