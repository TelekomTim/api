text_1 = "Hallo Welt!"
text_2 = "FOM"
tupel = (1,2,3,4,5,6,9,8,9,10)          # entspricht: tupel = tuple(range(1, 11))
liste_1 = [1,2,3,4,5,6,7,8,9,10]        # s. o. (falls Sie die Zahlen nicht abschreiben wollen)
liste_2 = [6,7,8,9,10,11,12,13,14,15]   # ...
zahl_1 = 6
zahl_2 = 12

#1
print("In text_1 sind {} Elemente enthalten. In tupel {}.".format(len(text_1), len(tupel)))

#2
print("text_1: Ersters: {} Letzes: {}".format(text_1[0],text_1[-1]))
print("tupel: Ersters: {} Letzes: {}".format(tupel[0],tupel[-1]))

#3
print("text_1: Ersten drei: {} Letzen drei: {}".format(text_1[0:3],text_1[-3:]))
print("tupel: Erstern drei: {} Letzen drei: {}".format(tupel[0:3],tupel[-3:]))

#4
print("Jedes zweites Element aus liste_1: {}".format(liste_1[1::2]))

#5
print("Größtes Element aus text_1: {}".format(max(text_1)))
print("Kleinstes Element aus liste_2: {}".format(min(liste_2)))

#6
#liste_1 =liste_1*3
#print("Liste 1: ",liste_1)

#7
gesamtliste = liste_1 + liste_2
gesamtliste.extend(tupel)
print("Gesamtliste: ",gesamtliste)

#8
print("zahl_1 liegt in gessamtliste? ", zahl_1 in gesamtliste)

#9
print("zahl_1 liegt an Stelle: ", gesamtliste.index(zahl_1)+1 if zahl_1 in gesamtliste else "---nicht in gesamtliste---")

#10
print("zahl_1 kommt {} mal in der gesamtliste vor.".format(gesamtliste.count(zahl_1)))

#11

