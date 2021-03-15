# 1 - imports
from daos.cart_dao import CartDAO
from db import Session

# 2 - extract a session
session = Session()

carts = session.query(DeliveryDAO).all()

# 4 - print deliveries' details
print('\n### All cart items:')
for items in carts:
    print(f'{items.id}')
print('')
