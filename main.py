# CONVERTISSEUR POUCES <-> cm




pouces = 0.394
cm = 2.54


# Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
choix = input("Souhaitez-vous convertir de pouces vers cm (1) ou de cm vers pouce (2) ?")
while choix != "1" and choix != "2":
        print("Choix invalide. Veuillez choisir 1 ou 2.")
        choix = input("Souhaitez-vous convertir de pouces vers cm (1) ou de cm vers pouce (2) ?")

# Demander à l'utilisateur de rentrer la valeur à convertir
if choix == "1":
        pouces = float(input("Entrez la valeur en pouces : "))
        valeur_cm = pouces * cm
        # Afficher la valeur convertie (et l'unité : cm )
        print(f"{pouces} pouces équivalent à {valeur_cm} centimètres.")

# Demander à l'utilisateur de rentrer la valeur à convertir
elif choix == "2":
    cm = float(input("Entrez la valeur en centimètres : "))
    valeur_pouces = cm * pouces
    # Afficher la valeur convertie (et l'unité : pouces)
    print(f"{cm} centimètres équivalent à {valeur_pouces} pouces.")
















