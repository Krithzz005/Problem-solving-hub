class Solution {
    public int countDigits(int num) {
        int temp=num;
        int rem,count=0;
        while(temp>0){
            rem=temp%10;
            if(num%rem ==0){
                count+=1;
            }
            temp/=10;
        }
        return count;
    }
}
