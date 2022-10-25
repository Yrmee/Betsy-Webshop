from models import (
    # import alle dingen los ipv *
    db,
    User,
    Tag,
    Product,
    OrderTransaction,
    UserProduct
)

import os


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_test_data():
    db.connect()
    print("Test Database Connected")
    db.create_tables([User, Tag, Product, UserProduct, OrderTransaction])

    # Fill with test Data for Database

    # Test User Data 

    users = [
        {'name': 'Obi-Wan Kenobi',
        'address': 'Stewjon',
        'payment': 1999},
        {'name': 'Leia Organa-Solo',
        'address': 'Alderaan',
        'payment': 1344},
        {'name': 'Ben Solo',
        'address': 'Chandrila',
        'payment': 2004},
        {'name': 'Rey',
        'address': 'Jakku',
        'payment': 8456},
    ]

    for user in users:
        User.create(
            name = user['name'],
            address = user['address'],
            payment = user['payment']
        )
    
    tags = [
        'food',
        'weapon',
        'transport',
        'clothes',
        'health',
        'droids'
    ]

    for tag in tags:
        Tag.create(tag = tag)

    products = [
        {'name': 'R2-D2',
        'description': 'Droid R2 Unit - R2 Series Astromech droid - R2-D2 is a diminutive droid, standing 0.96 meters tall.',
        'price': 2500.00,
        'quantity': 5,
        'tags': 'droids'},
        {'name': 'Millennium Falcon',
        'description': 'The Millennium Falcon (492727ZED) is a YT-1300 Corellian light freighter spaceship of the YT-1300f variety.',
        'price': 16000.00,
        'quantity': 5,
        'tags': 'transport'},
        {'name': 'Lightsaber',
        'description': 'The lightsaber is the weapon of a Jedi. The blade comes in the colors; green, blue, purple, yellow and red.',
        'price': 200.00,
        'quantity': 50,
        'tags': 'weapon'},
        {'name': 'Polystrarch portion bread',
        'description': 'Polystarch portion bread, also known as portion bread or simply polystarch, is a type of self-rising bread made by combining polystarch flour with water to trigger a chemical reaction.',
        'price': 3.50,
        'quantity': 350,
        'tags': 'food'},
        {'name': 'Mandalorian Armor',
        'description': "Mandalorian armor, known as beskar'gam in Mando'a, reffered to the traditional armor worn by the warrior clans of the planet Madalore. This armor includes a helmet with a T-shaped visor that concealed the face and armaments like whipcord throwers, flamethrowers and jetpacks.",
        'price': 655.50,
        'quantity': 15,
        'tags': 'clothes'},
        {'name': 'Blasters (DH-17 blaster pistol)',
        'description': 'The standard ranged weapon of both military personnel and civilians in the galaxy, the blaster pistol fires cohesive bursts of light-based energy called bolts.',
        'price': 75.50,
        'quantity': 890,
        'tags': 'weapon'},
        {'name': 'EOPIE',
        'description': "Easily domesticated, eopies serve Tatooine's settlers as transports and beasts of burden. These tough, desert-adapted quadrupeds can carry heavy loads, but are grumpy and stubborn.",
        'price': 280.00,
        'quantity': 25,
        'tags': 'transport'},
        {'name': 'Bacta Tank',
        'description': 'Bacta tanks are large vessels filled with a liquid healing agent and is used to treat seriously injured patients. To promote healing, patients are completely submerged and using breathing masks while recuperating.',
        'price': 750.00,
        'quantity': 150,
        'tags': 'health'},
    ]

    for product in products:
        Product.create(
            name = product['name'],
            description = product['description'],
            price = product['price'],
            quantity = product['quantity'],
            tags = product['tags'],
        )
    
    # User Product Data 
    user_products = [
        {'owner': 'Rey',
        'product': 'Polystrarch portion bread',
        'quantity': 1,
        'tags': 'food'},
        {'owner': 'Ben Solo',
        'product': 'Lightsaber',
        'quantity': 1,
        'tags': 'weapon'},
    ]

    for user_product in user_products:
        UserProduct.create(
            owner = user_product['owner'],
            product = user_product['product'],
            quantity = user_product['quantity'],
            tags = user_product['tags'],
        )
    

    db.close()
    print("Test Database Created")

if __name__ == "__main__":
    delete_database()
    populate_test_data()