class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        print("\n------------------")
        answer = 0
        vowels = {vowel: 0 for vowel in ["a", "e", "i", "o", "u"]}

        def every_vowel_is_present(vowels):
            for val in vowels.values():
                if val == 0:
                    return False
            return True

        consonants = 0
        l = 0
        r = 0
        while r < len(word):
            char = word[r]
            if char in vowels:
                vowels[char] += 1
            else:
                consonants += 1

            if consonants == k:
                every_vowel = every_vowel_is_present(vowels)
                if every_vowel:
                    answer += 1
            if consonants == k + 1:
                while consonants != k:
                    char = word[l]
                    if char in vowels:
                        vowels[char] -= 1
                    else:
                        consonants -= 1
                    if every_vowel_is_present(vowels):
                        answer += 1
                    l += 1

            r += 1

        print(answer, l)
        while l < r:
            char = word[l]
            if char in vowels:
                vowels[char] -= 1
            else:
                consonants -= 1

            print(consonants, vowels)
            if consonants == k and every_vowel_is_present(vowels):
                answer += 1

            l += 1

        return answer


solution = Solution()
a = solution.countOfSubstrings(word="aeioqq", k=1)
print(a)
b = solution.countOfSubstrings(word="aeiou", k=0)
print(b)
c = solution.countOfSubstrings(word="ieaouqqieaouqq", k=1)
print(c)
d = solution.countOfSubstrings("ieaouqqieaouqq", k=1)
print(d)
e = solution.countOfSubstrings("ieaouqaeoi", k=1)
print(e)
f = solution.countOfSubstrings("aoaiuefi", k=1)
print(f)
