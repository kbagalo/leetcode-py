class Solution:
    def isValid(self, s:str) -> bool:
        par_dict = {'(': ')', '{': '}', '[' : ']'}
        par_stack = []
        for par in s:
            print(par)
            if par in par_dict:
                par_stack.append(par)
            else:
                # print("Saw a closing par")
                last_par = par_stack.pop()
                # print("Previous par is:", last_par)
                if par_dict[last_par] != par:
                    return False
        return len(par_stack)==0

s = "()"
s2 = "{[]}"
sol = Solution()
print(sol.isValid(s))