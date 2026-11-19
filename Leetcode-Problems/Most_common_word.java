import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> bannedSet = new HashSet<>(Arrays.asList(banned));
        String[] words = paragraph.toLowerCase().split("[^a-zA-Z]+");
        Map<String, Integer> counts = new HashMap<>();
        String mostCommon = "";
        int maxCount = 0;
        for (String w : words) {
            if (!bannedSet.contains(w)) {
                counts.put(w, counts.getOrDefault(w, 0) + 1);
                if (counts.get(w) > maxCount) {
                    maxCount = counts.get(w);
                    mostCommon = w;
                }
            }
        }
        return mostCommon;
    }
}
