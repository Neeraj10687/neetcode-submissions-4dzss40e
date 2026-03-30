class Solution {
    public int lengthOfLongestSubstring(String s) {
        int res=0;

        for(int l=0;l< s.length();l++){

        Set<Character> charset= new HashSet<>();
            for(int r =l;r<s.length();r++){
                if(charset.contains(s.charAt(r))){
                    break;
                }
                charset.add(s.charAt(r));
            }
            res=Math.max(res,charset.size());
        }
        return res;
        
    }
}
