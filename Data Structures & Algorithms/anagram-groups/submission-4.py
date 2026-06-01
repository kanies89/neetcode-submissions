class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = dict.fromkeys(strs)
        result = []
        checked = []
        sorted_val = []


        for key in dict_strs:
            dict_strs[key] = [len(key), sorted(key)]
        
        for n_1, i in enumerate(strs):
            part_result = [i]
            if (dict_strs[i][0] in checked) & (dict_strs[i][1] in sorted_val):
                    continue
            checked.append(dict_strs[i][0])    
            sorted_val.append(dict_strs[i][1]) 
            for n_2, j in enumerate(strs):
                if n_1 == n_2:
                    continue
                if dict_strs[i][0] != dict_strs[j][0]:
                    continue
                if dict_strs[i][1] == dict_strs[j][1]:
                    part_result.append(j)
            result.append(part_result)
        
        return result

