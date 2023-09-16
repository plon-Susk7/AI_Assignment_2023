from knowledge_base import knowledge_base


'''
    'Place' : 'Montreal',
    'Country' : 'Canada',
    'Continent' : 'North America',
    'Language' : ['French', 'English'],
    'Currency' : 'Canadian Dollar',
    'Visa' : 'Yes',
    'Season_to_visit': ['Summer', 'Autumn'],
    'Expected_budget' : 'Medium',
    'Rating' : random.uniform(3.5, 5.0),
    'feedback' : [],
    'Activites' : []
'''

def no_place(data):
    if len(data) == 0:
        print("Sorry, we cannot recommend any place for you.")
        return True
    
def printDetails(places):

    for place in places:
        print("Place: ", place['Place'])
        print("Country: ", place['Country'])
        print("Continent: ", place['Continent'])
        print("Language: ", place['Language'])
        print("Currency: ", place['Currency'])
        print("Visa: ", place['Visa'])
        print("Season to visit: ", place['Season_to_visit'])
        print("Expected budget: ", place['Expected_budget'])
        print("Rating: ", place['Rating'])
        print("Activities: ", place['Activities'])
        print("Feedback: ", place['feedback'])
        print("\n")

def recommend_destination():

    visa = input("Do you need a visa? ")
    # filtering places based on visa criteria first
    if visa == "Yes":
        places = list(filter(lambda x: x['Visa'] == "Yes", knowledge_base))
    no_place(places)
    printDetails(places)
    
    # filtering places based on expected budget
    expected_budget = input("Enter your expected budget: ")
    for place in places:
        if place['Expected_budget'] != expected_budget:
            places.remove(place)
    
    no_place(places)
    printDetails(places)
    
    # filtering places based on season to visit
    season_to_visit = input("Enter the season you want to visit: ")
    for place in places:
        if season_to_visit not in place['Season_to_visit']:
            places.remove(place)
            
    no_place(places)
    printDetails(places)
    
    # filtering places based on continent
    continent = input("Enter the continent you want to visit: ")
    for place in places:
        if place['Continent'] != continent:
            places.remove(place)

    no_place(places)
    printDetails(places)
    
    # filtering places based on language
    language = input("Enter the language you want to use: ")
    for place in places:
        if language not in place['Language']:
            places.remove(place)

    no_place(places)
    printDetails(places)
    
    # filtering places based on activities
    activites = input("Enter the activities you want to do( space separated activities ): ").split(' ')
    for place in places:
        if activites not in place['Activities']:
            places.remove(place)
    
    no_place(places)
    printDetails(places)
    
    # filtering places based on rating
    rating = input("Enter the minimum rating you want: ")
    for place in places:
        if place['Rating'] < rating:
            places.remove(place)

    no_place(places)
    printDetails(places)
    
    # if we reach here, we have at least one place to recommend
    print("We recommend the following places for you:")
    for place in places:
        print(place['Place'])






def add_new_destination():
    pass


def add_feedback():
    pass


def main():
    # <---------------------------------------------------> #
    print("Welcome to Travel Agency System")
    print("Please choose one of the following options:")
    print("1. Recommend destination")
    print("2. Add new destination")
    print("3. Add feedback")
    print("4. Exit")
    # <---------------------------------------------------> #
    option = input("Enter your option: ")
    if option == "1":
        recommend_destination()
    elif option == "2":
        add_new_destination()
    elif option == "3":
        add_feedback()
    elif option == "4":
        print("Thank you for using Travel Agency System")
        exit()
    else:
        print("Invalid option. Please try again.")
        main()


    


main()
