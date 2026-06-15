"Binary tree level checking"
class Solution {
    
    int leafLevel = -1;
    
    boolean check(Node root) {
        return dfs(root, 0);
    }
    
    boolean dfs(Node node, int level) {
        if (node == null)
            return true;
        
        // Leaf node
        if (node.left == null && node.right == null) {
            if (leafLevel == -1)
                leafLevel = level; // first leaf
            
            return leafLevel == level;
        }
        
        return dfs(node.left, level + 1) &&
               dfs(node.right, level + 1);
    }
}
