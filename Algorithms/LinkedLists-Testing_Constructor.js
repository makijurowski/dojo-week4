// List constructor function 
function myList() {
    this.head = 'null',
        this.length = 1,
        this.allValues = [],
        this.minValArr = [],
        this.minPrevArr = [],
        this.newNode = function newLLNode(val) {	// Node constructor function
            this.val = val,
                this.next = null
        }
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
    var node = new currentList.newNode(currentList.length);
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
var newList = genListAndRandomNodes(10, 0, 10);

// Check the node values (contained in a array) 
console.log(newList.allValues);

