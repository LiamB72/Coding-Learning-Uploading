def rechercheMin(liste):
	min = liste[0]
	for i in range(1,len(liste)):
		if liste[i] < min:
			min = liste[i]
	return min

liste=[20,8,9,2,35,49]
print(rechercheMin(liste))