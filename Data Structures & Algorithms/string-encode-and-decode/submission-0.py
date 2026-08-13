class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded+=str(len(string))+'#'+string
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        counter = ''
        while i < len(s):
            #need to store numbers until #
            #  2#ab1#c3#def
            if s[i].isdigit():
                counter += s[i]
                i+=1
            if s[i] == '#':
                # get the count before and reset counter to '' again
                j = int(counter)
                counter = ''
                # slice next and add to output list
                decoded.append(s[i+1:i+j+1])
                # move the pointer
                i = i + j + 1
        return decoded
