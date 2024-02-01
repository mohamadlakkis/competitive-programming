//https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/
class Solution {
public:
    vector<vector<int>> divideArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int i = 0;
        int n = nums.size();
        while(i<n)
        {
            res.push_back({nums[i],nums[i+1],nums[i+2]});
            i+=3;
        }
        for(vector<int> v : res)
        {
            if ( !(v[2]-v[1]<=k && v[1]-v[0]<=k &&v[2]-v[0]<=k))
            {
                return {};
            }
        }
        return res;
        
    }
    
};
