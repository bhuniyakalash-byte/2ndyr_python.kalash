# Payment Methods
class UPI:
    def pay(self, amount):
        print("Payment Successful using UPI")
        print("Amount =", amount)

class Card:
    def pay(self, amount):
        print("Payment Successful using Card")
        print("Amount =", amount)

# Context
class PaymentProcessor:
    def __init__(self, payment):
        self.payment = payment

    def process(self, amount):
        self.payment.pay(amount)

# Main Program
print("1. UPI")
print("2. Card")

choice = int(input("Enter choice: "))
amount = int(input("Enter amount: "))

if choice == 1:
    upi = input("Enter UPI ID: ")

    if "@" in upi:
        payment = UPI()
    else:
        print("Invalid UPI ID")
        exit()

elif choice == 2:
    card = input("Enter 16-digit Card Number: ")

    if len(card) == 16 and card.isdigit():
        payment = Card()
    else:
        print("Invalid Card Number")
        exit()

else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process(amount)