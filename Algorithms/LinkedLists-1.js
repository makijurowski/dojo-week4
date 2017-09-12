/* This is a Coding Dojo algorithms practice assignment.

LINKED LISTS
- Series of individual nodes (e.g. tiles on the floor, scavenger hunt directions)
- The first node in a LL is called the 'head'
- Each node consists of data and a pointer to the next node, even if null
- Nodes can be decalred as object literals or via constructor



var myLinkedList = { head: null };

function makeNewNode(val) {
    this.val = val;
    this.next = null;
}

var firstNode = new makeNewNode(5);

function addFront(head, value) {
    var newFirstNode = new makeNewNode(value);
    newFirstNode.next = head;
    myLinkedList.head = newFirstNode;
    return myLinkedList;
}

addFront(firstNode, 3);
console.log(myLinkedList.head);

*/

firstNode = {
    val: 1,
    next: null
};

myList = { head: firstNode };

function findMax(myList) {
    var myMax = myList.val;
    var node = myList.head;
    while (node){
        if (node.val > myMax) {
            myMax = node.val;
            node = node.next;
        }
    }
    return myMax;
}

console.log(findMax(myList));