#!/usr/bin/python3
#-*- coding:utf-8 -*-

class UniqueChars(object):

    def has_unique_chars(self, string):
        chars = {}
        if not isinstance(string, str):
            return False
        if string is None:
            return False
        for c in string:
            if c not in chars:
                chars[c] = 1
            else:
                chars[c] += 1
        for count in chars.values():
            if count > 1:
                return False
        return True

    def has_unique_chars_answer(self, string):
        chars = {}
        if not isinstance(string, str):
            return False
        if string is None:
            return False
        return len(set(string)) == len(string)

if __name__ == "__main__":
    u_obj = UniqueChars()
    has_unique_chars = u_obj.has_unique_chars
    has_unique_chars_answer = u_obj.has_unique_chars_answer
    print(has_unique_chars("1"))
    print(has_unique_chars("11"))
    print(has_unique_chars("abca"))
    print(has_unique_chars("abcd"))
    print(has_unique_chars(""))
    print(has_unique_chars(1))
    print(has_unique_chars_answer("1"))
    print(has_unique_chars_answer("11"))
    print(has_unique_chars_answer("abca"))
    print(has_unique_chars_answer("abcd"))
    print(has_unique_chars_answer(""))
    print(has_unique_chars_answer(1))
