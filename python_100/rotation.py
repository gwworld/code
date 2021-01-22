#!/usr/bin/python3 
class Rotation(object):
    def is_substring(self, s1, s2):
        if len(s1) == 0 or len(s2) == 0:
            return False
        i = 0
        j = 0
        while (j < len(s2)) and (i < len(s1)):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j = 0
                if s1[i] != s2[0]:
                    i += 1
        if j == len(s2) - 1:
            return True
        return False
    
    def is_rotation(self, s1, s2):
        if s1 is None or s2 is None:
            return False
        for i in range(len(s1)):
            a, b = s1[:i], s1[i:]
            new_s1 = b + a
            if self.is_substring(new_s1, s2):
                return True
        return False

if __name__ == "__main__":
    a = Rotation()
    is_substring = a.is_rotation
    print(is_substring("ABCDEF", "EFABCD"))
    print(is_substring("ABCDEF", ""))
    print(is_substring("ABCDEF", None))

