class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int result =0;
        for(String i : operations){
            if(i.contains("++")){
                result++;
            }
            if(i.contains("--")){
                result--;
            }
        }
        return result;
    }
}