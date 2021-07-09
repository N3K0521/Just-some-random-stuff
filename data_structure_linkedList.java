//head node
private Node head;
//tail node 
private Node last;
//size of the linked list
private int size;

/**
 * the inserted element of the linked list
 * @param data inserted element
 * @param index inserted position
 */

 public void insert(int data, int index) throws Exception {
     if (index <0 || index > size){
         throw new IndexOutOfBoundsException("Index out of bounds exception!");
     }
     Node insertedNode = new Node(data);
     if(size == 0){
         //empty linked list
         head = insertedNode;
         last = insertedNode;
     }
     else if (index == 0){
         //head insert
         insertedNode.next = head; //the new inserted node's pointer has pointed to the original head node
         head = insertedNode; //let the new inserted node to become the new head node
     }
     else if (size == index){
         //end insert
         last.next = insertedNode;
         last = insertedNode;
     }
     else{
         //insert in the middle
         Node prevNode = get(index-1); //let the node which is one position before (prev) the inserted position to become "prevNode"
         insertedNode.next = prevNode.next; //let the inserted node's pointer (next) pointing to the node of the inserted position
         prevNode.next = insertedNode; // let the prev. node's pointer pointing to the inserted node
     }
     size ++;
 }

 /**
  * delete element
  * @param index deleted position
  */

  public Node remove(int index) throws Exception{
      if (index < 0 || index > size) {
        throw new IndexOutOfBoundsException("Index out of bounds exception!");
    } 
    Node removedNode = null;
    if(index == 0){
        //delete the head node
        removedNode = head;
        head = head.next;
    }
    else if (index == size - 1){
        //delete the tail node
        Node prevNode = get(index-1); //找出要删除的node的前一个节点
        removedNode = prevNode.next; //删除的node成为倒数第二个节点的next指针指向的节点
        prevNode.next = null; //将倒数第二个节点指向空
        last = prevNode; //倒数第二个节点成为尾部节点
    }
    else {
        //delete any node in between the head & tail
        Node prevNode = get(index-1);
        Node nextNode = prevNode.next.next;
        removedNode = prevNode.next;
        prevNode.next = nextNode;
    }
    size --;
    return removedNOde;
  }

  /**
   * search index
   * @param index searched position
   */
public Node get(int index) throws Exception {
    if (index < 0 || index > size) {
        throw new IndexOutOfBoundsException("Index out of bounds exception!");
    } 
    Node temp = head;
    for(int i=0; i < index; i++){
        temp = temp.next;
    }
    return temp;
}

/**
 * print the linked list
 */
public void output(){
    Node temp = head;
    while (temp!= true){
        System.out.println(temp.data);
        temp = temp.next;
    }
    return temp;
}

/**
 * node
 */
private static class Node {
    int data;
    Node next;
    Node(int data){
        this.data = data;
    }
}

public static void main(String[] args) throws Exception{
    MyLinkedList myLinkedList = new MyLinkedList();
    myLinkedList.insert(3,0);
    myLinkedList.insert(7,1);
    myLinkedList.insert(9,2);
    myLinkedList.insert(5,3);
    myLinkedList.insert(6,1);
    myLinkedList.remove(0);
    myLinkedList.output();
}