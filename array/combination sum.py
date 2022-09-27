#checking for all the combinations that sun up to target and avoiding duplicates of the combinations
class solution:
    def combination(self, candidates, target):
        res = []

        # creating a base case for the recursive function
        def dfs(i, cur, total):
            # i equals index,cur is the current index value we are using
            if total == target:
                # here we found the result we then append
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            # calling the dfs function
            dfs(i, cur, total + candidates[i])
            # now we pop our cur when we are done with it
            cur.pop()
            dfs(i + 1, cur, total)
            # this creates a 2 level decision tree

        dfs(0, [], 0)
        return res


ll = solution()
print(ll.combination([2, 3, 6, 7], 7))
