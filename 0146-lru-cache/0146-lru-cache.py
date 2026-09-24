class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left 
    def add(self,node):
        node.prev=self.right.prev
        node.next=self.right
        self.right.prev.next=node
        self.right.prev=node
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
    def move_to_mru(self,node):
        self.remove(node)
        self.add(node)    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.move_to_mru(node)
        return node.value   
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.move_to_mru(node)
        else:
            if len(self.cache)==self.capacity:
                iru=self.left.next
                self.remove(iru)
                del self.cache[iru.key]
            new_node=Node(key,value)
            self.cache[key]=new_node
            self.add(new_node)    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)