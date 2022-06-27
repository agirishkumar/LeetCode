class Solution {
    public String restoreString(String s, int[] indices) {
        char word[] = new char[indices.length];
        int n = 0;
        for(int i : indices){
            word[i] = s.charAt(n);
            n++;
        }
        String ans = new String(word);

        return ans;
        
    }
}