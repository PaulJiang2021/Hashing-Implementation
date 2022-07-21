from sklearn.utils import murmurhash3_32
import random
from collections import defaultdict

HashRange = 2**20
mSeed = 1000
random.seed(100)

def create_trigram(x:str) -> list:
    return [x[idx:idx+3] for idx in range(len(x) - 2)]

def minHash(x, m) -> list:
    seed = [i ** 2 for i in range(m)]
    trigramList = create_trigram(x)
    return [min([murmurhash3_32(trigram, j) % HashRange for trigram in trigramList]) for j in seed]

def combineHash(hashcodes: list) -> int:
    inpString = str(hashcodes)
    return hash(inpString)

def estimateJaccard(x: list, y: list):
    val = sum([x[i] == y[i] for i in range(len(x))])
    return val / len(x)

def actualJaccard(x:str, y: str) -> float:
    xTrigram = set(create_trigram(x))
    yTrigram = set(create_trigram(y))
    return len(xTrigram.intersection(yTrigram)) / len(xTrigram.union(yTrigram))
        
class HashTable():
    def __init__(self, K, L, B, R):
        self.numHashFunc = K
        self.numHashTable = L
        self.size = B
        self.r = R
        self.table = [defaultdict(list) for l in range(self.numHashTable)]

    def insert(self, hashcodes: list, id) -> None:
        """
        hashcodes: list[K * L]
        """
        for i in range(self.numHashTable):
            location = combineHash(hashcodes[i * self.numHashFunc : (i + 1) * self.numHashFunc]) % self.r
            self.table[i][location].append(id)

    def lookup(self, hashcodes: list) -> set:
        result = set()
        for i in range(self.numHashTable):
            location = combineHash(hashcodes[i * self.numHashFunc : (i + 1) * self.numHashFunc]) % self.r
            result.update(self.table[i][location])
        return result

