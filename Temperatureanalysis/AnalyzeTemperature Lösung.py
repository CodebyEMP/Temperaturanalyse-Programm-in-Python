# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


"""
Programm : AnalyzeTemperaur
Version  : 1.1
Date     : 28/03/2023
Author   : Emmanuel Moji Peters
"""

print("Analyze Temperatur Version 1.1")

boExit = False;

while (boExit == False):
    print("------------------------")
    print("Hauptmenue")
    print("0 : Beenden")
    print("1 : Datei einlesen")
    print("")
    menue = input("Menueauswahl: ")
    print("------------------------")

    if (menue == "0"):
        boExit = True


    elif (menue == "1"):
        print("Jetzt die Datei einlesen")

        filename = input("Dateiname mit Pfad: ")  # z.B. ".\2021-01-15.txt"
        print("DerDateiname lautet: " + filename)

        file = open(filename)

        strMessID = file.readline()
        strMessDate = file.readline()
        strMessStart = file.readline()
        strMessNum = file.readline()
        strDummyLine = file.readline()

        print(strMessID)
        print(strMessDate)
        print(strMessStart)
        print(strMessNum)
        print(strDummyLine)
        print("--- Start eingelesene Werte ---")

        cnt = 0
        list = []
        iMessNum = int(strMessNum)

        for i in range(1, iMessNum + 1):
            line = file.readline()
            if line:
                cnt = i
                fValue = float(line)
                list += [fValue]
                print(str(cnt) + " : " + str(fValue))
            else:
                print('EOF')

        file.close()

        boExit2 = False
        while boExit2 == False:
            print("Erweiterungsmenü")
            print("0 : zurück ins Hauptmenü")
            print("2 : Durchschnittswert berechnen")
            print("3 : Höchste und niedrigste Temperatur")
            print("4 : Zeitraum von Überschreitungen ausgeben")
            menue2 = input("Menüauswahl eingeben: ")


            if (menue2 == "0"):
                boExit2 = True

            elif (menue2 == "2"):

                durchlauf = 0
                temp_sum = 0
                temp_durchschnitt = 0


                for i in range(0, len(list) ):
                    temp_sum += list[i]
                    durchlauf += 1
                temp_durchschnitt = temp_sum / durchlauf
                print("Durchschnitt der", len(list), "berechneten Werte ist", temp_durchschnitt)

            elif (menue2 == "3"):
                highest_temp = -9999
                lowest_temp = 9999
                for i in range(0, len(list) ):
                    if (list[i] > highest_temp):
                        highest_temp = list[i]
                    if (list[i] < lowest_temp):
                        lowest_temp = list[i]
                print("Höchste Temperatur die gemessen wurde ist", highest_temp,", die niedriste Temperatur die gemessen wurde ist", lowest_temp)

            elif (menue2 == "4"):
                def conv_min_to_time(a):
                    min = a % 60
                    hours = int(a/60)

                    print(hours, ":", min)
                    return(hours, min)

                counter = 0
                while counter < len(list):
                    if list[counter] < 20:
                        print("Temperatur unterschritten ab", conv_min_to_time(counter))
                        counter += 1
                        while list[counter] < 20:
                                counter += 1
                        if list[counter] >= 20:
                            print("Temperatur normalisiert ab", conv_min_to_time(counter))
                            counter += 1
                        else:
                            counter += 1

                    elif list[counter] > 26:
                        print("Temperatur überschritten ab",conv_min_to_time(counter))
                        counter += 1
                        while list[counter] > 26:
                            counter += 1
                        if list[counter] <= 26:

                            print("Temperatur normalisiert ab", conv_min_to_time(counter))
                            counter += 1
                        else:
                            counter += 1
                    else:
                        counter += 1
            else:
                print("Ungültige Auswahl!")
    else:
        print("Ungültige Auswahl!")

print(" ... und tschuess")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
