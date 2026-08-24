from info_recipies import nutegg_, nutmilk_, milkegg_, nut_free, milk_free, egg_free
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