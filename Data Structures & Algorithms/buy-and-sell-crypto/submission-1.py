class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        while len(prices) > 1:
            min_val = min(prices)
            max_val = max(prices)
            index_min = prices.index(min_val)
            index_max = prices.index(max_val)
            
            if index_min < index_max:
                return max_val - min_val

            print(min_val, max_val)
            print(index_max)
            remove_val = min_val if max(prices[index_min:len(prices)] or [min_val]) - min_val < max_val - min(prices[0:index_max] or [max_val]) else max_val
            prices.remove(remove_val)

        return 0