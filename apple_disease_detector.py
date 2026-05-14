# Opening
print("================================================================================")
print("|          Welcome to the Apple Tree Disease Detection Program                 |")
print("================================================================================")

print("Please enter your identity")
name = input("Name\t: ")

print("Type 'next' to begin.")
start = input("Next\t: ")

# Examination
print("--------------------------------------------------------------------------------------------------------------")
print("")
print(f"Hello, {name}. Please answer the following questions based on the current condition of your apple tree.")
print("")
print("--------------------------------------------------------------------------------------------------------------")

ind1 = input("-> Are there any changes on the leaves? (yes/no): ")
if ind1 == "yes":
    g1 = input("-> Are the leaves falling off? (yes/no): ")
    if g1 == "yes":
        p = "LD"
    elif g1 == "no":
        p = "U"
    else:
        print("Invalid input.")
    g2 = input("-> Are there black spots appearing on the leaves? (yes/no): ")
    if g2 == "yes":
        p = "LD"
    elif g2 == "no":
        p = "U"
    else:
        print("Invalid input.")
    g3 = input("-> Are there white patches on the leaves during defoliation? (yes/no): ")
    if g3 == "yes":
        p = "LD"
    elif g3 == "no":
        p = "U"
    else:
        print("Invalid input.")
elif ind1 == "no":
    pass
else:
    print("Invalid input.")

print(" ")
ind2 = input("-> Are there any changes on the stem? (yes/no): ")
if ind2 == "yes":
    g4 = input("-> Does the stem surface appear to be rotting? (yes/no): ")
    if g4 == "yes":
        p = "CC"
    elif g4 == "no":
        p = "U"
    else:
        print("Invalid input.")
    g5 = input("-> Is the stem surface oozing liquid? (yes/no): ")
    if g5 == "yes":
        p = "CC"
    elif g5 == "no":
        p = "U"
    else:
        print("Invalid input.")
elif ind2 == "no":
    pass
else:
    print("Invalid input.")

print(" ")
ind3 = input("-> Are there any changes on the fruit? (yes/no): ")
if ind3 == "yes":
    g6 = input("-> Has the fruit surface turned brown? (yes/no): ")
    if g6 == "yes":
        p = "CC"
    elif g6 == "no":
        p = "U"
    else:
        print("Invalid input.")
    g7 = input("-> Does the fruit appear to be rotting? (yes/no): ")
    if g7 == "yes":
        p = "CC"
    elif g7 == "no":
        p = "U"
    else:
        print("Invalid input.")
elif ind3 == "no":
    pass
else:
    print("Invalid input.")

print(" ")

# Examination Results
print("--------------------------------------------------------------------------------------------------------------")
print("|------------------------------------------EXAMINATION RESULTS----------------------------------------------|")
print("--------------------------------------------------------------------------------------------------------------")
print(" ")

if p == "U":
    print()
    print(f"Hello, {name}. We are sorry, but the examination could not detect a specific disease. Please consult an apple disease expert.")
elif p == "LD":
    print("")
    print(f"Hello, {name}. The examination has detected that the apple tree is infected with Leaf Blight.")
    print("")
    print("To control Leaf Blight, remove and burn the affected parts and apply fungicide.")
    inf = input("Would you like to know more information about this disease? (yes/no): ")
    if inf == "yes":
        print(" ")
        print("                                        DEFINITION                                             ")
        print("...............................................................................................")
        print("| Leaf Blight, or Marssonina coronaria J.J. Davis, is a fungal disease. Symptoms include     |")
        print("| leaf drop, white patches during defoliation, and black spots on the leaves.                |")
        print("...............................................................................................")
        print(" ")
        print("                                    SPREADING PROCESS                                         ")
        print("...............................................................................................")
        print("| Irregular spots first appear on the leaves, followed by black spots that spread from old   |")
        print("| leaves to young leaves, eventually causing leaf drop.                                      |")
        print("...............................................................................................")
        print(" ")
    else:
        pass
elif p == "CC":
    print("")
    print(f"Hello, {name}. The examination has detected that the apple tree is infected with Canker.")
    print("")
    print("To control Canker, harvest the fruit before it is fully ripe and apply fungicide.")
    inf = input("Would you like to know more information about this disease? (yes/no): ")
    if inf == "yes":
        print(" ")
        print("                                        DEFINITION                                             ")
        print("...............................................................................................")
        print("| Canker is a fungal disease caused by Botryosphaeria ribis Gross. It attacks the stem and   |")
        print("| fruit. Symptoms include rotting stem and fruit, liquid oozing from the stem, and brownish  |")
        print("| discoloration of the fruit.                                                                |")
        print("...............................................................................................")
        print(" ")
        print("                                    SPREADING PROCESS                                         ")
        print("...............................................................................................")
        print("| The stem begins to ooze liquid and rot, while brown patches appear on the fruit and spread |")
        print("| across the entire surface, causing it to rot completely.                                   |")
        print("...............................................................................................")
        print(" ")
    else:
        pass
else:
    print("Not detected.")

print(" ")

# Reference
ref = input("Would you like to see the references used? (yes/no): ")
if ref == "yes":
    print("Sastrahidayat, I. R. & Djauhari, S. (2013). Penyakit dan Hama Apel serta Cara Pengendaliannya. Brawijaya Press. Malang.")
elif ref == "no":
    print("Alright. Thank you for using our program!")
else:
    print("Invalid input.")

import datetime
x = datetime.datetime.now()
print("Consultation conducted on:", x.strftime("%c"))
print("--------------------------------------------------------")
print("Program created by Yaya.")
print("Thank you <3")
