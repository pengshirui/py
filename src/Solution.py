from typing import DefaultDict

class Solution:
    def stringToDict(str):
        kv = DefaultDict();
        for i in range(len(str)):
            kv[i] = str[i]
        return kv