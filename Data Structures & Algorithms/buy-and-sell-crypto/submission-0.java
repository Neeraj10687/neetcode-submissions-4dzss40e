class Solution {
    public int maxProfit(int[] prices) {

        int l =0;
        int r =1;
        int mp =0;

        while(r<prices.length){
            if(prices[l]<prices[r]){
               int  profit = prices[r]- prices[l];
               mp = Math.max(profit,mp);
            }else{
                l = r;
            }
            r++;
        }
        return mp;
        
    }
}
