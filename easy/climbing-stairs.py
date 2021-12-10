
class Solution:
    cache = {}
    def climbStairs(self, n):
        if n in cache:
            return cache[n]
        if n < 3:
            return n
        else:
            cache[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
            return cache[n]



def main():
    s = Solution()
    print("staring....")
    print(s.climbStairs(44))
    

if __name__ == "__main__":
    main()
