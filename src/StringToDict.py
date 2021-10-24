from collections import defaultdict

def stringToDict(str):
        kv = defaultdict();
        for i in range(len(str)):
            kv[i] = str[i]
        return kv
