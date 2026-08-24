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
        PriorityQueue<ListNode> heap = new PriorityQueue<>((a,b) -> Integer.compare(a.val,b.val));
        ListNode dummy = new ListNode();
        ListNode head = dummy;
        for(ListNode node : lists){
            if (node != null) heap.offer(node);
        }

        while(!heap.isEmpty()){
            var node = heap.poll();
            if(node.next != null){
                heap.offer(node.next);
            }
            head.next = node;
            head = node;
        }

        return dummy.next;
    }
}
