class solution:
    def combinationsum2(self, candidates, target):
        candidates.sort()
        # sort the list first
        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                # base case for the recursion,cur is a list that contains our current combination of candidates

            if target <= 0:
                return
            prev = -1
            # use to void duplicates
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                # updating our prev variable
                prev = candidates[i]

        backtrack([], 0, target)
        return res


ll = solution()
print(ll.combinationsum2([10, 1, 2, 7, 6, 1, 5], 8))
