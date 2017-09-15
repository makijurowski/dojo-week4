// List constructor function 
function myList() {
    this.head = 'null',
        this.length = 0,
        this.allValues = [],
        this.newNode = (function ListNode(val) {	// Node constructor function
            this.val = val;
            this.next = null;});
}

// Used to generate a random value between 0-10
function randomNum(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

// Used to make a new singly linked list given n number of nodes 
// with random values between the min and max.
function genListAndRandomNodes(n, min, max) {
    // Make a new list using constructor
    var currentList = new myList(n);
    var node = new currentList.newNode(randomNum(min, max));
    currentList.allValues.push(node.val);
    currentList.length += 1;
    currentList.head = node;
    while (currentList.length < n) {
        let newNode = new currentList.newNode(randomNum(min, max));
        currentList.allValues.push(newNode.val);
        node.next = newNode;
        node = newNode;
        currentList.length += 1;
    }
    return currentList;
}

// Create a new singly linked list with randomized node values
var newList = genListAndRandomNodes(6, 2, 5);

// Check the node values (contained in a array) 
console.log(newList.allValues);

function ListNode(val) {	            // Node constructor function
    this.val = val;
    this.next = null;
}

function prependVal(val, before, list) {
    // Insert a new list node with a given value before the given node
    var node = list.head;
    while (node) {
        if (!node.next) {
            node.next = new ListNode(val);
            list.length += 1;
            return list;
        }
        else if (node.next.val == before) {
            var newNext = node.next;
            var newNode = new ListNode(val);
            node.next = newNode;
            newNode.next = newNext;
            list.length += 1;
            return list;
        }
        node = node.next;
    }
}

function appendVal(val, after, list) {
    var node = list.head;
    while (node) {
        if (!node.next) {
            node.next = new ListNode(val);
            list.length += 1;
            return list;
        }
        else if (node.val == after) {
            var newNext = node.next;
            var newNode = new ListNode(val);
            node.next = newNode;
            newNode.next = newNext;
            list.length += 1;
            return list;
        }
        node = node.next;
    }
}

appendVal(100, 4, newList);