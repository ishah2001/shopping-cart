# shopping_cart.py
import os
from datetime import datetime


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

print("Welcome to the Shopping Cart Application. You will soon be asked to input product identifiers")
print("")
print("When you are done inputting product identifiers simply enter the word 'DONE'")
print("")

current_time = datetime.now()
current_time_formatted = current_time.strftime("%Y/%m/%d %I:%M:%p")

tax_rate = float(os.getenv("TAX_RATE", default=0.0875))
grocery_store_name = "ISHAAN'S GROCERY SHOP"
grocery_store_number = "333-675-4847"
matching_products = []

subtotal = 0


while True:

    # ASK FOR USER INPUT

    product_id = input("Please input a product identifier: ")
    
    if product_id == "DONE" or product_id == "Done" or product_id == "done":
        break

    if int(product_id) > len(products) or int(product_id) <= 0:
        print("Hey, are you sure that product identifier is correct? Please try again!")

    # LOOK UP CORRESPONDING PRODUCTS
    for x in products:
        if str(x["id"]) == str(product_id):
            # this is a match
            matching_products.append(x)
            subtotal = subtotal + x["price"]




#printing the receipt
print("")
print("----------------------------------------------")
print(grocery_store_name)
print(grocery_store_number)
print("----------------------------------------------")
print("CHECKOUT AT: " + current_time_formatted)
print("----------------------------------------------")
print("SELECTED PRODUCTS: ")

#printing all items
for x in matching_products:
    print("... " + x["name"] + " (" + to_usd(x["price"]) +") ")

#tax and total calculation
tax = subtotal * tax_rate
total = subtotal + tax

print("----------------------------------------------")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total))
print("----------------------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("----------------------------------------------")




