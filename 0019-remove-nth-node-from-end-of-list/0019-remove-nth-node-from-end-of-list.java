/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        int size = size_ll(head);
        if(size == n){
            head = head.next;
            return head;
        }
        System.out.print(size);
        size = size - n;
    
        ListNode temp = head;
        while(size != 1 && temp.next!=null){
            size--;
            temp = temp.next;
        }

        if(temp.next!= null){
            temp.next = temp.next.next;
        }else{
            temp.next = null;
        }

        return head;
    }

    public int size_ll(ListNode head){
        ListNode temp = head;
        int size = 0;
        while(temp!=null){
            size++;
            temp = temp.next;
        }

        return size;
    }
}