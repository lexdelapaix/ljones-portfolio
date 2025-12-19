#Leslie Jones
#Programming Project 1: AI ChatBot

def treebot_sales():
    #Ask for the customer's first and last name
    first_name = input("Welcome to TreeBot AI! What's your first name? ")
    last_name = input("And your last name? ")
    full_name = first_name + " " + last_name

    #Greet your customer using their full name.
    print(f"\nHello, {full_name}!")
    print("Thank you for visiting TreeBot AI. Where technology meets sustainability.\n")

    #Provide a few sentence overview of your Chatbot program.
    print("Welcome to TreeBot, your eco-conscious AI assistant!")
    print("TreeBot handles customer service, educates users on green living, and promotes environmental awareness.")
    print("From carbon footprint tracking to climate tips, TreeBot is the perfect partner for eco-forward businesses.\n")

    #Ask if your customer would like to make a purchase
    make_purchase = input("Would you like to purchase TreeBot licenses today? (yes/no): ").lower()

    if make_purchase == "yes":
        #Ask for their email address.
        #Ask for their phone number.
        email = input("Please enter your email address: ")
        phone = input("Please enter your phone number: ")

        #Ask for how many chatbot licenses they would like to purchase.
        licenses = int(input("How many TreeBot licenses would you like to purchase? "))
        license_price = 75
        license_total = licenses * license_price

        #Ask if they would also like to purchase an optional Gold Support plan that gets them priority support. 
        gold_support = input("Would you like to add the optional 'Gold Support Plan'? (yes/no): ").lower()
        support_cost = 0

        if gold_support == "yes":
            if licenses <= 50:
                support_cost = 500
            elif licenses <= 99:
                support_cost = 350
            else:
                support_cost = 250

        #Apply 10% tax for the total bill. 
        #Calculate the total amount due.
        subtotal = license_total + support_cost
        tax = subtotal * 0.10  # 10% tax
        total_due = subtotal + tax

        #Ask for a credit card information.
        card_number = input("Enter your credit card number: ")
        exp_date = input("Enter your card's expiration date (MM/YY): ")
        cvc = input("Enter the 3-digit CVC: ")
        zip_code = input("Enter your billing ZIP code: ")

        #Output a receipt using all of the variables you have input.
        print("\n======= Receipt from TreeBot AI =======")
        print(f"Customer: {full_name}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Card: {card_number}")
        print(f"Expiration: {exp_date}")
        print("-----------------------------------------")
        print(f"Licenses Purchased: {licenses}")
        print(f"Cost per License: ${license_price}")
        print(f"License Total: ${license_total:.2f}")
        print(f"Evergreen Support Plan: ${support_cost:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"Total Due: ${total_due:.2f}")
        print("==============================================")
        print("Thank you for supporting a greener future!")
        print("TreeBot will be planted digitally soon!\n")

    else:
        #If no - thank the customer by name and say goodbye. 
        print(f"\nThank you for considering TreeBot, {full_name}. ")
        print("Every step toward sustainability makes a world of a difference!")

    # Ask the customer if they would like to restart the ChatBot.
    restart = input("\nWould you like to restart the TreeBot demo? (yes/no): ").lower()
    if restart == "yes":
        treebot_sales()
    else:
        print("Thank you for visiting TreeBot AI, goodbye!")
treebot_sales()
