class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0) # Dummy node to simplify result list construction
        current = dummy_head # Pointer to the current node in the result list
        carry = 0 # Initialize carry to 0

        while l1 or l2 or carry: # Continue until both lists are exhausted and no carry remains
            val1 = l1.val if l1 else 0 # Get value from l1 or 0 if l1 is exhausted
            val2 = l2.val if l2 else 0 # Get value from l2 or 0 if l2 is exhausted

            total = val1 + val2 + carry # Sum the values and carry
            carry = total // 10 # Update carry for next iteration
            current.next = ListNode(total % 10) # Create a new node with the digit value
            current = current.next # Move to the next node in the result list

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next # Return the next node of dummy head as the result list

    def addTwoNumbers_s2(self, l1, l2):
        i1= 0
        i2= 0
        i = 0 
        
        while l1 is not None: # traverse the first linked list
            i1 = i1 + l1.val * (10**i) # convert linked list to integer
            l1 = l1.next # move to the next node
            i = i + 1 # increment the position
        i = 0 # reset position for the second linked list

        while l2 is not None:
            i2 = i2 + l2.val * (10**i)
            l2 = l2.next
            i = i + 1
        i3 = i1 + i2

        if i3 == 0: # edge case for 0
            return ListNode(0) # return a node with value 0
        
        dummy = ListNode(0) # dummy node to simplify result list construction
        current = dummy # pointer to the current node in the result list

        while i3 > 0: 
            digit = i3 % 10 # get the last digit
            current.next = ListNode(digit) # create a new node with the digit value
            current = current.next # move to the next node in the result list
            i3 = i3 // 10 # remove the last digit from the integer

        return dummy.next # return the next node of dummy head as the result list