class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # len(s) != len(t)
        # t can have duplicates like s = b, t = bb or s = bbb, t = bbbb
        #result = 0

    #With XOR
        
        # for i in range(lnt):
        #     result ^= ord(t[i])
        #     if i < lns:
        #         result ^= ord(s[i])

        # for i in range(ln):
        #     result ^= ord(t[i])
        #     result ^= ord(s[i])
        # result ^= ord(t[ln])

        # result = [result ^=ord(char) for char in t+s][0]

        # return chr(result)

        #With Hashmap

        count = {}

        for char in t:
            if char in count:
                 count[char] +=1
            else:
                count[char] = 1
        for char in s:
            count[char] -=1
            if count[char] == 0:
                del count[char] # We are deleting every character that both t and s have

        # after all the remaining character is the different one

        return list(count.keys())[0] ## There maybe better solution than this , but learned a lot from this piece of code
        
      