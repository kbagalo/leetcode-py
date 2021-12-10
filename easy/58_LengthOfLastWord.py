class Solution:

    def lengthOfLastWord(self, s: str) -> None:
        if s:
            for word in reversed(s.split(" ")):
                if "" != word:
                    return len(word)


def main():
    # s = "   fly me   to   the moon  "
    s = "luffy is still joyboy"
    sol = Solution()
    print(sol.lengthOfLastWord(s))


if __name__ == "__main__":
    main()
