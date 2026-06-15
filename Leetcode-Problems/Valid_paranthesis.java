import java.util.Stack;

public class Solution {

    public static boolean isValid(String s) {

        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {

            // Push opening brackets
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }

            // Check closing brackets
            else {
                if (stack.isEmpty()) {
                    return false; // no matching opening bracket
                }

                char top = stack.pop();

                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }

        // Stack should be empty for valid parentheses
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        String s = "{[()]}";
        System.out.println(isValid(s)); // true
    }
}
