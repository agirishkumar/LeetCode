class Solution {
    public int[] sortedSquares(int[] nums) {
        
        int[] returnArr = new int[nums.length];
        int i = 0; 
        int j = nums.length - 1;
        int index = nums.length - 1;
        while (i <= j) {
            if (Math.abs(nums[i]) > Math.abs(nums[j])) {
                returnArr[index] = nums[i] * nums[i];
                i++;
            } else {
                returnArr[index] = nums[j] * nums[j];
                j--;
            }
            index--;
        }
        return returnArr;
        
    }
}