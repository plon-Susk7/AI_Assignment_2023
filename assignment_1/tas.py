import random
import json

# Load data from knowledge_base.json
with open("knowledge_base.json", "r") as json_file:
    knowledge_base = json.load(json_file)

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
            temp = filter_places(places, filter_key, user_input, score_map, score)
            if temp:
                places = temp
        elif filter_key == "Season_to_visit":
            filtered_places = []
            for place in places:
                if user_input in place[filter_key]:
                    filtered_places.append(place)
            add_score(score_map, filtered_places, score)
            if filtered_places:
                places = filtered_places
        elif filter_key == "Rating":
            filtered_places = []
            for place in places:
                if float(user_input) <= place[filter_key]:
                    filtered_places.append(place)
            add_score(score_map, filtered_places, score)
            if filtered_places:
                places = filtered_places
        else:
            temp = filter_places(places, filter_key, user_input, score_map, score)
            if temp:
                places = temp
        
        printDetails(score_map)
        if places:
            print("We recommend the following places for you:")
            for place in places:
                print(place['Place'])

def add_new_destination():
    new_place = {}
    new_place['Place'] = input("Enter the place: ")
    new_place['Country'] = input("Enter the country: ")
    new_place['Continent'] = input("Enter the continent: ")
    new_place['Language'] = input("Enter the language: ").split()
    new_place['Currency'] = input("Enter the currency: ")
    new_place['Visa'] = input("Does the place require a visa? : ")
    new_place['Season_to_visit'] = input("Enter the season to visit: ").split()
    new_place['Expected_budget'] = input("Enter the expected budget: ")
    new_place['Rating'] = float(input("Enter the rating: "))
    new_place['feedback'] = []
    new_place['Activities'] = input("Enter the activities: ").split()
    
    # Add the new place to the knowledge_base list
    knowledge_base.append(new_place)
    
    # Write the updated knowledge_base list back to the JSON file
    with open("knowledge_base.json", "w") as json_file:
        json.dump(knowledge_base, json_file, indent=4)
    
    print("New destination added successfully!")


def add_feedback():
    place_name = input("Enter the place: ")
    feedback_text = input("Enter the feedback: ")
    rating = float(input("Enter the rating: "))
    
    for place in knowledge_base:
        if place['Place'] == place_name:
            place['feedback'].append(feedback_text)
            place['Rating'] = (place['Rating'] + rating) / place['reviewers']
            
            # Write the updated knowledge_base list back to the JSON file
            with open("knowledge_base.json", "w") as json_file:
                json.dump(knowledge_base, json_file, indent=4)
            
            print("Feedback added successfully!")
            return
    
    print("Place not found. Please try again.")
    add_feedback()


def main():
    print("Welcome to Travel Agency System")
    print("Please choose one of the following options:")
    print("1. Recommend destination")
    print("2. Add new destination")
    print("3. Add feedback")
    print("4. Exit")
    
    while True:
        option = input("Enter your option: ")
        if option == "1":
            recommend_destination()
            exit()
        elif option == "2":
            add_new_destination()
        elif option == "3":
            add_feedback()
        elif option == "4":
            print("Thank you for using Travel Agency System")
            exit()
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
