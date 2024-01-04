class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        i = 0
        maxCandy = max(candies)
        for i in range(len(candies)):

            if candies[i]+extraCandies >= maxCandy:
                candies[i] = True
            else:
                candies[i] = False
            i += 1
        return candies
