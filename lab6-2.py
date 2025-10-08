from lab6 import Node

class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False


    def append(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode
        print( data)

        
        

    def insert(self, index, data):
        if index < 0:
            print("Index cannot be negative")
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        
        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1
        
        if current is None:
            print("Index not in range")
        
        newNode.next = current.next
        current.next = newNode

#   POP
    def pop(self, index=None):
        if self.is_empty():
            print("Pop from empty list")
    
        if index is None:
            if self.head.next is None:
                # Only one element
                data = self.head.data
                self.head = None
                return data
        
            current = self.head
            while current.next.next:
                current = current.next
            data = current.next.data
            current.next = None
            return data
    
        if index < 0:
            print("Index cannot be negative")
    
        if index == 0:
            data = self.head.data
            self.head = self.head.next
            return data
    
        current = self.head
        count = 0
        while current.next and count < index - 1:
            current = current.next
            count += 1
    
        if current.next is None:
            print("Index out of range")
    
        data = current.next.data
        current.next = current.next.next
        return data

    def remove_at_index(self, index):
        return self.pop(index)

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        print("None")


if __name__ == "__main__":
# Create linked list object
    linked_list = SinglyLinkedList()
# Example operations:
linked_list.append(10)
print("-----------------------------")
linked_list.append(20)
print("-----------------------------")

linked_list.append(30)
print("-----------------------------")

linked_list.display()
print("-----------------------------")

linked_list.insert(1, 15)
print("-----------------------------")

linked_list.display()
print("-----------------------------")

linked_list.pop()
print("-----------------------------")

linked_list.display()
print("-----------------------------")

linked_list.pop(0)
print("-----------------------------")

linked_list.display()
print("-----------------------------")

pos = linked_list.search(20)
print("Found at index:", pos)
pass