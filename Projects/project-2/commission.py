print("Welcome to Dunder Mifflin!")
sales_made = 0
money_made = 0

while True:
    add_sale = str(input("Would you like to add a sale (y/n)?: "))
    if add_sale.lower() == "y":
        sale_type = str(input("paper or printer: "))
        if sale_type.lower() == "paper":
            paper_price = 10
            paper_commision = 0.15
            quantity = int(input("# of paper piles: "))
            amount = (paper_price * quantity) * paper_commision
            sales_made += 1
            money_made = money_made + amount
            print(f"You've made {int(money_made)} today with {sales_made} sales")
        elif sale_type.lower() == "printer":
            printer_price = 150
            printer_commission = 0.30
            quantity = int(input("# of printers: "))
            amount = (printer_price * quantity) * printer_commission
            sales_made += 1
            money_made = money_made + amount
            print(f"You've made {int(money_made)} today with {sales_made} sales")
        else:
            print("You did neither type in paper nor printer")
            print(f"You've made {int(money_made)} today with {sales_made} sales")
    else:
        break
