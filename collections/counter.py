# Summary of collections.Counter:
# https://pymotw.com/2/collections/counter.html
# https://gist.github.com/bradmontgomery/4717521

from collections import Counter

# Need to calculate the total sum collected from shoe sales
sum = 0

# get number of shoes (X)
X = int(input())

# Create counter of all available shoe sizes
available_shoes = Counter(map(int, input().split(' ')))

# get number of customers (N)
N = int(input())

# Work through customer orders and calculate the sum
for order in range(N):
    size, price = map(int, input().split(' '))
    if available_shoes[size]:
        sum += price
        available_shoes.subtract({size: 1})
        
print (sum)
