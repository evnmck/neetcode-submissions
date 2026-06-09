class LRUCache:


    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = {}

        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.vals:
            curr = self.vals[key]
            self.Delete(curr)
            self.Add(curr)
            return curr.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.vals:
            node = self.vals[key]
            node.value = value
            self.Delete(node)
            self.Add(node)
        else:
            new_node = self.Node(key,value)
            self.vals[key] = new_node
            self.Add(new_node)

            if len(self.vals) > self.cap:
                least_used = self.tail.prev
                self.vals.pop(least_used.key, None)
                self.Delete(least_used)


    def Add(self, node: Node):
        old = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = old
        old.prev = node

    def Delete(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


       
        
