class Solution {
    public int[] twoSum(int[] nums, int target) {

        int[][] a=new int[nums.length][2];

        for(int i=0;i<nums.length;i++){
            a[i][0]=nums[i];
            a[i][1]=i;
        }

        Arrays.sort(a,Comparator.comparingInt(A->A[0]));

        //2 pointer approach
        int i=0;
        int j=nums.length-1;

        while(i<j){
            int curr=a[i][0]+a[j][0];
            if(curr==target){
                return new int[]{Math.min(a[i][1],a[j][1]),Math.max(a[i][1],a[j][1])};
            }else if(curr<target){
                i++;
            }else{
                j--;
            }
        }
        return null;
    }
}
