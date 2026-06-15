class Solution {

    int tour(int petrol[], int distance[]) {

        int start = 0;
        int balance = 0;
        int deficit = 0;

        for (int i = 0; i < petrol.length; i++) {

            balance += petrol[i] - distance[i];

            if (balance < 0) {
                deficit += balance;
                start = i + 1;
                balance = 0;
            }
        }

        if (balance + deficit >= 0)
            return start;

        return -1;
    }
}
