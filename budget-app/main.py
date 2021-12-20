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


food = Category('Food')
clothing = Category('Clothing')
food.deposit(1000, 'Initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food items')
food.transfer(50, clothing)
print(food)
