#https://leetcode.com/problems/sequential-digits/
class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int>v;
#You can generate this vector using recursion, or using loops
        vector<int> m = {
12,23,34,45,56,67,78,89,            
123,234,
345,
456,
567,
678,
789,
1234,
2345,
3456,
4567,
5678,
6789,
12345,
23456,
34567,
45678,
56789,
123456,
234567,
345678,
456789,
1234567,
2345678,
3456789,
12345678,
23456789,
123456789};
        for(int i:m){
            if(low<=i && i<=high){
            string s = to_string(i);
            int temp = s[0]-'0';
            int j = 1;
            bool T = true;
            while (j<s.size()){
                if (s[j]-'0'!=temp+1){
                    T = false;
                    break;
                }
                temp = s[j]-'0';
                j++;
            }
            if(T)
            {
                v.push_back(stoi(s));
            }
            }
        }
        return v;
    }
};onl
