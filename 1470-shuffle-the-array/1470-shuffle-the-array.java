class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] ans = new int[2*n];
        for(int i = 0, j=n; i<n && j<2*n; i++,j++){
            ans[2*i]=nums[i];
            ans[2*i+1]=nums[j];
        }
        return ans;
        
    }
}