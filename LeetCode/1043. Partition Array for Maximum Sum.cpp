class Solution {
public:
    int maxSumAfterPartitioning(std::vector<int>& arr, int k) {
        vector<int> memo(arr.size(), -1);
        return dfs(arr, k, 0, memo);
    }
    int dfs(vector<int>& arr, int k, int i, vector<int>& memo) {
        if (i >= arr.size())return 0;
        if (memo[i] != -1) return memo[i];
        int res = 0;
        int cur_max = 0;
        for (int j = i; j < i + k && j < arr.size(); j++) {
            cur_max = max(cur_max, arr[j]);
            int temp = dfs(arr, k, j + 1, memo) + cur_max * (j - i + 1);
            res = max(res, temp);
        }
        memo[i] = res;
        return res;
    }
};
