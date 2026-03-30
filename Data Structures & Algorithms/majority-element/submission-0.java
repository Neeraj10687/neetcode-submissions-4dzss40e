class Solution {
    public int majorityElement(int[] num) {

    HashMap<Integer,Integer> map=new HashMap<>();

    for(int i=0;i<num.length;i++){
      int key =num[i];

      map.put(key,map.getOrDefault(key,0)+1);

          }

    int freq=0;
    for(Integer Key:map.keySet()){
      if(map.get(Key)>num.length/2){
        freq = Key;
      }
    }
return freq;
 
    }
}
