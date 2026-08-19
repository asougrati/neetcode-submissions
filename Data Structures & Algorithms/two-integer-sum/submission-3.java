class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> prev = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            if (prev.containsKey(diff)) {
                result[0] = prev.get(diff);
                result[1] = i;
            }
            prev.put(num, i);
        }
        return result;
    }
}
