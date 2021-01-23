class Solution(object):

    def find_diff(self, str1, str2):
        if str1 is None or str2 is None:
            raise("TypeError")
        long_str = str1 if len(str1) > len(str2) else str2
        short_str = str2 if len(str1) > len(str2) else str1
        for i in range(len(short_str)):
            if long_str[i] != short_str[i]:
                return long_str[i]
        return long_str[i+1]

if __name__ == "__main__":
    obj = Solution()
    print(obj.find_diff("abcd", "acd"))
    print(obj.find_diff("abcd", "abcde"))