class Solution {
public:
    int maxArea(vector<int>& height) {
        int maximo = 0;
        int i = 0;
        int j = height.size()-1;
        int water;
        
        while(i<=j) {
            water = min(height[i], height[j]) * (j - i);
            if (water > maximo) {
                maximo = water;
            }

            if (height[i] < height[j]) {
                i++;
            } else {
                j--;
            }

        }
        return maximo;
    }
};