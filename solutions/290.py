class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ss = s.split(' ')
        if len(ss)!=len(pattern):
            return False
        dic = dict()
        tokens = set()
        for index, word in enumerate(ss):
            if word in dic:
                token = dic[word]
                if token != pattern[index]:
                    return False
            else:
                token = pattern[index]
                if token in tokens:
                    return False
                dic[word] = token
                tokens.add(token)
        return True