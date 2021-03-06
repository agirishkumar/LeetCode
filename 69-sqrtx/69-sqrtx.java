class Solution {
    public int mySqrt(int x) {
        
        if (x==1||x==0) return x;
    int left=1;
    int right=x;
	int mid;
    while (left<right){       
        mid=left+(right-left+1)/2;
        if (mid<=x/mid) left=mid;
        else  right=mid-1;
    }
    return left;
    }
}