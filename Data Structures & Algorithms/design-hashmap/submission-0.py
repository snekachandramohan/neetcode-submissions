class MyHashMap:

    def __init__(self):
        self.array_size = 10007
        self.buckets = []
        for i in range(self.array_size):
            self.buckets.append([])

    def put(self, key: int, value: int) -> None:
        index = key % self.array_size
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return None
        bucket.append([key,value])

    def get(self, key: int) -> int:
        index = key % self.array_size
        bucket = self.buckets[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.array_size
        bucket = self.buckets[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                return
        
