# Define a dictionary of fruits and their calorie counts.
fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
}

# Prompt the user to enter a fruit item and convert it to lowercase.
fruit = input("Item: ").lower()

# Iterate through the items in the 'fruits' dictionary.
for item in fruits:
    # Check if the entered fruit matches any item in the dictionary.
    if item == fruit:
        # If a match is found, print the calorie count for that fruit.
        print(f"Calories: {fruits[fruit]}")
        break