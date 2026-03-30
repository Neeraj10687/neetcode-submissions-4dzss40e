class Solution {
    public boolean isAnagram(String s, String t) {

        if(s.length()!=t.length()){
            return false;
        }

        HashMap<Character,Integer> Cs=new HashMap<>(); 
        HashMap<Character,Integer> Ts=new HashMap<>(); 

        for(int i=0;i<s.length();i++){
            Cs.put(s.charAt(i),Cs.getOrDefault(s.charAt(i),0)+1);
            Ts.put(t.charAt(i),Ts.getOrDefault(t.charAt(i),0)+1);

        }

        return Cs.equals(Ts);

    }
}
