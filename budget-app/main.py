class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

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


food = Category('food')
clothing = Category('clothing')

food.deposit(500)
print(food.get_balance())
food.transfer(400, clothing)
print(food.get_balance())
print(clothing.get_balance())
