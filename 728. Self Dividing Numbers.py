class Solution:
    def __init__(self):
        pass

    def Check(self, n):
        strN=str(n)
        for d in strN:
            if d == '0':
                return False
            elif n % int(d) != 0:
                return False
        return True

    def selfDividingNumbers(self, left, right) :
        result=[]
        for n in range(left, right+1):
            if self.Check(n):
                result.append(n)
        return result



sln=Solution()
assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]==sln.selfDividingNumbers(1,22)