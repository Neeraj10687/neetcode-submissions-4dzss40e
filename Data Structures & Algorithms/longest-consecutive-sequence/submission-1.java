class Solution {
    public int longestConsecutive(int[] nums) {

        Set<Integer> hset =new HashSet<>();
        for(Integer n: nums){
            hset.add(n);
        }

        int length =0;
        int longes =0;

        for(Integer num:hset){
            if(!hset.contains(num-1)){
                length=0;
                while(hset.contains(num+length)){
                    length+=1;
                }
                longes=Math.max(length,longes);
            }
        }
        return longes;

        
    }
}
