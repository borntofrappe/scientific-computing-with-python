class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output = f'{self.name.center(30, "*")}\n'
        for operation in self.ledger:
            description = operation['description'][:23].ljust(23)
            amount = f'{operation["amount"]:.2f}'[:7].rjust(7)
            output = f'{output}{description}{amount}\n'

        output = f'{output}Total: {self.get_balance()}'
        return output

    def get_balance(self):
        balance = 0
        for operation in self.ledger:
            balance = balance + operation['amount']

        return balance

    def check_funds(self, amount):
        balance = self.get_balance()

        return balance >= amount

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description,
        })

    def withdraw(self, amount, description=""):
        has_enough_funds = self.check_funds(amount)

        if has_enough_funds:
            self.ledger.append({
                'amount': amount * -1,
                'description': description,
            })

        return has_enough_funds

    def transfer(self, amount, category):
        has_enough_funds = self.check_funds(amount)

        if has_enough_funds:
            self.withdraw(amount, f"Transfer to {category.name}")

            category.deposit(amount, f"Transfer from {self.name}")

        return has_enough_funds


def create_spend_chart(categories):
    amounts = []
    total_amount = 0

    names = []
    max_length_name = 0

    dashes = '-' * (len(categories) * 3 + 1)
    width = len(dashes) + 4

    for category in categories:
        amount = 0
        for operation in category.ledger:
            if operation['amount'] < 0:
                amount = amount + abs(operation['amount'])

        amounts.append(amount)
        total_amount = total_amount + amount

        name = category.name
        names.append(name)
        length_name = len(name)
        if length_name > max_length_name:
            max_length_name = length_name

    percentages = []
    for amount in amounts:
        percentage = int(amount / total_amount * 100)
        percentages.append(percentage)

    output = 'Percentage spent by category\n'

    for point in range(11):
        row = ''
        percentage_point = (10 - point) * 10

        for percentage in percentages:
            character = percentage >= percentage_point and 'o' or ''
            row = f'{row}{character.center(3)}'

        output = f'{output}{str(percentage_point).rjust(3)}|{row} \n'

    output = f'{output}{dashes.rjust(width)}\n'

    for i in range(max_length_name):
        row = ''
        for name in names:
            character = ''
            if len(name) > i:
                character = name[i]

            row = f'{row}{character.center(3)}'

        output = f'{output}{row.rjust(width -1)} \n'

    return output.rstrip()


food = Category('Food')
clothing = Category('Clothing')
food.deposit(1000, 'Initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food items')
food.transfer(50, clothing)
print(food)

print()

energy = Category('Energy')
entertainment = Category('Entertainment')
business = Category('Business')
energy.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
energy.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([energy, business, entertainment]))
