class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freqMap = new HashMap<>();

        for (int num : nums){
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new List[nums.length + 1];
        for (int key : freqMap.keySet()) {
            int freq = freqMap.get(key);
            if (buckets[freq] == null) {
                buckets[freq] = new ArrayList<>();
            }
            buckets[freq].add(key);
        }

        int[] res = new int[k];
        int index = 0;
        for(int i=nums.length; i>0; i--){
            if (buckets[i] == null) continue;
            for (int val : buckets[i]){
                res[index] = val;
                index++;
                if (index == k){
                    return res;
                }
            }
        }
        return new int[] {};

    }
}
