class Node:
    def __init__(self, number):
        self.spine = number
        self.left = None
        self.right = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Add node at the end
    def append(self, number):
        new_node = Node(number)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    # Add node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Print the list
    def display(self):
        current = self.head
        while current:
            print(current.left, "-", current.spine, "-", current.right)
            if current.next:
                print("    |    ")
            current = current.next
    
    # Delete a node by value
    def delete(self, number):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

list = [4,3,3,6,9,5,2,3,7,6,1,4,6,3,3,4,1,6,2,2,3,5,2,1,7,3,5,1,7,9]
fishbone = LinkedList()
for i in range(len(list)):
    if not fishbone.head:
        fishbone.append(list[i])
    else:
        current = fishbone.head
        while current:
            if list[i] < current.spine:
                if not current.left:
                    current.left = list[i]
                    break
                else:
                    current = current.next
            elif list[i] > current.spine:
                if not current.right:
                    current.right = list[i]
                    break
                else:
                    current = current.next
            else:
                current = current.next
            if not current:
                fishbone.append(list[i])
fishbone.display()
