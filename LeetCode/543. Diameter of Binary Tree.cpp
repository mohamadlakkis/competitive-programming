//https://leetcode.com/problems/diameter-of-binary-tree
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int MAX = 0;
    int diameterOfBinaryTree(TreeNode* root) {
        X(root);
        return MAX;
    }
    int X(TreeNode* root)
    {
        if (!root)return -1;
        int L = X(root->left);
        int R = X(root->right);
        MAX = max(2+L+R,MAX);
        return 1+max(L,R);
    }
};
