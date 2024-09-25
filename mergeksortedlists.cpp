// https://leetcode.com/problems/merge-k-sorted-lists
class Solution {
 public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    if (lists.empty()) return nullptr;
    ListNode* dummyNode = new ListNode(-1);
    ListNode* temp = dummyNode;
    priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>,
                   greater<pair<int, ListNode*>>>
        pq;

    for (auto head : lists)
      if (head != nullptr) pq.push({head->val, head});

    while (!pq.empty()) {
      ListNode* minNode = pq.top().second;
      pq.pop();

      if (minNode->next != nullptr)
        pq.push({minNode->next->val, minNode->next});

      temp->next = minNode;
      temp = temp->next;
    }

    return dummyNode->next;
  }
};
