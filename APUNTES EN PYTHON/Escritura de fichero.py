f = open('Fichero para escribir.txt', 'w') #Genero un nuevo fichero
f.write("Con los dedos de las manos con los dedos de los pies, \n")
f.write("con la polla y los cojones todos suman 23 \n")
lista = ["Cayo Octavio Turino\n ",
        "Cayo Julio Cesar\n ",
        "Marco Ulpio Trajano\n ",
        "Publio Cornelio Escipion El Africano \n"]
f.writelines(lista)#Se meten listas