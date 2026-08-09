class MyHashSet:

    def __init__(self):
        self.array_size = 16
        self.buckets = []
        for i in range(self.array_size):
            self.buckets.append([])

    def add(self, key: int) -> None:
        # get index by hasing and mod
        index = key % self.array_size
        # grab the bucket at that index
        bucket = self.buckets[index]
        # check if already available if not add
        if key in bucket:
            return None
        else:
            bucket.append(key)
            return None

    def remove(self, key: int) -> None:
        # get index by hasing and mod
        index = key % self.array_size
        # grab the bucket at that index
        bucket = self.buckets[index]
        # check if already available and remove
        if key in bucket:
            bucket.remove(key)
        

    def contains(self, key: int) -> bool:
        # get index by hasing and mod
        index = key % self.array_size
        # grab the bucket at that index
        bucket = self.buckets[index]
        # check if already available
        return key in bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)