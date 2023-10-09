tax_rate = 0.07
tip_rate = 0.18

def get_sales_tax(bill):
    tax = bill * tax_rate
    print("Sales tax: %.2f" % tax)
    return tax

def get_tip(bill):
    tip = bill * tip_rate
    print("Tip: %.2f" % tip)
    return tip

def main():
    bill = float(input("Input the cost of the meal: "))
    tax = get_sales_tax(bill)
    tip = get_tip(bill)
    bill = bill + tax + tip
    print("Total: %.2f" % bill)
    return bill

main()

