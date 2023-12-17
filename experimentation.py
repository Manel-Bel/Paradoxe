import datetime, random

#debut du challenge sur https://www.101computing.net/the-birthday-paradox/

#la listes des noms
listes_personnes = ["Manel","Aminata","Nafyssata","Antoinette","Lyes","Adrien","Gwen","Taous","Karima","Sabrina","Yannis","Melissa","Amar","Naila","Théo","Abdallah","Ines","Sofiane","Celena","Lydia","Ilyes","Nabila","Sofie"]


def generation_date():
    # nous generons une date entre "1/1/2002" et "31/12/2012"
    debut_periode = datetime.date(2002,1,1)
    fin_periode = datetime.date(2012,12,31)

    # le nombre de jours entre les deux dates
    nb_jours = (fin_periode - debut_periode).days
    #on choisie un nombre aleatoire de jours
    rd_jours = random.randint(0,nb_jours)

    #on crée notre date aleatoire en ajoutant le nombre de jours à la date du debut de la periode  
    return debut_periode + datetime.timedelta(days=rd_jours)


if __name__ == "__main__":
    # nb_personnes = 23

    anniversaires = {}

    for prenom in listes_personnes :
        date = generation_date()
        # on récupère que le mois et le jours de la date
        date1 = date.strftime("%d %b")
        anniversaires[prenom] = date1
        print(f'Prenom: {prenom} : {date1}')
    

    #verification des dates
    date_partage = {}

    for n,d in anniversaires.items():
        if d in date_partage:
            date_partage[d].append(n)
        else:
            date_partage[d] = [n]

    # recuperartion des dates en doublons
    doublons = {}
    for date, nom_list in date_partage.items() :
        if len(nom_list) > 1:
            doublons[date] = nom_list
    
    if doublons :
        for date, nom_list in doublons.items():
            print(f'La date {date} est partagée par : {nom_list}')
    else:
        print("Aucune date n'est partagée")
    