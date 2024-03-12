//https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode node=ListNode(0, head);
        unordered_map<int, ListNode*> mp;
        int prefix=0;
        for(ListNode* ptr=&node; ptr; ptr=ptr->next){
            prefix+=(ptr->val);
            mp[prefix]=ptr;
        }
        prefix=0;
        for(ListNode* ptr=&node; ptr; ptr=ptr->next){
            prefix+=(ptr->val);
            ptr->next=mp[prefix]->next; // removing elemennts between this current ptr and mp[prefix]
        }
        return node.next;
    }
};
