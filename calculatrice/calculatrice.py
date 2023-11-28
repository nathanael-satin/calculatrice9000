historique = []

def calculatrice():
    while True:
        print("\nCalculatrice")
        print("Entrez 'exit' pour quitter")
        print("Entrez 'historique' pour afficher l'historique")
        print("Entrez 'effacer' pour effacer l'historique")

        operation = input("Entrez l'opération (+, -, *, /) : ")
        
        if operation == 'exit':
            break
        elif operation == 'historique':
            if not historique:
                print("L'historique est vide.")
            else:
                print("\nHistorique :")
                for calcul in historique:
                    print(calcul)
        elif operation == 'effacer':
            historique.clear()
            print("L'historique a été effacé.")
        elif operation in ['+', '-', '*', '/']:
            try:
                nombre1 = float(input("Entrez le premier nombre : "))
                nombre2 = float(input("Entrez le deuxième nombre : "))
                
                if operation == '+':
                    resultat = nombre1 + nombre2
                elif operation == '-':
                    resultat = nombre1 - nombre2
                elif operation == '*':
                    resultat = nombre1 * nombre2
                elif operation == '/':
                    if nombre2 == 0:
                        print("Erreur : division par zéro")
                        continue
                    resultat = nombre1 / nombre2

                calcul = f"{nombre1} {operation} {nombre2} = {resultat}"
                historique.append(calcul)
                print(f"Résultat : {resultat}")
                
            except ValueError:
                print("Erreur : veuillez entrer des nombres valides.")
        else:
            print("Opération non reconnue. Veuillez réessayer.")

calculatrice()
