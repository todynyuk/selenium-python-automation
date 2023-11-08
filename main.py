import json


def fizz_buzz():
    user_number = int(input("Enter a number: "))

    for num in range(1, user_number + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# --------------------------Task 1
def print_json_count_records():
    with open('bank_information.json') as file:
        data = json.load(file)

    pretty_json = json.dumps(data, indent=4)

    print(pretty_json)

    item_dict = json.loads(pretty_json)
    print("Records count: ")
    print(len(item_dict['clients_data'][0]['users']))


# -------------------------Task 3

def decode_string(input_string):
    stack = []
    current_num = 0
    current_str = ""

    for char in input_string:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            last_str, repeat_count = stack.pop()
            current_str = last_str + current_str * repeat_count
        else:
            current_str += char

    return current_str


# -----------------------Task 4

def are_palindromes(str1, str2):
    def count_characters(input_string):
        char_count = {}
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

    char_count1 = count_characters(str1)
    char_count2 = count_characters(str2)

    return char_count1 == char_count2


# --------------------------------------Task 6
def find_combinations(coins, menu, current_combination, results):
    for item, price in menu.items():
        if coins >= price:
            new_coins = coins - price
            new_combination = current_combination + [item]
            if new_coins > 0:
                results.append(new_combination)
            if new_coins == 0:
                results.append(new_combination)
            else:
                find_combinations(new_coins, menu, new_combination, results)


def calculate_optimal_combinations(coins, menu):
    results = []
    find_combinations(coins, menu, [], results)
    return results


# Input parameters
coins = 400
menu = {
    "coffee": 100,
    "cake": 200,
    "popcorn": 225
}


# ------------------------------------------------------------------------------

def print_hi(name):
    print(f'Hi, {name}')
    print("Chose task: ")
    print("FizzBuzz-0")
    print("Calculate total amount of bank records for different users-1")
    print("")
    print("string_processing-3")
    print("are_palindromes-4")
    print("")
    print("combinations-6")
    print("Please input number: ")
    chose = int(input())

    # ----------------------------Task 0 --------------------------------
    if chose == 0:
        fizz_buzz()
    # -------------------------------------------------------------------
    # ----------------------------Task 1---------------------------------
    if chose == 1:
        print_json_count_records()
    # -------------------------------------------------------------------

    # ---------------------------Task 3---------------------------------
    if chose == 3:
        print("Input you request:\n")
        input_string = input()
        output_string = decode_string(input_string)
        print("Result: ", output_string)
    # ------------------------------------------------------------

    # -------------------------Task 4-----------------------------------
    if chose == 4:
        print("Please input first string: ")
        first_string = str(input())
        print("Please input second string: ")
        second_string = str(input())
        result = are_palindromes(first_string, second_string)
        print(result)
    # ------------------------------------------------------------------

    # ---------------------Task 6-----------------------------------------
    if chose == 6:
        combinations = calculate_optimal_combinations(coins, menu)

        if combinations:
            for i, combination in enumerate(combinations, 1):
                print(f"Combination {i}: {', '.join(combination)}")
        else:
            print("No valid combinations found.")
    # --------------------------------------------------------------------


if __name__ == '__main__':
    print_hi('PyCharm')
