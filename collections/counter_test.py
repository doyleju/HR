# Summary of collections.Counter:
# https://pymotw.com/2/collections/counter.html
# https://gist.github.com/bradmontgomery/4717521

from collections import Counter

# Need to calculate the total sum collected from shoe sales
sum = 0

# X number of shoes
X = 10

# Set of shoe sizes
available_shoes = Counter([2, 3, 4, 5, 6, 8, 7, 6, 5, 18])

# N number of customers
N = 6

# Customer orders: (size 6, €55), (size 6, €45) etc.
customer_orders = [(6, 55), (6, 45), (6, 55), (4, 40), (18, 60), (10, 50)]

# Work through customer orders and calculate the sum
for order in range(N):
    size, price = customer_orders[order]
    if available_shoes[size]:
        sum += price
        available_shoes.subtract({size: 1})

print (sum)
