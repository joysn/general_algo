# https://junchengyang.com/publication/nsdi24-SIEVE.pdf
# Input: The request x, doubly-linked queue T, cache size C, hand p
# 1: if x is in T then           ▷ Cache Hit
# 2:   x.visited ← 1
# 3: else ▷ Cache Miss
# 4:   if |T| = C then           ▷ Cache Full
# 5:     o ← p
# 6:     if o is NULL then
# 7:       o ← tail of T
# 8:     while o.visited = 1 do
# 9:       o.visited ← 0
# 10:      o ← o.prev
# 11:     if o is NULL then
# 12:       o ← tail of T
# 13:       p ← o.prev
# 14:   Discard o in T           ▷ Eviction
# 15: Insert x in the head of T.
# 16: x.visited ← 0              ▷ Insertion


class sieve:
    cache = list()
    cache_size = 1000
    hand = -1

    def __init__(self,size):
        self.cache_size = size

    def current_size(self):
        return len(self.cache)
    
    def display(self):
        for e in self.cache:
            print(e,end=" ")
        print()
    
    def read(self,data):
        found = 0
        for e in self.cache:
            if e[0] == data:
                e[1] = 1
                found = 1
                print("found",e)
        if found == 0: # cache miss
            if len(self.cache) == self.cache_size: # cache full
                curr = self.hand
                if curr == -1:
                    curr = len(self.cache) - 1 # tail of cache
                while self.cache[curr][1] == 1:
                    self.cache[curr][1] = 0
                    curr -= 1
                    if curr == -1:
                        curr = len(self.cache) - 1 # tail of cache
                self.hand = curr - 1
                del self.cache[curr] # eviction
            # insert and set visited to 0
            self.cache.append([data,0])

if __name__ == "__main__":
    print("Hi")
    s = sieve(5)
    print(s.current_size())
    s.cache.append([1,0])
    s.cache.append([2,0])
    s.cache.append([3,0])
    s.cache.append([4,0])
    # s.cache.append([5,0])
    print(s.current_size())
    s.display()

    # cache hit
    s.read(2)
    s.read(3)
    s.display()

    #cache miss
    s.read(6)
    s.display()

    # cache hit
    s.read(6)
    s.display()

    #cache full
    s.read(7)
    s.display()

    # cache hit
    s.read(6)
    s.read(7)
    s.display()
    s.read(8)
    s.display()

# % python3 seive_cache_algo.py 
# 0
# 4
# [1, 0] [2, 0] [3, 0] [4, 0] 
# found [2, 1]
# found [3, 1]
# [1, 0] [2, 1] [3, 1] [4, 0] 
# [1, 0] [2, 1] [3, 1] [4, 0] [6, 0] 
# found [6, 1]
# [1, 0] [2, 1] [3, 1] [4, 0] [6, 1] 
# [1, 0] [2, 1] [3, 1] [6, 0] [7, 0] 
# found [6, 1]
# found [7, 1]
# [1, 0] [2, 1] [3, 1] [6, 1] [7, 1] 
# [2, 0] [3, 0] [6, 1] [7, 1] [8, 0] 
