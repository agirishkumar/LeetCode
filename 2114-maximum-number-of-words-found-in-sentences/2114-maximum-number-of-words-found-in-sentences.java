class Solution {
    public int mostWordsFound(String[] sentences) {
        
        int max = 1;
        for(String j : sentences){
            int count = 1;
            for (int i = 0; i < j.length() - 1; i++)
            {
                if ((j.charAt(i) == ' ') && (j.charAt(i + 1) != ' '))
                {
                    count++;
                }
            }
            if(count > max){
                max = count;
            }
            
        }
        return max;
    }
}