def rechercheMax(liste):
	max = liste[0]
	for i in range(1,len(liste)):
		if liste[i] > max:
			max = liste[i]
	return max

liste=[20,8,9,2,35,49]
print(rechercheMax(liste))
