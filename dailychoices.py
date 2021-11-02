import os
import sys

def restartprogram(): 
    restart = input("Want to Restart? (y/n)")
    if restart == "y":
            os.execl(sys.executable, sys.executable, *sys.argv)

answer1 = input(" je wordt wakker om 8 uur in de ochtend. wat ga je doen? \na.door blijven slapen \nb.telefoon pakken \nc.opstaan \nAntwoord: ")
if answer1 == "a":
   print("dat kan maar je komt te laat op school. ;-;")
   restartprogram()
elif answer1 == "b":
    print("Jatochh lekker tiktoks vids kijken")
elif answer1 == "c":
    print("Dumb Beta child")
    restartprogram()

answer2 = input("het is nu half 8 je hebt school om 9 uur. wat ga je doen? \na.douchen en je tandenpoetsen \nb.door blijven slapen \nc.ontbijten \nAntwoord: ")
if answer2 == "a":
    print("Jaja lekker speedrunnen")
elif answer2 == "b":
    print("Nee sta nou eens op luie kind")
    restartprogram()
elif answer2 == "c":
    print("Nee joch ben helemaal beschodemieterd")
    restartprogram()

answer3 = input("oke het is nu kwart voor 9 je gaat nu de deur uit, maar je hebt nog 15min om in de les te zijn. Wat ga je doen? \na.je gaat  rennen voor je leven \nb.je gaat nog lekker wat eten \nc.je gaat toch te laat komen dus je gaat lekker op je eigen tempo lopen \nAntwoord: ")
if answer3 == "a":
    print("BEN JE ZIEK IN JE HOOFD!")
    restartprogram()
elif answer3 == "b":
    print("dat zo wel leuk zijn maar je hebt geen tijd. L")
    restartprogram()
elif answer3 == "c":
    print("Jatoch lekker de docent scammen.")


