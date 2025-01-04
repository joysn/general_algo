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


# ##################### #
# Second Implementation #
# ##################### #

class Node:
    def __init__(self, value):
        self.value = value
        self.visited = 0
        self.next = None
        self.prev = None

class Cache:
    def __init__(self,size):
        self.size = size
        self.cache = {}
        self.head = None
        self.tail = None
        self.hand = None

    def insert_at_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail == None:
            self.tail = node

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        node.prev = node.next = None

    def access(self, x):
        if x in self.cache: # cache hit
            node = self.cache[x]
            node.visited = 1
        else: # cache miss
            if len(self.cache) == self.size: #cache full
                curr = self.hand
                if curr is None:
                    curr = self.tail
                while curr.visited == 1:
                    curr.visited = 0
                    curr = curr.prev
                    if curr is None:
                        curr = self.tail
                self.hand = curr.prev
                self.remove_node(curr)
                del self.cache[curr.value]
            new_node = Node(x)
            self.insert_at_head(new_node)
            self.cache[x] = new_node
            new_node.visited = 0

# Example usage
cache = Cache(3)
requests = [1, 2, 3, 1, 4, 5]
for req in requests:
    cache.access(req)
    print(f"Cache state after accessing {req}: {[node.value for node in cache.cache.values()]}")

# % python3 seive_cache_algo2.py
# Cache state after accessing 1: [1]
# Cache state after accessing 2: [1, 2]
# Cache state after accessing 3: [1, 2, 3]
# Cache state after accessing 1: [1, 2, 3]
# Cache state after accessing 4: [1, 3, 4]
# Cache state after accessing 5: [1, 4, 5]
