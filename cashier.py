class Cashier:

    def process_coins(self):
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        return large_dollars * 1 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print("Here is $" + str(change) + " in change.")
        return True