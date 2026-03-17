class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def solve(open_count, close_count, curr):
            # Base case
            if open_count == 0 and close_count == 0:
                result.append(curr)
                return

            # Add '('
            if open_count > 0:
                solve(open_count - 1, close_count, curr + "(")

            # Add ')'
            if close_count > open_count:
                solve(open_count, close_count - 1, curr + ")")

        solve(n, n, "")
        return result
    
obj = Solution()
ans =obj.generateParenthesis(3)
print(ans)