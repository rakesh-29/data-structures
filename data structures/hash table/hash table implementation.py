class hash_table:
    def __init__(self):
        self.max=100
        self.arr=[[] for i in range(self.max)]

    def get_hash(self,key):
        total=0
        for char in key:
            total =total+ord(char)
        return total % self.max

    def __setitem__(self, key, value):
        arr_index=self.get_hash(key)
        found=False
        for index,element in enumerate(self.arr[arr_index]):
            if len(element)==2 and element[0]==key:
                self.arr[arr_index][index]=(key,value)
                found=True

        if not found:
            self.arr[arr_index].append((key,value))

    def __getitem__(self, item):
        arr_index=self.get_hash(item)
        for element in self.arr[arr_index]:
            if element[0]==item:
                return element[1]

    def __delitem__(self, key):
        arr_index=self.get_hash(key)
        for index,element in enumerate(self.arr[arr_index]):
            if element[0]==key:
                del self.arr[arr_index][index]


h=hash_table()
h["march 1"]=120
h["march 2"]=220
print(h["march 1"])