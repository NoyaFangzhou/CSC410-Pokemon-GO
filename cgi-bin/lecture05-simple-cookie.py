#!/usr/bin/env python

# this code has been enhanced from the base demo given in class to include more complicated form submission types
# including drop-down lists, checkboxes, and a password field to hide the credit card number.
#
# note that this code is extraordinarily fragile.  things that will blow it up include:
#    a. not specifying a phone number
#    b. not specifying a credit card number
#    c. choosing 0 or 1 toppings
#    d. probably other things.
#  I will leave it as an exercise for the interested student to fix these errors.

print 'Content-Type: text/html'
print 'Set-Cookie: whatever=buffy_is_awesome'
print
print "<html>"
print "<head><title>Simple Cookie Test</title></head>"
print "<body>Simple cookie sent!</body>"
print "</html>"
