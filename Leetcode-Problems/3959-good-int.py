class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum,squareSum=0,0
        while(n > 0):
            digit=n%10
            digitSum+=digit
            squareSum+=digit**2
            n//=10
        if (squareSum - digitSum) >= 50:
            return True
        else:
            return False
