class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> mySet(nums.begin(), nums.end());
        return nums.size() != mySet.size();
    }
};