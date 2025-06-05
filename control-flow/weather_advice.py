# Ask the user about the weather
weather = input("what is the weather like today? ").strip().lower()
# provide clothing recommendations
if weather == "sunny":
    print("Wear a T-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have a recommendations for this weather.")
