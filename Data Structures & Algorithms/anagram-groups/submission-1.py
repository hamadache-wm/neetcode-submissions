class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()
        res = []

        for e in strs:
            len_e = len(list(e))
            set_e = set(e)
            group = anagram_groups.get(len_e)

            if group == None:
                res.append([e])
                index = len(res)-1
                anagram_groups[len_e] = [{"set": set_e, "value": e, "index": index}]
            else:
                set_found_flag = False
                for group_el in group:
                    if group_el["set"] == set_e:
                        set_found_flag = True
                        if self.areAnagrams(group_el["value"], e, group_el["set"]):
                            res[group_el["index"]].append(e)
                        else:
                            res.append([e])
                            index = len(res)-1
                            anagram_groups[len_e] = [{"set": set_e, "value": e, "index": index}]

                if set_found_flag == False:
                        res.append([e])
                        index = len(res)-1
                        group.append({"set": set_e, "value": e, "index": index})
            
        return res


    
    def areAnagrams(self, s1: str, s2: str, str_set: set):
        for e in str_set:
            if s1.count(e) != s2.count(e):
                return False
        
        return True
