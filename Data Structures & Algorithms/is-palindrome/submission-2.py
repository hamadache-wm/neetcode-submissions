class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(c for c in s if c.isalnum()).lower()
        len_res = len(res)

        word_length = int(len_res/2)

        first_word = res[0:word_length]
        second_word = res[len_res-word_length:len_res]
        second_word = second_word[::-1]

        return first_word == second_word
        