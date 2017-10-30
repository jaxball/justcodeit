/**
 * bst.h
 *  Implements a(n unbalanced) BST storing Key,Value pairs
 */

#include <iostream>
#include <exception>
#include <stdexcept>
#include <cstdlib>
#include <utility>

/* -----------------------------------------------------
 * Regular Binary Tree Nodes
 ------------------------------------------------------*/

template <class KeyType, class ValueType>
class Node {
public:
    Node (const KeyType & k, const ValueType & v, Node<KeyType, ValueType> *p)
    : _item(k, v)
    // the default is to create new nodes as leaves
    { _parent = p; _left = _right = NULL; }
    
    virtual ~Node()
    { }
    
    std::pair<const KeyType, ValueType> const & getItem () const
    { return _item; }
    
    std::pair<const KeyType, ValueType> & getItem ()
    { return _item; }
    
    const KeyType & getKey () const
    { return _item.first; }
    
    const ValueType & getValue () const
    { return _item.second; }
    
    /* the next three functions are virtual because for Red-Black-Trees,
     we'll want to use Red-Black nodes, and for those, the
     getParent, getLeft, and getRight functions should return
     Red-Black nodes, not just ordinary nodes.
     That's an advantage of using getters/setters rather than a struct. */
    
    virtual Node<KeyType, ValueType> *getParent () const
    { return _parent; }
    
    virtual Node<KeyType, ValueType> *getLeft () const
    { return _left; }
    
    virtual Node<KeyType, ValueType> *getRight () const
    { return _right; }
    
    
    void setParent (Node<KeyType, ValueType> *p)
    { _parent = p; }
    
    void setLeft (Node<KeyType, ValueType> *l)
    { _left = l; }
    
    void setRight (Node<KeyType, ValueType> *r)
    { _right = r; }
    
    void setValue (const ValueType &v)
    { _item.second = v; }
    
protected:
    std::pair<const KeyType, ValueType> _item;
    Node <KeyType, ValueType> *_left, *_right, *_parent;
};

/* -----------------------------------------------------
 * Regular Binary Search Tree
 ------------------------------------------------------*/

template <class KeyType, class ValueType>
class BinarySearchTree {
protected:
    // Main data member of the class
    Node<KeyType, ValueType> *root;
    
public:
    /**
     * Constructor
     */
    BinarySearchTree () { root = NULL; }
    
    /**
     * Destructor
     */
    ~BinarySearchTree () { deleteAll (root); }
    
    /**
     * Prints the entire tree structure in a nice format
     *
     * It will denote subtrees in [] brackets.
     *  This could be helpful if you want to debug your functions.
     */
    void print () const
    {
        printRoot (root);
        std::cout << "\n";
    }
    
    /**
     * An In-Order iterator
     *  !!! You must implement this !!!
     */
    class iterator {
    public:
        /**
         * Initialize the internal members of the iterator
         */
        
        friend class Node<KeyType, ValueType>;
        
        //Default constructor - should it be public or not
        iterator() {
            curr = NULL;
        }
        
        iterator(Node<KeyType,ValueType>* ptr) : curr(ptr) {}
        
        std::pair<const KeyType,ValueType>& operator*()
        { return curr->getItem();  }
        
        std::pair<const KeyType,ValueType>* operator->()
        { return &(curr->getItem()); }
        
        /**
         * Checks if 'this' iterator's internals have the same value
         *  as 'rhs'
         */
        bool operator==(const iterator& rhs) const {
            return curr->_item.first == rhs->_item.first && curr->_item.second == rhs->curr->_item.second;
        }
        
        /**
         * Checks if 'this' iterator's internals have a different value
         *  as 'rhs'
         */
        // bool operator!=(const iterator& rhs) const {
        //   return curr->_item.first != rhs->_item.first || curr->_item.second != rhs->curr->_item.second;
        // }
        
        /**
         * Non const version of comparator for use with for loops
         *
         */
        bool operator!=(iterator& rhs) {
            return curr->_item.first != rhs->_item.first || curr->_item.second != rhs->curr->_item.second;
        }
        
        /**
         * Advances the iterator's location using an in-order sequencing
         */
        iterator& operator++() {
            if (curr == NULL)
            {
                // ++ from end(). get the root of the tree
                //curr = BinarySearchTree::root;
                
                // error! ++ requested for an empty tree
                if (curr == NULL) {
                    throw
                    std::out_of_range("stree iterator operator++ (): tree empty");
                }
                
                // move to the smallest value in the tree,
                // which is the first node inorder
                while (curr->getLeft() != NULL) {
                    curr = curr->getLeft();
                }
            }
            else
                if (curr->getRight() != NULL)
                {
                    // successor is the furthest left node of
                    // getRight() subtree
                    curr = curr->getRight();
                    
                    while (curr->getLeft() != NULL) {
                        curr = curr->getLeft();
                    }
                }
                else
                {
                    // have already processed the left subtree, and
                    // there is no getRight() subtree. move up the tree,
                    // looking for a parent for which curr is a left child,
                    // stopping if the parent becomes NULL. a non-NULL parent
                    // is the successor. if parent is NULL, the original node
                    // was the last node inorder, and its successor
                    // is the end of the list
                    Node<KeyType, ValueType>* p = curr->getParent();
                    while (p != NULL && curr == p->getRight())
                    {
                        curr = p;
                        p = p->getParent();
                    }
                    
                    // if we were previously at the getRight()-most node in
                    // the tree, curr = NULL, and the iterator specifies
                    // the end of the list
                    curr = p;
                }
            return *this;
        }
        
        operator bool() {
            return curr != NULL;
        }
        
    protected:
        Node<KeyType, ValueType>* curr;
        //you are welcome to add any necessary variables and helper functions here.
        //iterator(Node<KeyType, ValueType>* init) : curr(init) {}
        
    };
    
    /**
     * Returns an iterator to the "smallest" item in the tree
     */
    iterator begin() {
        Node<KeyType, ValueType>* curr = root;
        while (curr->getLeft()!=NULL) {
            curr = curr->getLeft();
        }
        
        iterator it(curr);
        return it;
    }
    
    /**
     * Returns an iterator whose value means INVALID
     */
    iterator end() {
        iterator it(NULL);
        return it;
    }
    
    /**
     * Returns an iterator to the item with the given key, k
     * or the end iterator if k does not exist in the tree
     */
    iterator find (const KeyType & k) const
    {
        Node<KeyType, ValueType> *curr = internalFind(k);
        iterator it(curr);
        return it;
    }
    
    
protected:
    /**
     * Helper function to find a node with given key, k and
     * return a pointer to it or NULL if no item with that key
     * exists
     */
    Node<KeyType, ValueType>* internalFind(const KeyType& k) const 
    {
        Node<KeyType, ValueType> *curr = root;
        while (curr) {
            if (curr->getKey() == k) {
                return curr;
            } else if (k < curr->getKey()) {
                curr = curr->getLeft();
            } else {
                curr = curr->getRight();
            }
        }
        return NULL;
    }
    
    /**
     * Helper function to print the tree's contents
     */
    void printRoot (Node<KeyType, ValueType> *r) const
    {
        if (r != NULL)
        {
            std::cout << "[";
            printRoot (r->getLeft());
            std::cout << " (" << r->getKey() << ", " << r->getValue() << ") ";
            printRoot (r->getRight());
            std::cout << "]";
        }
    }
    
    /**
     * Helper function to delete all the items
     */
    void deleteAll (Node<KeyType, ValueType> *r)
    {
        if (r != NULL)
        {
            deleteAll (r->getLeft());
            deleteAll (r->getRight());
            delete r;
        }
    }
};

/* Feel free to add member function definitions here if you need */
