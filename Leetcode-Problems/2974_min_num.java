class Solution {
    public int[] numberGame(int[] nums) {
        int i;
        Arrays.sort(nums);
        int[] arr=new int[nums.length];
        for(i=0;i<nums.length;i+=2){
            arr[i]=nums[i+1];
            arr[i+1]=nums[i];
        }
        return arr;
    }
}
