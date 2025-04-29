class Solution:
    def reverseWords(self, s: str) -> str:
        j=0
        st=[]
        for i in range(len(s)):
            if s[i]==" ":
               sub=s[j:i]
               if sub!="":
                  st.append(sub)
               j=i+1
        sub=s[j:len(s)]
        if sub!="":
            st.append(sub)       
        return ' '.join(st[::-1])

        