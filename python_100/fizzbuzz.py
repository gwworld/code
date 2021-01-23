class Solution(object):
    def fizz_buzz(self, num):
        if num < 1:
            raise ValueError("num should be > 1")
        if num is None:
            raise TypeError("num cannot be None")
        result = []
        for i in range(1, num+1):
            if (i % 3 == 0) and (i % 5 == 0):
                result.append("fizz_buzz")
            elif i % 3 == 0:
                result.append("fizz")
            elif i % 5 == 0:
                result.append("buzz")
            else:
                result.append(str(i))
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.fizz_buzz(20))