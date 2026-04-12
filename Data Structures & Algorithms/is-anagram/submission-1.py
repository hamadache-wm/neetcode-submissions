class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)
        list_s = sorted(s)
        list_t = sorted(t)

        if len(set_s) != len(set_t) or len(list_s) != len(list_t) or set_s != set_t: return False

        for e in set_s:
            if list_s.count(e) != list_t.count(e):
                return False

        return True