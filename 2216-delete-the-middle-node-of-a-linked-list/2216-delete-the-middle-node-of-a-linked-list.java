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
    public ListNode deleteMiddle(ListNode head) {

        if(head == null || head.next == null){
            return null;
        }
        int size = size_of_ll(head);
        int pos = size/2 ;

        ListNode temp = head;
        while(pos != 1){
            pos--;
            temp = temp.next;
        }
        //System.out.print(temp.val);
        if(temp.next != null){
            temp.next = temp.next.next;
        }else{
            temp.next = null;
        }
        
        return head;
    }

    public int size_of_ll(ListNode head){
        ListNode temp = head;
        int size = 0;
        while(temp != null){
            size++;
            temp = temp.next;
        }

        return size;
    }
}