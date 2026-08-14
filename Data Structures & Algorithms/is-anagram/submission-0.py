class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_letters = dict()
        t_letters = dict()
        s_duplicates = set()
        t_duplicates = set()

        for i in range(len(s)):
            if s[i] in s_duplicates:
                s_letters[s[i]] += 1
                continue
            s_duplicates.add(s[i])
            s_letters[s[i]] = 1

        for j in range(len(t)):
            if t[j] in t_duplicates:
                t_letters[t[j]] += 1
                continue
            t_duplicates.add(t[j])
            t_letters[t[j]] = 1

        return s_letters == t_letters
        