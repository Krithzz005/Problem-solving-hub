class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int i,rem,sum=0;
        int og=x;
        if(x<=0){
            return -1;
        }
        while(og>0){
            rem=og%10;
            sum+=rem;
            og/=10;
        }
        if(x%sum==0){
            return sum;
        }
        else{
            return -1;
        }
    }
}
