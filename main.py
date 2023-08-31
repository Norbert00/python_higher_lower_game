import art
from game_data import data
import random


def print_logo():
    print(art.logo)


def print_vs():
    print(art.vs)


# * method generate a random number which will be use to extract random data from the object game_data
def generate_random_index():
    random_index = random.randint(0, 50)
    return random_index


# * method extract score from the game_data object for the chosen element
def compare_count(data_set, index):
    score = data_set[index]["follower_count"]
    return score


# * method extract values for the chosen element from the object game_data and return it as a list of string without score
def extract_data(data_set, index):
    values = list(data_set[index].values())
    del values[1]
    return values


# * method return chosen data form the object game_data as a formatted single string
def formatted_string(some_string):
    string = " ".join(map(str, some_string))
    return string


def print_massages_to_user(data_a, data_b, score):
    print_logo()
    print(f"Actual score: {score}")
    print(f"Compare A: {data_a}")
    print_vs()
    print(f"Against B: {data_b}")


def game():
    data_index_a = generate_random_index()
    data_index_b = generate_random_index()
    score_for_element_a = compare_count(data, data_index_a)
    score_for_element_b = compare_count(data, data_index_b)
    # print(f"score a : {score_for_element_a}, score b: {score_for_element_b}")
    data_compare_a = formatted_string(extract_data(data, data_index_a))
    data_compare_b = formatted_string(extract_data(data, data_index_b))
    user_score = 0
    user_choice = ""

    print_massages_to_user(data_compare_a, data_compare_b, user_score)

    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ")
        if score_for_element_a > score_for_element_b and user_choice == "a":
            user_score += 1
        elif score_for_element_a < score_for_element_b and user_choice == "b":
            user_score += 1
        else:
            print(f"You loose. Your score is {user_score}")
            break

        data_index_a = generate_random_index()
        data_index_b = generate_random_index()
        score_for_element_a = compare_count(data, data_index_a)
        score_for_element_b = compare_count(data, data_index_b)
        # print(f"score a : {score_for_element_a}, score b: {score_for_element_b}")
        data_compare_a = formatted_string(extract_data(data, data_index_a))
        data_compare_b = formatted_string(extract_data(data, data_index_b))

        print_massages_to_user(data_compare_a, data_compare_b, user_score)


game()
