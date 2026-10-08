CHEMIN_DATA = "data/telco_churn.csv"

with open (CHEMIN_DATA, "r", encoding="utf-8") as fichier: 
    lignes = fichier.readlines()
    entete = lignes[0].strip().split(",")
    clients = lignes[1:]
    print("📄 En-tête du fichier :")
    print(entete)
    print("-"*50)

    print("📄 Les 3 premiers clients :")
    for i in range(3) :
        print(f"Client {i+1}")
        ligne = clients[i].strip().split(",")
        print(ligne) 
    print("-"*50)

    total_nb_yes = 0
    for client in clients :
        elements = client.strip().split(",")
        derniere_colonne = elements[-1]
        if derniere_colonne == "Yes" :
            total_nb_yes += 1 
    print(f"Nombre total de clients avec 'Yes' : {total_nb_yes}")
    taux_churn = (total_nb_yes/ len(clients) * 100)
    print(f"Le taux de churn est de  : {taux_churn:.1f} %")
    print(f"Le nombre de clients {len(clients)}")
    print(f"Le nombre de colonnes {len(entete)}")     
