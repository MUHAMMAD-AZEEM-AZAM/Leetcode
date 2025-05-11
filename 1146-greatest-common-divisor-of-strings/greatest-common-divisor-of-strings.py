class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divides(st,subS):
            print("Called")
            if len(st)%len(subS)!=0:
                print("not divisible")
                return False
            n=0    
            for i in range(int(len(st)/len(subS))):
                if st[n:n+len(subS)]!=subS:
                    print("not equal",st[i:len(subS)])
                    return False
                print("True")    
                n=n+len(subS)    
            return True          

        check=0
        minimum=min(len(str1),len(str2))
        for i in range(minimum):
            if str1[i]!=str2[i]:
                break
            check+=1
        subString=str1[0:check]
        print(subString)


        for i in range(check):
            if divides(str1,subString) and divides(str2,subString):
                return subString 
            check-=1      
            subString=str1[0:check]
            print(subString)

        return ""          


