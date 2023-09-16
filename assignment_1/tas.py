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
    
def printDetails(score):
    for key, value in score.items():
        print(key, value)

def add_score(score_map, places, score):
    for place in places:
        if place['Place'] in score_map:
            score_map[place['Place']] += score
        else:
            score_map[place['Place']] = score

def filter_places(places, question, answer, score_map, score):
    filtered_places = []
    for place in places:
        print(place)
        if place[question] == answer:
            filtered_places.append(place)
    add_score(score_map, filtered_places, score)
    return filtered_places

def recommend_destination():
    # creating a dictionary to add points for each question and places
    score_map = {}
    places = knowledge_base

    questions = [
        ("Do you need a visa? ", "Visa", "Yes", 1),
        ("Enter your expected budget: ", "Expected_budget", None, 1),
        ("Enter the season you want to visit: ", "Season_to_visit", None, 1),
        ("Enter the continent you want to visit: ", "Continent", None, 1),
        ("Enter the language you want to use: ", "Language", None, 1),
        ("Enter the activities you want to do (space-separated activities): ", "Activities", None, 1),
        ("Enter the minimum rating you want: ", "Rating", None, 1)
    ]

    for question, filter_key, answer, score in questions:
        user_input = input(question)
        if filter_key == "Expected_budget":
            places = filter_places(places, filter_key, user_input, score_map, score)
        elif filter_key == "Season_to_visit":
            filtered_places = []
            for place in places:
                if user_input in place[filter_key]:
                    filtered_places.append(place)
            add_score(score_map, filtered_places, score)
            places = filtered_places
        elif filter_key == "Rating":
            places = filter_places(places, filter_key, float(user_input), score_map, score)
        else:
            places = filter_places(places, filter_key, user_input, score_map, score)
        
        printDetails(score_map)


        if places:
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
