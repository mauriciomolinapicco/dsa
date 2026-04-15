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
    bool valid_tree(TreeNode* root, long minimo, long maximo) {
        if (root == NULL) return true;

        int v = root->val;

        if (v <= minimo || v >= maximo) return false;

        return valid_tree(root->left, minimo, v) && valid_tree(root->right, v, maximo);

    }

    bool isValidBST(TreeNode* root) {
        return valid_tree(root, LONG_MIN, LONG_MAX);
    }
};