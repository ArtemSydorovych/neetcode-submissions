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
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> heap = new PriorityQueue<>(Comparator.comparingInt(el -> el.val));
        for (ListNode head : lists){
            if (head != null) heap.offer(head);
        }

        ListNode dummy = new ListNode(0), tail = dummy;
        while(!heap.isEmpty()){
            ListNode min = heap.poll();
            tail.next = min; 
            tail = min;
            if(min.next != null) heap.offer(min.next);
        }

        return dummy.next;
    }
}
