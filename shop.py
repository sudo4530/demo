from classes import Category, Product

def category(username, password):
    Category.select()

    back = input("0. Back")
    if back == "0":
        return shop(username, password)


def products(username, password):
    Product.select()

    back = input("0. Back")
    if back == "0":
        return shop(username, password)

def shop(username, password):
    service = input(f"""
        1. Category
        2. Products
            >>> """)

    if service == "1":
        return category(username, password)

    elif service == "2":
        return products(username, password)