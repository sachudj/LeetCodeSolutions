class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                new_s.append(str((int(s[i]) + int(s[i+1])) % 10))
            s = ''.join(new_s)
        return s[0] == s[1]

# Two other solutions I found while checking the solutions
# Code #1
# Time complexity: O(n^2). Space complexity: O(n).
#
# class Solution:
#     def hasSameDigits(self, s: str) -> bool:
#         return eq(*reduce(lambda q,_:[sum(p)%10 for p in pairwise(q)],s[2:],map(int,s)))
#
#
# Code #2
# Time complexity: O(n^2). Space complexity: O(n).
#
# class Solution:
#     def hasSameDigits(self, s: str) -> bool:
#         return (f:=lambda q:f([sum(p)%10 for p in pairwise(q)]) if len(q)>2 else eq(*q))([*map(int,s)])
