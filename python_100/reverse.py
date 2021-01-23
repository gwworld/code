class ReverseString(object):
    def reverse(self, chars):
        if chars is None:
            return None
        if len(chars) == 0:
            return chars
        length = len(chars)-1
        mid = length // 2 + 1
        for i in range(mid):
            chars[i], chars[length-i] = chars[length-i], chars[i]
        return chars


if __name__ == "__main__":
    obj = ReverseString()
    print(obj.reverse(["a", "b", "c", "d", "e"]))