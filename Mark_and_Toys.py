"""
Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. There are a number 
of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the 
number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy?
"""

def maximumToys(prices, k):
    # sort with bubble sort
    for num_iterations in range(len(prices)-1,0,-1):
        for j in range(num_iterations):
            if prices[j] > prices[j+1]:
                tmp = prices[j]
                prices[j] = prices[j+1]
                prices[j+1] = tmp
    num_items = 0
    counter = 0
    while k > counter:
        counter += prices[num_items]
        num_items += 1

    return num_items-1



if __name__ == '__main__':

    n = 7 
    k = 50

    prices = [1, 12, 5, 111, 200, 1000, 10]
    result = maximumToys(prices, k)

    print(str(result) + '\n')

