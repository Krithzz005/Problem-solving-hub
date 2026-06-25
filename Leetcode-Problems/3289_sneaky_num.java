import java.util.HashSet;

class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        int[] res = new int[2];
        int index = 0;
        HashSet<Integer> seen = new HashSet<>();
        for (int num : nums) {
            if (seen.contains(num)) {
                res[index] = num;
                index++;
                if (index == 2) {
                    break;
                }
            } else {
                seen.add(num);
            }
        }
        
        return res;
    }
}
