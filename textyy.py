from random import shuffle 
liste = "eins zwei drei vier feunf sechs sieben acht neun zehn".upper().split()

shuffle(liste)

for s in range (3):
    for i in range (2):
        for n in range (4):
            print ("Spam ", end='')
        print ()
    el1=liste.pop()
    el2=liste.pop()
    print ("{} Spam, {} Spam".format(el1, el2))
    print ()
    