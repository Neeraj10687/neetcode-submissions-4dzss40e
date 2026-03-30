class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res =new ArrayList<>();

        int n = nums.length;

        for(int i=0;i<n;i++){
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }

            int l=i+1;
            int r=n-1;

            while(l<r){
                int tsum=nums[l]+nums[r]+nums[i];
                if(tsum>0){
                    r--;
                }else if(tsum<0){
                    l++;
                }else{
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    l++;
                    r--;
                    while (nums[l] ==nums[l-1] && l<r){
                        l++;
                    }
                }
            }
        }
        
            return res;
    }
}
