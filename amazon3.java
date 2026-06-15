class Solution {
    int longestUniqueSubsttr(String s) {

        int[] last = new int[26];

        for (int i = 0; i < 26; i++) {
            last[i] = -1;
        }

        int start = 0;
        int maxLen = 0;

        for (int end = 0; end < s.length(); end++) {

            int idx = s.charAt(end) - 'a';

            if (last[idx] >= start) {
                start = last[idx] + 1;
            }

            last[idx] = end;

            maxLen = Math.max(maxLen, end - start + 1);
        }

        return maxLen;
    }
}
