__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from datetime import datetime


def search(term):
    """
    Search for products based on a term. 
    Searching for 'sweater' should yield all products that have the word 'sweater' in the name. 
    This search should be case-insensitive.
    """
    term = term.lower()
    search_query = Product.select().where(Product.name.contains(term) | Product.description.contains(term))
    if search_query:
        print(f"\nProducts found based on your search term: {term}")
        for product in search_query:
            print(f"- {product.name}")
    else:
        print(f"\nNo products are found for: {term}")



def list_user_products(user_id):
    """
    View the products of a given user.
    """
    user_product_list_query = UserProduct.select().where(UserProduct.owner == user_id)
    if user_product_list_query:
        print(f"{user_id}'s Product List: ")
        for product in user_product_list_query:
            print(f"- {product.product}")
    else:
        print(f"No user found for: {user_id}")



def list_products_per_tag(tag_id):
    """
    View all products for a given tag.
    """
    products_list_per_tag_query = Product.select().where(Product.tags == tag_id)
    if products_list_per_tag_query:
        print(f"\nProducts found by tag: {tag_id} ")
        for product in products_list_per_tag_query:
            print(f"- {product.name}")
    else: 
        print(f"\nNo products are found with tag: {tag_id}")



def add_product_to_user(user_id, product):
    """
    Add a product to a user.
    """
    get_product_query = Product.select().where(Product.name == product)
    get_user_query = User.select().where(User.name == user_id)

    if get_product_query and get_user_query:
        new_product = UserProduct.create(
            owner = user_id,
            product = product,
            quantity = 1,
            #tags = Product.tags
        )
        print(f"{product} is now added to user {user_id}.")
        return new_product
    else:
        print("No user of product are found.")



def remove_product_from_user(product_id):
    """
    Remove a product from a user.
    """
    try:
        product = UserProduct.get(UserProduct.product == product_id)
        print(f"{product_id} has been removed.")
        return product.delete_instance()
    except DoesNotExist:
        print("No products are found.")



def update_stock(product_id, new_quantity):
    """
    Update the stock quantity of a product.
    """
    update_product_stock = Product.get(Product.name == product_id)
    if update_product_stock:
        print(f"PRODUCT:\t{update_product_stock.name}")
        print(f"PREV STOCK:\t{update_product_stock.quantity}")
        update_product_stock.quantity = new_quantity
        update_product_stock.save()
        #print(f"Product name: {update_product_stock.name}")
        print(f"UPDATE STOCK:\t{update_product_stock.quantity}")
    else:
        print("No products are found.")



def purchase_product_between_users(product_id, buyer_id, quantity):
    """
    Handle a purchase between a buyer and a seller for a given product.
    """
    user_of_purchase = User.get(User.name == buyer_id)
    product_of_purchase = Product.get(Product.name == product_id)

    if user_of_purchase and product_of_purchase:
        # set date for order transaction
        current_date = datetime.now().date()
        get_date = datetime.strftime(current_date, "%d-%m-%Y")
        # set check for excisting amount of stock
        quantity_stock_check = product_of_purchase.quantity - quantity
        if quantity_stock_check >= 0:
            order = OrderTransaction.create(
                date = get_date,
                user = buyer_id,
                product = product_id,
                quantity = quantity
            )
            print("-" * 35)
            print("ORDER TRANSACTION: ")
            print(f"DATE:\t\t{order.date}\nCLIENT:\t\t{order.user}\nPRODUCT:\t{order.product}\nAMOUNT:\t\t{order.quantity}")

            print("\n")
            add_product_to_user(buyer_id, product_id)
            print("\n")
            list_user_products(buyer_id)

            if quantity_stock_check == 0:
                return remove_product_from_user(product_id)
            print("\nSTOCK UPDATE:")
            return update_stock(product_id, quantity_stock_check)
        else:
            print("Amount not in stock.")
    else:
        print("User or products not found.")


def main():
    db.connect()
    print("\nDatabase Connected\n")

    # test data here

    """
    View the result per code block, not all at once.
    This way, the results remains clear in the terminal.
    """

    # --> search()
    search('weapon')
    search('bread')
    search('spaceship')
    search('star destroyer')


    # --> list_user_products()
    #list_user_products('Rey')
    #list_user_products('Ben Solo')
    #list_user_products('Darth Vader')


    # --> list_products_per_tag()
    #list_products_per_tag('droids')
    #list_products_per_tag('transport')
    #list_products_per_tag('health')
    #list_products_per_tag('vader')



    # - User: 'Rey'
    # --> add_product_to_user() 
    #list_user_products('Rey')
    #add_product_to_user('Rey', 'Mandalorian Armor')
    #list_user_products('Rey')

    # --># remove_product_from_user() 
    #list_user_products('Rey')
    #remove_product_from_user('Mandalorian Armor')
    #list_user_products('Rey')



    # - User: 'Ben Solo'
    # --> add_product_to_user() 
    #list_user_products('Ben Solo')
    #add_product_to_user('Ben Solo', 'Millennium Falcon')
    #list_user_products('Ben Solo')

    # --> remove_product_from_user()
    #list_user_products('Ben Solo')
    #remove_product_from_user('Millennium Falcon')
    #list_user_products('Ben Solo')



    # --> update_stock()
    #update_stock('EOPIE', 200)



    # --> purchase_product_between_users()
    #purchase_product_between_users('Polystrarch portion bread', 'Ben Solo', 1)
    #purchase_product_between_users('Lightsaber', 'Rey', 1)
    #list_user_products('Rey')
    #list_user_products('Ben Solo')


    print("\nDatabase Disconnected\n")
    db.close()

if __name__ == "__main__":
    main()