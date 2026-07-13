class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[1:].count("1")