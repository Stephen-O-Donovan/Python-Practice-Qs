#!/usr/bin/python

class Solution:

    def __init__(self, prices):
        self.prices = prices
    def get_prices(self):
        return self.prices

    def maxProfit(self) -> int:
        maxSale = 0
        minPrice = float('inf')
        prices = self.get_prices()
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxSale:
                maxSale = prices[i] - minPrice
        return maxSale

        # hashmap = {}
        # for i in range(len(self.prices)):
        #     hashmap[self.prices[i]] = i
        #     if(self.prices[i] > maxSale):
        #         maxSale = self.prices[i]
        #     if(minPrice == 0 or minPrice > self.prices[i]):
        #         minPrice = self.prices[i]
        # for i in self.prices[minPrice+1:]:
        #     if i > maxSale:
        #         maxSale = i
        # maxProfit = maxSale - minPrice
        # if(hashmap[maxProfit] > hashmap[minPrice] and maxProfit> 0):
        #     return maxProfit
        # else:
        #     return 0
            
            

if __name__ == '__main__':
    p1 = Solution([7,1,5,3,6,4])
    print("p1 max profit: " , p1.maxProfit())
    p2 = Solution([7,6,4,3,1])
    print("p2 max profit: " , p2.maxProfit())

 