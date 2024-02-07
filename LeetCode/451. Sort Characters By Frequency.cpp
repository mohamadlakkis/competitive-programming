//https://leetcode.com/problems/sort-characters-by-frequency/
//Bucket sort solution 
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char,int> D1;
        for(char c:s)
        {
            if(D1.find(c)==D1.end())D1[c]=1;
            else D1[c]++;
        }
        unordered_map<int,vector<char>> D2;
        for(const auto& pair : D1)
        {
            if(D2.find(pair.second)==D2.end())D2[pair.second]={pair.first};
            else D2[pair.second].push_back(pair.first);
        }
        string res = "";
        for(int i=s.size();i>=0;i--)
        {
            string temp = "";
            if(D2.find(i)!=D2.end())
            {
                for(char c:D2[i])
                {
                    for(int j=0;j<i;j++)
                    {
                        temp+=c;
                    }
                }
                res+=temp;
            }
        }
        return res;
    }
};

//Solution (TLE)
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> D;
         vector<char> chars;
        for (char c : s) {
            D[c]++;
            chars.push_back(c);
        }
        quickSort(chars, 0, chars.size() - 1, D);
        string result(chars.begin(), chars.end());
        return result;
    }

private:
    void quickSort(vector<char>& arr, int low, int high, const unordered_map<char, int>& D) {
        if (low < high) {
            int pi = partition(arr, low, high, D);
            quickSort(arr, low, pi - 1, D);
            quickSort(arr, pi + 1, high, D);
        }
    }
    int partition(vector<char>& arr, int low, int high, const unordered_map<char, int>& D) {
        char pivot = arr[high];
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (D.at(arr[j]) > D.at(pivot) || 
                (D.at(arr[j]) == D.at(pivot) && arr[j] < pivot)) {
                i++;
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[i + 1], arr[high]);
        return i + 1;
    }
};
