def verifier_mot_de_passe(mdp):
    score = 0
    retour = []

    # CRITÈRE 1 : Longueur (au moins 8 caractères)
    if len(mdp) >= 8:
        score += 1
    else:
        retour.append("Min 8 caracteres")

    # CRITÈRE 2 : Majuscule
    if any(c.isupper() for c in mdp):
        score += 1
    else:
        retour.append("Ajoute une majuscule")

    # CRITÈRE 3 : Minuscule
    if any(c.islower() for c in mdp):
        score += 1
    else:
        retour.append("Ajoute une minuscule")

    # CRITÈRE 4 : Chiffre
    if any(c.isdigit() for c in mdp):
        score += 1
    else:
        retour.append("Ajoute un chiffre (0-9)")

    # CRITÈRE 5 : Caractère spécial
    specials = "!@#$%^&*()_+=-|{}[]:;<>,.?"
    if any(c in specials for c in mdp):
        score += 1
    else:
        retour.append("Ajoute un caractere special (!@#...)")

    return score, retour

# --- Partie Affichage ---
print("=== Verificateur de Mot de Passe ===")
mdp = input("Entrez votre mot de passe : ")

score, conseils = verifier_mot_de_passe(mdp)

print(f"\nScore : {score}/5")

# Détermination du niveau selon le score
if score == 5:
    print("Niveau : Tres fort")
elif score == 4:
    print("Niveau : Fort")
elif score == 3:
    print("Niveau : Moyen")
elif score == 2:
    print("Niveau : Faible")
else:
    print("Niveau : Tres faible")

# Affichage des conseils si nécessaire
if conseils:
    print("\nConseils pour ameliorer :")
    for conseil in conseils:
        print("-", conseil)

a


