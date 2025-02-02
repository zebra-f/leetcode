class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_bin = bin(num2)[2:]
        num2_set_bits = num2_bin.count("1")

        num1_bin_list = list(bin(num1)[2:])

        num3 = ["0"] * len(num1_bin_list)

        i = 0
        while num2_set_bits > 0 and i < len(num1_bin_list):
            if num1_bin_list[i] == "1":
                num3[i] = "1"
                num2_set_bits -= 1
            i += 1

        i = len(num1_bin_list) - 1
        while num2_set_bits > 0 and i >= 0:
            if num1_bin_list[i] == "0":
                num3[i] = "1"
                num2_set_bits -= 1
            i -= 1

        num3 = ["1"] * num2_set_bits + num3

        return int("".join(num3), 2)


solution = Solution()
a = solution.minimizeXor(num1=3, num2=5)
print(a)
b = solution.minimizeXor(num1=1, num2=12)
print(b)
