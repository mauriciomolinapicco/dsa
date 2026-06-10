class Solution {
public:
    int uniquePaths(int rows, int cols) {
        int dp[rows][cols];
        for (int i=0; i<cols; i++) {
            dp[0][i] = 1;
        }
        for (int i=0; i<rows; i++) {
            dp[i][0] = 1;
        }

        for (int row=1; row<rows; row++) {
            for (int col=1; col<cols; col++) {
                dp[row][col] = dp[row-1][col] + dp[row][col-1];
            }
        }

        return dp[rows-1][cols-1];
    }
};