import data
import sandwich_maker
import cashier

resources = data.resources
recipes = data.recipes

machine = sandwich_maker.SandwichMaker(resources)
payment = cashier.Cashier()

is_on = True

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        machine.show_report()

    elif choice in recipes:
        ingredients = recipes[choice]["ingredients"]
        cost = recipes[choice]["cost"]

        if machine.check_resources(ingredients):
            coins = payment.process_coins()
            if payment.transaction_result(coins, cost):
                machine.make_sandwich(choice, ingredients)
