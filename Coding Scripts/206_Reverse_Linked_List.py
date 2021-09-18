class Solution:
  def RLL_iterative(self, head):
    prev = None
    curr = head
    while curr:
      temp = curr.next # 留联系方式
      curr.next = prev # 转向 （主要逻辑）
      prev = curr # move forward
      curr = temp
    return prev
  
  def RLL_recursive(self, head):
    # 归纳法：base case + a_n=f(a_(n-1)) => f(head.next); head.next.next, head.next = head, None
    if not head or not head.next:
      return head
    else:
      new_head = self.RLL_recursive(head.next)
      head.next.next, head.next = head, None # 最后反转head
    return new_head



