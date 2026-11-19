class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = getNextSum(n);
        
        while (fast != 1 && slow != fast) {
            slow = getNextSum(slow);
            fast = getNextSum(getNextSum(fast));
        }
        
        return fast == 1;
    }
    
    private int getNextSum(int n) {
        int sum = 0;
        while (n > 0) {
            int rem = n % 10;
            sum += rem * rem;
            n /= 10;
        }
        return sum;
    }
}
