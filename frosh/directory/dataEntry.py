import re
from directory.models import House, Vassal

indexList = []

for i in range(7, 35):
    
    if i == 21 or i == 28 or i == 30 or i == 13:
    
        print("skipped " + str(i))
        
    else:
        
        indexList.append(i)


string = "Hassan Al-Rabea, Nour el Tayah, Luis Pombo, Carlos Marin;Siobhan Doherty, Laura Morrison, Chris Sarlos, Amer Dib;Justin Asfour, Alex Cerulli, Sandra Buchen, Martin De Sousa;Laurence Blondeau-Bouchard, Marc-Olivier Granger, Marc-Antoine Grondin, Roberto Cola;Steven Cummings, Chelsea Rogers, Olivier Gomes, James Mehta;Sara Cullen, Emmet Austin, Sam Pho, Matthias Rivollier;Phil Sioumaras, Shannon Gregory, Gabriel Giguere-Joannette, Christian Percque;Eitan Bulka, Justin Hayto, Cole Macdonald, Robyn Iannitto;Annelise Loczy, Matthieu Labaudiniere, Clara Hartmanshenn, Bram Marriott;Zoe Petard, Marilena Anghelopoulu, Josh Ton, Jonathan Choi;Dana Ben David, Veronique Demers, Michael Karpuk, Tuhin Gupta;Davide Campellone, Rubo Liu, Scott Rochefort, Melissa L'Heureux-Hache;Laurissa Cebryk, Heather Richardson, Colin Grambow, Justin Cayouette;Andy Cabral, Annie Pike, Dune Desormeaux, Ian Richardson;Husam Al-Rameeni, Steven Paolasini, Ziad Saliba, Kiersten Locas-Hoeltken;Anthony Delage, Jean-Nicholas Di Marzo, Ilana Khin, Jared Kimball;Samantha Dorrance, Rachel Meland, Jamie Fuoco, Jeff Hamilton;Christophe Petitclerc-Demers, Nicolas Westgate, Michelle Bennett, Myles Hildebrand;Celina Gratton, Eleni Speal, Ashkaan Mohtashami, Reid Hadaway;Justin Mendonca, Eric Gubiani, Michael Dionisi, Sibylle Deriot;Justin MacAskill, Rob Oda, Jack Minchom, Sophie Marcotte;Vincent Wu, Reza Tadayon, Patrick Chandler, Tania Pilon;Avril Levasseur, Alexander Chevarie, Daniel Kost-Stevenson, David Johnson;Nicholas Nadeau, Jennifer Kwiatkowski, Samuel Bruneau, Vincent Wiedemann;"

splitString = re.findall('([a-zA-Z\-,\s]+);', string)

print(len(splitString))
    
i = 0

for entry in splitString:

    entry = entry + ","

    iD = indexList[i]

    house = House.objects.get(pk=int(iD))

    names = re.findall('([a-zA-Z\s\-]+),', entry)

    for name in names:

        b = Vassal.objects.create(title = "Sir", name = name, house = house)

        b.save()

    i += 1

    if i == 24:

        break
