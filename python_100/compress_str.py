#! /usr/bin/python3

class CompressString(object):
    def compress(self, string):
        if string is None:
            return None
        if len(string) == 0:
            return ""
        if len(set(string))*2 >= len(string):
            return string
        new_str = ""
        count = 0
        pre_char = string[0]
        for i in string:
            if i == pre_char:
                count += 1
            else:
                new_str += "%s%s" % (pre_char, count)
                count = 1
                pre_char = i
        new_str += "%s%s" % (pre_char, count)
        return new_str

if __name__ == "__main__":
    a = CompressString()
    print(a.compress("aaacccddd"))
    print(a.compress("aaacccdddc"))
    print(a.compress(""))
    print(a.compress("acddccmmnn"))
    print(a.compress(None))


        