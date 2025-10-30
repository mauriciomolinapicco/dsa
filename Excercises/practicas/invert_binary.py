class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)[2:].zfill(32)
        s = []
        inverted = b[::-1]
        # for i in range(len(b)-1, -1, -1):
        #     inverted += b[i]
        return int(inverted, 2)
