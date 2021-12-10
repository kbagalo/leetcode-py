class Solution:
    
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        if len(strs)==1:
            return strs[0]
        # print("Started")
        first_sub_string = self.find_common_prefix(strs[0],strs[1])
        # print(first_sub_string)

        for next_string in strs[2:]:
            first_sub_string = self.find_common_prefix(first_sub_string, next_string)

        return first_sub_string

    
    def find_common_prefix(self,str1, str2):
        substr = ""
        for char in str1:
            if char in str2:
                substr+= char
            else:
                break

        return substr


def main():
    sol = Solution()
    # print(sol.longestCommonPrefix(["flower","flow","flight"]))
    # print(sol.longestCommonPrefix( ["dog","racecar","car"]))
    print(sol.longestCommonPrefix(["ab", "a"]))

if __name__ == "__main__":
    main()