#!/usr/bin/env python

import sqlite3

conn = sqlite3.connect('pizza_orders.db')

c = conn.cursor()



c.execute('DROP TABLE IF EXISTS pizza_orders')

c.execute('CREATE TABLE IF NOT EXISTS pizza_orders(name varchar(100) primary key, size varchar(10), crust varchar(100), toppings varchar(100), phone varchar(100), credit_card varchar(100))')

c.execute('INSERT INTO pizza_orders VALUES("Bobby", "small", "thin", "pepperoni", "123-456-7890", "1234-5678-9012-3456")')


conn.commit()

conn.close()

print 'Content-Type: text/html'
print
print '''<html>
    <head>
        <title>Created Database</title>
    </head>
    <body>
        Database created successfully.
    </body>
</html>'''

