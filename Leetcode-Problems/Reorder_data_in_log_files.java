import java.util.*;

class Solution {
    public String[] reorderLogFiles(String[] logs) {

        Arrays.sort(logs, (a, b) -> {

            String[] log1 = a.split(" ", 2);
            String[] log2 = b.split(" ", 2);

            boolean isDigit1 = Character.isDigit(log1[1].charAt(0));
            boolean isDigit2 = Character.isDigit(log2[1].charAt(0));

            if (!isDigit1 && !isDigit2) {
                int cmp = log1[1].compareTo(log2[1]);

                if (cmp != 0)
                    return cmp;

                return log1[0].compareTo(log2[0]);
            }

    
            if (!isDigit1 && isDigit2)
                return -1;

            if (isDigit1 && !isDigit2)
                return 1;

          
            return 0;
        });

        return logs;
    }
}
