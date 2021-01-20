#!/usr/bin/python3

class Permutations(object):
    def is_permutation(self, str1, str2):
        if str1 is None or str2 is None:
            return False
        if len(str1) == 0 or len(str2) == 0:
            return False
        return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    p_obj = Permutations()
    print(p_obj.is_permutation("", "a"))
    print(p_obj.is_permutation("a", ""))
    print(p_obj.is_permutation("a", "a"))
    print(p_obj.is_permutation("b", "a"))
    print(p_obj.is_permutation("ba", "ab"))
    print(p_obj.is_permutation("ba1", "1ab"))
    print(p_obj.is_permutation(None, "1ab"))
    print(p_obj.is_permutation("a", None))
