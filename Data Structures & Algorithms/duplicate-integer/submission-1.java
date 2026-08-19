class Solution {
    public boolean hasDuplicate(int[] nums) {
        int pointer = 0;
        while(pointer < nums.length) {
            int duplicate = 0;
            for (int i = 0; i < nums.length; i++) {
                if (nums[pointer] == nums[i]) {
                    duplicate++;
                }
            }
            if (duplicate > 1) {
                return true;
            }
            pointer++;
        }       
        return false;
    }
}