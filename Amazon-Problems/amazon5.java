class Solution {

    int maximumSumRectangle(int R, int C, int M[][]) {

        int maxSum = Integer.MIN_VALUE;

        for (int top = 0; top < R; top++) {

            int[] temp = new int[C];

            for (int bottom = top; bottom < R; bottom++) {

                for (int col = 0; col < C; col++) {
                    temp[col] += M[bottom][col];
                }

                int currentSum = kadane(temp);

                maxSum = Math.max(maxSum, currentSum);
            }
        }

        return maxSum;
    }

    int kadane(int[] arr) {

        int maxEndingHere = arr[0];
        int maxSoFar = arr[0];

        for (int i = 1; i < arr.length; i++) {
            maxEndingHere = Math.max(arr[i], maxEndingHere + arr[i]);
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }
}
