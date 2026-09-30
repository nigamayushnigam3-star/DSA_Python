class Solution:
    def getCount(self, head):
        count = 0
        temp = head

        while temp is not None:
            count += 1
            temp = temp.next

        return count