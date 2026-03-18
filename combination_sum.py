class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, remaining):
            # Base case
            if remaining == 0:
                result.append(path[:])
                return
            
            if remaining < 0:
                return

            # Try all choices
            for i in range(start, len(candidates)):
                # Choose
                path.append(candidates[i])

                # Explore (same index allowed)
                backtrack(i, path, remaining - candidates[i])

                # Undo (backtrack)
                path.pop()

        backtrack(0, [], target)
        return result
obj = Solution()
result= obj.combinationSum(([2,3,5,4]), 7)  
print(result)  