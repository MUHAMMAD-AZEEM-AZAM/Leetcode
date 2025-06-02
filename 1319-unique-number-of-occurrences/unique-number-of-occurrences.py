class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        Hmap={}
        for i in arr:
            if i not in Hmap:
               Hmap[i]=1
            else:
                Hmap[i]+=1   
        print(Hmap)
        for i in Hmap:
            for j in Hmap:
                if Hmap[i]==Hmap[j] and i!=j:
                    return False
                   
        return True    
