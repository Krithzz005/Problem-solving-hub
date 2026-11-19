class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=1
        if(num<=1):
            return False
        for i in range(2,int(num**0.5)+1):
            if(num % i == 0):
                sum+=i
                if i * i != num:
                    sum += num // i
        if(sum == num):
            return True
        else:
            return False
