class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        result = 0
        prev_value = 0
        for letter in s:
            value = roman_to_int[letter]
            result += value
            if value > prev_value:
                # preceding roman nummber is smaller
                # we need to undo the previous addition
                # and substract the preceding roman char
                # from the current one, i.e. we need to
                # substract twice the previous roman char
                result -= 2 * prev_value
            prev_value = value
        return result

def main():
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))
    

if __name__ == "__main__":
    main()
