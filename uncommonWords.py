#primeira tentativa
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        uncommon = []
        s1 = s1.split(" ")
        print s1
        s2 = s2.split(" ")
        print s2
        for i in s1:
            print(i)
            if i in s2:
                continue
            else:
                uncommon.append(i)
        print(uncommon)
        for j in s2:
            print(j)
            if j in s1:
                continue
            else:
                uncommon.append(j)        
        print(uncommon)
        return uncommon
#correto

        count = {}
     
        for i in s1.split():

            count[i] = count.get(i, 0) +1
#             .get -> Return the value for key if key is in the dictionary, else default. If default is not given, it defaults to None, so that this method never raises a KeyError.
        for i in s2.split():
            count[i] = count.get(i, 0)+1
        
        return [i for i in count if count[i]==1 ]
    