class Solution:
    def insertAtEnd(self, head, x):
        newNode = Node(x)

        # If linked list is empty
        if head is None:
            return newNode

        # Go to the last node
        temp = head
        while temp.next is not None:
            temp = temp.next

        # Add new node at the end
        temp.next = newNode

        return head