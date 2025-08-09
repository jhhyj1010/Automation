# Key Points of Inheritance and Binary Trees

## Inheritance

Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit properties and methods from another class.

### Key Points of Inheritance:

#### 1. **Basic Syntax**
```python
class ParentClass:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")

class ChildClass(ParentClass):  # Inheritance syntax
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
    
    def display(self):
        super().display()  # Call parent method
        print(f"Age: {self.age}")
```

#### 2. **Types of Inheritance**
- **Single Inheritance**: One class inherits from one parent
- **Multiple Inheritance**: One class inherits from multiple parents
- **Multilevel Inheritance**: Chain of inheritance (A → B → C)
- **Hierarchical Inheritance**: Multiple classes inherit from one parent

#### 3. **Method Overriding**
```python
class Animal:
    def make_sound(self):
        print("Some sound")

class Dog(Animal):
    def make_sound(self):  # Override parent method
        print("Woof!")
```

#### 4. **Access Modifiers**
- **Public**: Accessible everywhere
- **Protected**: Accessible within class and subclasses (prefix with `_`)
- **Private**: Accessible only within class (prefix with `__`)

#### 5. **Abstract Classes**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2
```

## Binary Trees

A binary tree is a hierarchical data structure where each node has at most two children, referred to as left and right child.

### Key Points of Binary Trees:

#### 1. **Basic Structure**
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
```

#### 2. **Types of Binary Trees**
- **Full Binary Tree**: Every node has 0 or 2 children
- **Complete Binary Tree**: All levels are filled except possibly the last
- **Perfect Binary Tree**: All internal nodes have 2 children
- **Balanced Binary Tree**: Height difference between left and right subtrees is at most 1

#### 3. **Binary Search Tree (BST)**
```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
```

#### 4. **Tree Traversal Methods**

**Depth-First Search (DFS):**
```python
def dfs_in_order(self):
    results = []
    
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)
    
    traverse(self.root)
    return results

def dfs_pre_order(self):
    results = []
    
    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
    
    traverse(self.root)
    return results

def dfs_post_order(self):
    results = []
    
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.value)
    
    traverse(self.root)
    return results
```

**Breadth-First Search (BFS):**
```python
def bfs(self):
    current_node = self.root
    queue = []
    results = []
    queue.append(current_node)
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        results.append(current_node.value)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
    return results
```

#### 5. **Common Operations**
- **Insert**: Add a new node
- **Search/Contains**: Find a specific value
- **Delete**: Remove a node
- **Find Minimum/Maximum**: Find smallest/largest value
- **Height**: Calculate tree height
- **Size**: Count total nodes

#### 6. **Time Complexity**
- **Average Case**: O(log n) for balanced trees
- **Worst Case**: O(n) for unbalanced trees (degenerate to linked list)

### Practical Example Combining Both Concepts:

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeTraversal:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        # Implementation here
        pass
    
    def traverse(self, method="inorder"):
        if method == "inorder":
            return self._inorder_traversal(self.root)
        elif method == "preorder":
            return self._preorder_traversal(self.root)
        elif method == "postorder":
            return self._postorder_traversal(self.root)

class SpecializedTree(TreeTraversal):  # Inheritance
    def __init__(self):
        super().__init__()
        self.node_count = 0
    
    def insert(self, value):
        super().insert(value)  # Call parent method
        self.node_count += 1   # Add specialized behavior
    
    def get_node_count(self):
        return self.node_count
```

### Key Takeaways:

**Inheritance:**
- Promotes code reuse and establishes relationships between classes
- Enables polymorphism and method overriding
- Supports the "is-a" relationship
- Can lead to complex hierarchies if overused

**Binary Trees:**
- Efficient for searching and sorting operations
- Foundation for more complex data structures (AVL, Red-Black trees)
- Used in database indexing, file systems, and expression parsing
- Traversal order affects the sequence of processing nodes 