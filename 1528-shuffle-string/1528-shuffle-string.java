class Solution {
    public String restoreString(String s, int[] indices) {
        char[] temp = s.toCharArray();
        for(int i=0;i<s.length();i++){
            int j = indices[i];
            temp[j] = s.charAt(i);
        }
        StringBuilder stringBuilder = new StringBuilder();
        for (int i = 0; i < temp.length; i++) {
            stringBuilder.append(temp[i]);
        }
        String joinedString = stringBuilder.toString();

        return joinedString;
        
    }
}