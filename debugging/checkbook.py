class Checkbook:
    """
    Classe représentant un carnet de chèques simple.

    Attributs :
        balance (float) : solde actuel du compte.

    Méthodes :
        deposit(amount) : ajoute un montant au solde.
        withdraw(amount) : retire un montant du solde si suffisant.
        get_balance() : affiche le solde actuel.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant sur le compte.

        Args:
            amount (float): montant à déposer.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant du compte s'il y a assez de fonds.

        Args:
            amount (float): montant à retirer.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Affiche le solde actuel."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale permettant d'interagir avec la classe Checkbook
    via une interface en ligne de commande.

    Commandes disponibles :
    - deposit : déposer de l'argent
    - withdraw : retirer de l'argent
    - balance : afficher le solde
    - exit : quitter le programme
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()