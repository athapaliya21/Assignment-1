class SandwichMaker:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print("Sorry there is not enough " + item + ".")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(sandwich_size + " sandwich is ready. Bon appetit!")

    def show_report(self):
        print("Bread: " + str(self.machine_resources["bread"]) + " slice(s)")
        print("Ham: " + str(self.machine_resources["ham"]) + " slice(s)")
        print("Cheese: " + str(self.machine_resources["cheese"]) + " pound(s)")