#Z DEDYKACJĄ DLA MARTINA AMLICKIEGO, NAJWIĘKSZEGO HAZARDZi... - ZNACZY BIZNESMANA W BRODNICY!

import random
import time

def zakladzik():
    print (f"kasa: {kasa}")
    zaklad = (input ("Podaj swój zaklad (all jeżeli wszystko): "))
    if zaklad == "all":
        zaklad = kasa
    elif zaklad:
        zaklad = int (zaklad)
    else:
        print ("podaj zaklad")
    podane = False
    return zaklad

kasa = 200


pierwszy = False
game = True

while game == True:

    zakladnik = zakladzik()
    podane = False
    while podane == False:
        if zakladnik <= kasa:
            podane = True
        else:
            print ("ERROR: Nie masz wystarczających środków\n")
            zakladnik = zakladzik()
    
    liczba = input("Podaj swój los. Możliwe losy:\nod 0 do 36\ngreen, red, black\n\n")
    if liczba:
        if liczba not in ["red","green","black",]:
            liczba = int(liczba)
    secret_liczba = random.randint(0,36)
    
    if liczba in range(1,37,2):
        status = "red"
    elif liczba in range (2,37,2):
        status = "black"
    else:
        status = "green"

    if secret_liczba in range(1,37,2):
        secret_status = "red"
    elif secret_liczba in range (2,37,2):
        secret_status = "black"
    else:
        secret_status = "green"
    print("Koło się kręci...\n Odpowiedzi za 5 sekund")

    time.sleep(5)



    print (f"{secret_status} {secret_liczba}")
    if liczba == secret_liczba or secret_status == liczba:
        print ("##~~Gratulacje!~~##\n\n")
        kasa = kasa + zakladnik
    else:
        print ("spróbuj ponownie\n\n")
        kasa = kasa - zakladnik

    if kasa == 0:
        kontynuacja = input ("Czy chcesz kontynuować? y/n ")
        if kontynuacja == "y":
            print ("Tajemniczy bezdomny dał ci dotacje w wysokości 200 zł!\n\n")
            kasa = 200
            continue
        
        elif kontynuacja == "n":
            print ("Brak środków na koncie. Prosimy o opuszczenie kasyna. To nie schronisko dla bezdomnych.")
            game = False
            time.sleep(10)
        
        else:
            print ("y/n")
    
    elif pierwszy == False and kasa > 10000:
        print ("Brawo! Zostałeś użytkownikiem VIP! Użytkownikom VIP zabrania się gry w kasynie, ponieważ za dużo już zabrali.\n Prosimy o opuszczenie kasyna.")
        game = False
        time.sleep(10)
