class Solution {
    public int lengthOfLastWord(String s) {
        String[] a = s.split(" ");
        int ans  = a[a.length - 1].length();
        return ans;        
    }
}