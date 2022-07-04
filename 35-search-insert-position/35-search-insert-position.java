class Solution {
    public int searchInsert(int[] nums, int target) {
        int index = Arrays.binarySearch(nums,target);
        return index<0 ? -(index+1) : index;
        
    }
}