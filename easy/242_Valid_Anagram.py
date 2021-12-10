class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        from collections import Counter
        counter_s = Counter(s)
        counter_t = Counter(t)
        # print(counter_t + counter_s)

        for each_key in (counter_s + counter_t):
            print(each_key)
            if counter_s.get(each_key) != counter_t.get(each_key):
                return False
        return True

def main():
    s = "a"
    t = "ab"
    sol = Solution()
    print(sol.isAnagram(s,t))

if __name__ == "__main__":
    main()