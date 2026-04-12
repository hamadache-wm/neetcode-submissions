class Solution:
    def isValid(self, s: str) -> bool:
        set_open = {'(', '{', '['}
        dict_string = {'(': ')','{': '}','[': ']'}
        next_close = []

        for e in s:
            if e in set_open:
                next_close.append(dict_string[e])
            elif not next_close or e != next_close.pop():
                return False

        return not next_close