# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 10:58:28 2022

@author: richard_bohunovsky
"""

import sys
import random
import colorama 
from colorama import Back, Fore, Style


hra = 0
hod = 1
pravidla = ("\n\tVšechny figurky jsou před začátkem hry umístěny ve startovním domečku, který je barevně vyznačen"
"stejnou barvou, jakou jsou označeny 4 figurky hráče. \n\tCílem hry je dovést své figurky jedné barvy ze startovního"
"pole do cílového domečku. To lze pouze tak, že figurka musí projít postupně všemi poli na obvodu hracího plánu."
"\n\tKaždý hráč posune při svém tahu figurku o tolik bodů, kolik padlo při jeho hodu kostkou. Skončí-li s figurkou"
"na políčku obsazeném cizí figurkou, je tato odstraněna ze hry a vrácena zpět do startovního domečku. Na políčko"
"obsazené figurkou stejné barvy vstoupit nelze. \n\tK nasazení figurky na startovní pole je potřeba hodit šestku."
"Nemá-li hráč nasazenou žádnou figurku, hází kostkou do té doby, dokud nepadne šestka, maximálně však třikrát."
"Pokud ani po třetím hodu nepadne šestka, pokračuje ve hře další hráč.Během hry po hozené šestce hází hráč kostkou"
"ještě jednou a posune jednu zvolenou figurku o součet bodů při obou hodech.\n"
"\tVyhrává ten hráč, který oběhne hrací plán všemi svými figurkami a umístí je do cílového domečku.\n"
"\nNA POLI MŮŽE BÝT NASAZENÁ POUZE JEDNA FIGURKA !!!")
vyherni_mista = ["prvním", "druhém", "třetím", "posledním"]

#Funkce pomocí cyklu for vykreslí část políček s kladnou i zápornou posloupností pomocí hodnoty 0 or 1
def for_herni_plan_posloupnost(kolikrat, start, hodnota):
    lajna = ""
    for i in range(kolikrat):
        if hodnota == 1:
            lajna += policka[start+i][-1] + " " + Fore.RESET
        else:
            lajna += policka[start-i][-1] + " " + Fore.RESET
    return lajna
#Funkce přidá přesný počet mezer, kvůli vycentrování hracího plánu
def mezery(kolik):
    string_mezery = ""
    for a in range(kolik):
        string_mezery += " "
    return string_mezery
#Funkce generuje pro každého hráče seznam políček
def generace_policek(start, konec, seznam):
    zacatek = start+1
    for i in range(40):
        if len(seznam) == 39:
            seznam.append(zacatek)
            zacatek = start
        if zacatek == start:
            zacatek = konec
            for a in range(3):
                seznam.append(zacatek)
                zacatek += 1
        seznam.append(zacatek)
        zacatek += 1
        if zacatek>40 and len(seznam)<40:
            zacatek = 1
#Funkce vygeneruje slovník s číslem hracího políčka a znakem, který bude použit na vykreslení hracího plánu
def generace_slovniku(slovnik, znak_hraciho_pole):
    for policko in range(56):
        slovnik[policko+1] = [znak_hraciho_pole]
#Funkce vygeneruje hrací plán ze slovníku políček
def generace_herniho_planu(policka):
    global mapa
    mapa = "\n"
    mapa += mezery(8) + Fore.RESET + policka[39][-1] + " " + Fore.RESET + policka[40][-1] + " " + Fore.RESET + policka[1][-1] + "\n"
    mapa += mezery(8) + Fore.RESET + policka[38][-1] + " " + Fore.RED + policka[41][-1] + " " + Fore.RESET + policka[2][-1] + "\n"
    mapa += mezery(8) + Fore.RESET + policka[37][-1] + " " + Fore.RED + policka[42][-1] + " " + Fore.RESET + policka[3][-1] + "\n"
    mapa += mezery(8) + Fore.RESET + policka[36][-1] + " " + Fore.RED + policka[43][-1] + " " + Fore.RESET + policka[4][-1] + "\n"
    mapa += Fore.RESET + for_herni_plan_posloupnost(5, 31, 1) + Fore.RED + policka[44][-1] + " " + Fore.RESET + for_herni_plan_posloupnost(5, 5, 1) + "\n"
    mapa += Fore.RESET + policka[30][-1] + " " + Fore.BLUE + policka[53][-1] + " " + Fore.BLUE + policka[54][-1] + " " + Fore.BLUE + policka[55][-1] + " " + Fore.BLUE + policka[56][-1] + " "
    mapa += mezery(2) + Fore.RESET + Fore.GREEN + policka[48][-1] + " " + Fore.GREEN + policka[47][-1] + " " + Fore.GREEN + policka[46][-1] + " " + Fore.GREEN + policka[45][-1] + " " + Fore.RESET + policka[10][-1] + "\n"
    mapa += Fore.RESET + for_herni_plan_posloupnost(5, 29, 0) + Fore.MAGENTA + policka[52][-1] + " " + Fore.RESET + for_herni_plan_posloupnost(5, 15, 0) + "\n"
    mapa += mezery(8) + Fore.RESET + policka[24][-1] + " " + Fore.MAGENTA + policka[51][-1] + " " + Fore.RESET + policka[16][-1] + "\n"
    mapa += mezery(8) + Fore.RESET + policka[23][-1] + " " + Fore.MAGENTA + policka[50][-1] + " " + Fore.RESET + policka[17][-1] + "\n"
    mapa += mezery(8) + Fore.RESET + policka[22][-1] + " " + Fore.MAGENTA + policka[49][-1] + " " + Fore.RESET + policka[18][-1] + "\n"
    mapa += mezery(8) + Fore.RESET + policka[21][-1] + " " + Fore.RESET + policka[20][-1] + " " + Fore.RESET + policka[19][-1] + "\n"
    return mapa
#Funkce vygeneruje barevný seznam figurek hráčů
def generace_seznamu_figurek(barva, seznam, znak):
    for i in range(4):
        seznam.append(barva + znak)
    Fore.RESET
    return seznam
#Funkce, která zajistí tři hody, když hráč nemá nasazenou žádnou figurku
def nasazeni_figurky(hod, hrac, policka, policka_hraci, kdo_je_na_rade, hraci, znaky_hracu, aktualni_policko):
    while hod<=3:
        hod += 1
        vstup = input(Fore.RESET + "Pro hod kostkou stiskněte ENTER: ")
        konec(vstup)
        kostka = random.randint(1, 6)
        print(f"{Fore.RESET}Na kostce padlo: {kostka}")
        if kostka == 6:
            print(f"{Fore.RESET}{hrac} si nasazuje figurku.")
            vyhazovani_protihracu(policka, policka_hraci, aktualni_policko[kdo_je_na_rade], hraci, znaky_hracu, kdo_je_na_rade, aktualni_policko)
            hraci[kdo_je_na_rade].pop(0)
            hod=4
#Funkce, která zajistí možnost vyhazování protihráčů a zároveň zapisuje novou polohu hráče
def vyhazovani_protihracu(policka, policka_hraci, cislo_policka, hraci, znaky_hracu, kdo_je_na_rade, aktualni_policko):
    symbol = policka[policka_hraci[kdo_je_na_rade][cislo_policka]][-1]
    if len(policka[policka_hraci[kdo_je_na_rade][cislo_policka]]) > 1 and symbol!=znaky_hracu[kdo_je_na_rade]:
        if len(policka[policka_hraci[kdo_je_na_rade][aktualni_policko[kdo_je_na_rade]]])!=1:
            policka[policka_hraci[kdo_je_na_rade][aktualni_policko[kdo_je_na_rade]]].pop(-1)
        hraci[znaky_hracu.index(symbol)].append(symbol)
        aktualni_policko.pop(znaky_hracu.index(symbol))
        aktualni_policko.insert(znaky_hracu.index(symbol), 0)
        if len(policka[policka_hraci[kdo_je_na_rade][cislo_policka]]) > 1:
            policka[policka_hraci[kdo_je_na_rade][cislo_policka]].pop(-1)
        policka[policka_hraci[kdo_je_na_rade][cislo_policka]].append(znaky_hracu[kdo_je_na_rade])
        aktualni_policko.insert(kdo_je_na_rade, cislo_policka)
        aktualni_policko.pop(kdo_je_na_rade+1)
    elif len(policka[policka_hraci[kdo_je_na_rade][cislo_policka]]) == 2 and symbol==znaky_hracu[kdo_je_na_rade]:
        print(f"{Fore.RESET}Bohužel toto políčko máš již obsazené")
    else:
        if len(policka[policka_hraci[kdo_je_na_rade][aktualni_policko[kdo_je_na_rade]]])!=1:
            policka[policka_hraci[kdo_je_na_rade][aktualni_policko[kdo_je_na_rade]]].pop(-1)
        policka[policka_hraci[kdo_je_na_rade][cislo_policka]].append(znaky_hracu[kdo_je_na_rade])
        aktualni_policko.insert(kdo_je_na_rade, cislo_policka)
        aktualni_policko.pop(kdo_je_na_rade+1)
#Funkce. která zajišťuje hod kostkou
def hod_kostkou(aktualni_policko, kdo_je_na_rade, policka, policka_hraci, hraci, znaky_hracu, domecky):
    vstup = input(Fore.RESET + "Pro hod kostkou stiskněte ENTER: ")
    konec(vstup)
    kostka = random.randint(1, 6)
    print(f"Na kostce padlo: {kostka}")
    kde_je = aktualni_policko[kdo_je_na_rade]+kostka
    if kde_je>43:
        print(f"{Fore.RESET}Bohužel, přesáhl jsi políčka domečku")
    elif kde_je<44 and kde_je>39:
        vyhazovani_protihracu(policka, policka_hraci, kde_je, hraci, znaky_hracu, kdo_je_na_rade, aktualni_policko)
        if aktualni_policko[kdo_je_na_rade] in [40,41,42,43]:
            domecky[kdo_je_na_rade].append(znaky_hracu[kdo_je_na_rade])
            aktualni_policko.pop(kdo_je_na_rade)
            aktualni_policko.insert(kdo_je_na_rade, 0)
    else:
        vyhazovani_protihracu(policka, policka_hraci, kde_je, hraci, znaky_hracu, kdo_je_na_rade, aktualni_policko)
        if kostka == 6:
            hod_kostkou(aktualni_policko, kdo_je_na_rade, policka, policka_hraci, hraci, znaky_hracu, domecky)
#Funkce ukončí program podle toho když hráč napíše konec, nebo hráče odkloní na hlavní větev když napíše menu
def konec(vstup):
    if vstup == "konec":
        sys.exit()
    elif vstup == "menu":
        main()
#Funkce je vedlejší větví programu, resetuje takřka všechny proměnné, které se v programu vyskytují
def main_2():
    kdo_je_na_rade = 0
    #Určení seznamu jmen hráčů a hráč si může zvolit přezdívku a symbol, se kterým bude hrát
    #Cykly while ošetřují vstupy, aby nemohly obsahovat prázdný string, nebo mezeru
    jmeno_hrace = ""
    znak_hrace = ""
    znak_hraciho_pole = ""
    while jmeno_hrace.strip() == "":
        jmeno_hrace = str(input("Zadejte Vaši přezdívku: "))
        konec(jmeno_hrace)
    while znak_hrace.strip() == "":
        znak_hrace = str(input("Zadejte znak, se kterým chcete hrát: "))
        konec(znak_hrace)
    while znak_hraciho_pole.strip() == "":
        znak_hraciho_pole = str(input("Zadejte znak, který se bude zobrazovat jako políčko na hrací desce: "))
        konec(znak_hraciho_pole)
    hraci_jmena = [jmeno_hrace, "Zelený", "Fialový", "Modrý"]
    #Blok hráče
    policka_hrac = []
    generace_policek(0, 41, policka_hrac)
    figurky_hrac = []
    domecek_hrac = []
    generace_seznamu_figurek(Fore.RED, figurky_hrac, znak_hrace)
    #Blok počítače č.1
    policka_bot_1 = []
    generace_policek(10, 45, policka_bot_1)
    figurky_bot_1 = []
    domecek_bot_1 = []
    generace_seznamu_figurek(Fore.GREEN, figurky_bot_1, "☻")
    #Blok počítače č.2
    policka_bot_2 = []
    generace_policek(20, 49, policka_bot_2)
    figurky_bot_2 = []
    domecek_bot_2 = []
    generace_seznamu_figurek(Fore.MAGENTA, figurky_bot_2, "☻")
    #Blok počítače č.3
    policka_bot_3 = []
    generace_policek(30, 53, policka_bot_3)
    figurky_bot_3 = []
    domecek_bot_3 = []
    generace_seznamu_figurek(Fore.BLUE, figurky_bot_3, "☻")
    #Seznamy seznamů, ve kterých se program vyzná podle toho, kdo je zrovna na řadě
    hraci = [figurky_hrac, figurky_bot_1, figurky_bot_2, figurky_bot_3]
    policka_hraci = [policka_hrac, policka_bot_1, policka_bot_2, policka_bot_3]
    domecky = [domecek_hrac, domecek_bot_1, domecek_bot_2, domecek_bot_3]
    aktualni_policko = [0,0,0,0]
    znaky_hracu = []
    vyherni_poradi = []
    for znak_figu in range(4):
        znaky_hracu.append(hraci[znak_figu][0])
    #První vypsání hrcího pole a seznámení s protihráči
    generace_slovniku(policka, znak_hraciho_pole)
    print(generace_herniho_planu(policka))
    for vypis in range(len(hraci)):
        print("Figurky hráče " + hraci_jmena[vypis] + ":", *hraci[vypis], "\n", Fore.RESET)
    #Program hry, kdy program běží dokud nezbývá jen jeden hráč
    while len(hraci)!=1:
        print(f"{Fore.RESET}Na řadě je hráč {hraci_jmena[kdo_je_na_rade]}\n")
        if len(hraci[kdo_je_na_rade]) + len(domecky[kdo_je_na_rade]) == 4:
            nasazeni_figurky(1, hraci_jmena[kdo_je_na_rade], policka, policka_hraci, kdo_je_na_rade, hraci, znaky_hracu, aktualni_policko)
            print(generace_herniho_planu(policka))
        else:
            hod_kostkou(aktualni_policko, kdo_je_na_rade, policka, policka_hraci, hraci, znaky_hracu, domecky)
            print(generace_herniho_planu(policka))
        # if v domečku jsou 4 -> smazat ze všech seznamů
        if len(domecky[kdo_je_na_rade]) == 4:
            vyherni_poradi.append(hraci_jmena[kdo_je_na_rade])
            domecky.pop(kdo_je_na_rade)
            hraci.pop(kdo_je_na_rade)
            policka_hraci.pop(kdo_je_na_rade)
            hraci_jmena.pop(kdo_je_na_rade)
            aktualni_policko.pop(kdo_je_na_rade)
            znaky_hracu.pop(kdo_je_na_rade)
        kdo_je_na_rade+=1
        # if pokud číslo kdo je na řadě přesáhlo délku seznamu hráčů, vrací se k prvnímu hráči
        if kdo_je_na_rade>=len(hraci):
            kdo_je_na_rade = 0
    vyherni_poradi.append(hraci_jmena[0])
    vstup = input("Pro vypsání pořadí hráčů stiskněte ENTER:")
    konec(vstup)
    for vyhra in range(4):
        print(f"\nNa {vyherni_mista[vyhra]} místě se umístil {vyherni_poradi[vyhra]}")
    vstup = input("Pro navrácení do hlavního menu stiskněte ENTER:")
    konec(vstup)
    main()
#Funkce je hlavní větví programu, jedná se o hlavní menu, kde se resetuje proměnná policka
def main():
    global policka
    policka = {}
    print(("\n"+mezery(19)+"ČLOVĚČE NEZLOB SE"+"\n\n"+mezery(12)+"Pro začátek hry napište: '1'"+"\n\n"+mezery(12)+"Pro zobrazení pravidel napište: '2'"+"\n\n"+mezery(12)+"Pro ukončení aplikace napište: '3'"))
    volba_uziv = str(input("\nVaše volba: "))
    if "1" in volba_uziv:
        main_2()
    elif "2" in volba_uziv:
        print(f"{pravidla} \n")
        main()
    elif "3" in volba_uziv:
        print(f"{Back.BLACK}{Fore.RED}Aplikace bude ukončena, děkujeme za vyzkoušení!")
        Back.RESET
        global hra
        hra = 1
    else:
        print("Zadal jste špatnou možnost, zkuste to znovu")
        main()
#while programu 0 => spuštěné/1 => konec
while hra == 0:
    main()
















