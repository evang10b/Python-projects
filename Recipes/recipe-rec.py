# Main function that recomends a recipie based on users input
def main():
    print("Looking for good allergy recommendations but you have allergies.")
    print("Just your luck I am here to help.")
    allergies = input("Do you have any allergies? (Yes or No): ").lower().strip()
    if allergies == "yes":
        extra_algy = input("Do you have another allergy (Yes or No): ").lower().strip()
    
    if allergies == "yes" and extra_algy == "no":
        s_allergies = input("Choose from list: Nuts, Milk, Eggs, Other: ").lower().strip()

        if s_allergies == "nuts":
            recommend(*nut_free)
            prefrences("Cheese scones")
        elif s_allergies == "milk":
            recommend(*milk_free)
            prefrences("Cinnamon and apple trail mix")
        elif s_allergies == "eggs":
            recommend(*egg_free)
            prefrences("Teriyaki Salmon")
        else:
            print("More allergies added soon")
    # Adding 2 allergies
    elif allergies == "yes" and extra_algy == "yes":
        t_allergies = input("Choose 1st allergy from list: Nuts, Milk, Eggs, Other: ").lower().strip()
        a_allergies = input("Choose 2nd allergy from list: Nuts, Milk, Eggs, Other: ").lower().strip()
        if t_allergies == "nuts" and a_allergies == "milk" or t_allergies == "milk" and a_allergies == "nuts":
            recommend(*nutmilk_)
            prefrences("Avocado Chocolate Pudding")
        elif t_allergies == "nuts" and a_allergies == "eggs" or t_allergies == "eggs" and a_allergies == "eggs":
            recommend(*nutegg_)
            prefrences("Error: There arent any")
        elif t_allergies == "milk" and a_allergies == "eggs" or t_allergies == "eggs" and a_allergies == "milk":
            recommend(*milkegg_)
            prefrences("Error: There arent any")
        else:
            print("More allergies added soon")
    
    else:
        print("Why you here then. Get out. It was a trick question")

# List of nut free dessert
nut_free = [("""
    ======================
    1. Cheese sconces:
    - Duration: 35 minutes
    - Key ingredients: Cheddar cheese,
    Flour, Butter
    ======================
"""),
            ("""
    ======================
    2. Canberry and coconut cereal bars:
    - Duration: 2 hours
    - Key ingredients: Dried Canberries,
    Dessicated Coconuts, Crisped Rice 
    Cereals, Oats
    ======================
"""),
            ("""
    ======================
    3. Banana Chips:
    - Duration: 2 hours approx.
    - Key ingredients: Banana, Oil
    ======================
"""),
            ("""
    ======================
    4. Pitta Pizzas
    - Duration: 45 minutes
    - Key ingredients: Pitta Bread, Tomato,
    Cheese
    ======================
""")]
# List of Milk free dessert
milk_free = [("""
    ======================
    Apple Cinnamon Trail Mix:
    - Duration: 5 minutes
    - Key ingredients: Apple cinnamon
    cherios, variety of nuts
    ======================\n
"""),
             ("""
    ======================
    Spicy tortilla chips with pomegranate
    hummus:
    - Duration: 15 minutes
    - Key ingredients: Spices, Tortilla,
    pomegranate seeds
    ======================\n
"""),
             ("""
    ======================
    Banana Chips:
    - Duration: 2 hours
    - Key ingredients: Banana, Oil
    ======================\n
"""),
             ("""
    ======================
    Roasted Spicy Sweet Potato:
    - Duration: 40 minutes
    - Key ingredients: Sweet potatoes,
    Spices
    ======================
""")]
# List of Egg free dessert
egg_free = [("""
    ======================
    Banana Chips:
    - Duration: 2 hours approx.
    - Key ingredients:
    ======================\n
"""),
            ("""
    ======================
    Spicy Sweet Potato:
    - Duration: 40 minutes
    - Key ingredients: Sweet potatos,
    Spices
    ======================\n
"""),
            ("""
    ======================
    Chicken satay:
    - Duration: 40 minutes
    - Key ingredients: Chicken,
    Spices, Honey
    ======================\n
"""),
            ("""
    ======================
    Teriyaki Salmon:
    - Duration: 40 minutes
    - Key ingredients: Teriyaki,
    Salmon
    ======================
""")]

# Nut and Milk free dessert
nutmilk_ = [("""
    ======================
    Banana Chips:
    - Duration: 2 hours approx.
    - Key ingredients: Banana,
    Oil
    ======================\n
"""),
            ("""
    ======================
    Chocolate Water Cake:
    - Duration: 50 minutes
    - Key ingredients: Cocoa Powder,
    Water
    ======================\n
"""),
            ("""
    ======================
    Homemade Baked Apples:
    - Duration: 1 hour
    - Key ingredients: Apple
    ======================\n
"""),
            ("""
    ======================
    Avocado Chocolate Pudding:
    - Duration: 10 minutes
    - Key ingredients:
    =====================
""")]
# Nut and egg free dessert
nutegg_ = [("""
    ======================
    Rice Pudding:
    - Duration: 2 hours
    - Key ingredients: Rice pudding,
    Nutmeg(NOT a nut)
    ======================\n
"""),
           ("""
    ======================    
    Panna Cotta:
    - Duration: 7+ hours
    - Key ingredients: Milk, Cream,
    Gelatine Powder, Vanilla
    ======================\n
"""),
           ("""
    ======================
    Oatmeal Crescent:
    - Duration: 2-3 hours
    - Key inredients: Oats
    ======================\n
"""),
           ("""
    ======================
    Depression Cake:
    - Duration: 40 minutes
    - Key ingredients: Cocoa Powder
    ======================
""")]
# Milk and egg free dessert
milkegg_ = [("""
    ======================
    Berry Crumbles: 
    - Duration: 45 minutes to 1 hour
    - Key ingredients: Berries, Sugar,
      Mangerine, Cornstarch
    ======================\n
"""),
           ("""
    ======================
    Banana Chips:
    - Duration: 2 hours approx.
    - Key ingredients: Bananas, Oil
    ======================\n
"""),
           ("""
    ======================
    Fruit sorbets:
    - Duration: 6 hours
    - Key ingredients: Fruit of your 
      choice, Honey, lemon juice, Water
    ======================\n
"""),
           ("""
    ======================
    Apple Cinnamon Crisps:
    - Duration: 2 hours
    - Key Ingredients: Apples, Cinnamon
    ======================
""")]

# Prefrencing function
def prefrences(recipe):
    pref_reci = input("Do you only want a quick meal? (Yes or No) ").lower().strip()
    if pref_reci == "yes":
        print("Then this is just for you:", recipe)
    else:
        print("Enjoy the options that were given")

# Recommendation function
def recommend(r1, r2, r3, r4):
    print("You might like:\n" + r1 + r2 + r3 + r4)

main()