//https://leetcode.com/problems/group-anagrams/
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> D;
        for(string s:strs)
        {
            string k = s;
            sort(s.begin(),s.end());
            if (D.find(s)==D.end())
            {
                D[s] = {k};
            }
            else
            {
                D[s].push_back(k);
            }
        }
        vector<vector<string>> RES;
        for(auto i = D.begin(); i != D.end(); ++i)
        {
            vector<string> temp;
            for(string j:i->second)
            {
                temp.push_back(j);
            }
            RES.push_back(temp);
        }
        return RES;
    }
};
