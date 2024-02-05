//https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,int> D;
        for(char i:s)
        {
            if(D.find(i)!=D.end())D[i]++;
            else D[i]=1;
        }
        for(int i=0;i<s.size();i++)
        {
            if(D[s[i]]==1)return i;
        }
        return -1;
    }
};
