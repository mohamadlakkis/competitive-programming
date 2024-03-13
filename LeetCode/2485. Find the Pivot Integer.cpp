//https://leetcode.com/problems/find-the-pivot-integer
class Solution {
public:
    int pivotInteger(int n) {
        int sum = n*(n+1)/2;
        int l =1;
        int r = n;
        int mid;
        while(l<=r)
        {
            mid = (l+r)/2;
            int cur = mid*(mid+1)/2;
            int temp = sum-cur+mid;
            if(cur==temp)return mid;
            else if(cur<temp) l = mid+1;
            else r = mid-1;
        }
        return -1;

    }
    
};
