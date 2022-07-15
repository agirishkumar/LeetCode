class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        boolean result = false;
        
        String a = "";
        String b = "";
        for(String i : word1){
            a = a+i;
        }
        for(String j : word2){
            b = b+j;
        }
        if(a.equals(b)){
            result = true;
        }
        
        return result;
        
        
    }
}