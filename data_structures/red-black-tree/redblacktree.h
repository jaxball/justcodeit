#include <iostream>
#include <exception>
#include <cstdlib>
#include "bst.h"

/* -----------------------------------------------------
 * Red-Black Nodes and Search Tree
 * 
 * Author: Jason Lin
 * Date: 05-2015 
 ------------------------------------------------------*/

enum Color {red, black};

template <class KeyType, class ValueType>
class RedBlackNode : public Node<KeyType, ValueType>
{
public:
    RedBlackNode (KeyType k, ValueType v, RedBlackNode<KeyType, ValueType> *p)
    : Node<KeyType, ValueType> (k, v, p)
    { color = red; }
    
    virtual ~RedBlackNode () {}
    
    Color getColor () const
    { return color; }
    
    void setColor (Color c)
    { color = c; }
    
    virtual RedBlackNode<KeyType, ValueType> *getParent () const
    { return (RedBlackNode<KeyType,ValueType>*) this->_parent; }
    
    virtual RedBlackNode<KeyType, ValueType> *getLeft () const
    { return (RedBlackNode<KeyType,ValueType>*) this->_left; }
    
    virtual RedBlackNode<KeyType, ValueType> *getRight () const
    { return (RedBlackNode<KeyType,ValueType>*) this->_right; }
    
protected:
    Color color;
};

// Example:
// Node*n;
// colorOf(n) = red;
template <class KeyType, class ValueType>
Color& colorOf(Node<KeyType, ValueType>* input)
{
    return dynamic_cast<RedBlackNode<KeyType, ValueType>*>(input)->color;
}

// Example:
// Node* n;
// castToRbNode(n)->setColor(red);
template <class KeyType, class ValueType>
RedBlackNode<KeyType, ValueType>* castToRbNode(Node<KeyType, ValueType>* input)
{
    return dynamic_cast<RedBlackNode<KeyType, ValueType>*>(input);
}



/* -----------------------------------------------------
 * Red-Black Search Tree
 ------------------------------------------------------*/

template <class KeyType, class ValueType>
class RedBlackTree : public BinarySearchTree<KeyType, ValueType>
{
public:
    void insert (const std::pair<const KeyType, ValueType>& new_item) {
        if(this->root == NULL) {
            this->root = insertInTree(new_item.first, new_item.second, NULL, NULL);
        }
        else {
            this->root = insertInTree(new_item.first, new_item.second, (RedBlackNode<KeyType,ValueType>*) this->root, NULL);
        }
        RedBlackNode<KeyType, ValueType>* added_item = (RedBlackNode<KeyType,ValueType>*)this->internalFind(new_item.first);
        fixTree_case1(added_item);
        
    }
    
   
    
private:
    
    // Insert in tree, colored red, without fixing tree
    RedBlackNode<KeyType, ValueType>* insertInTree(const KeyType& k, const ValueType& v, RedBlackNode<KeyType, ValueType>* node, RedBlackNode<KeyType, ValueType>* previous) {
        // Adding first node to tree
        if (node == NULL) {
            RedBlackNode<KeyType, ValueType>* newNode = new RedBlackNode<KeyType, ValueType>(k, v, node);
            newNode->setLeft(NULL);
            newNode->setRight(NULL);
            newNode->setParent(previous);
            return newNode;
        }
        
        if(k < node->getItem().first) {
            node->setLeft(insertInTree(k, v, node->getLeft(), node));
            return node;
        }
        // go right
        else {
            node->setRight(insertInTree(k, v, node->getRight(), node));
            return node;
        }
    }
    
    void fixTree_case1(RedBlackNode<KeyType, ValueType>* node) {

        //Case 1: node is root of tree
        if (node->getParent()==NULL) {
            node->setColor(black);
        }
        else {
            fixTree_case2(node);
        }
    }
    
    void fixTree_case2(RedBlackNode<KeyType, ValueType>* node) {

        //Case 2: node's parent is black, no need to do anything
        if (node->getParent()->getColor() == black){
            return;
            //consider removing this check statement since its useless
        }
        else {
            fixTree_case3(node);
        }
    }
    
    void fixTree_case3(RedBlackNode<KeyType, ValueType>* node) {

        //Case 3: both parent and uncle are red
        RedBlackNode<KeyType, ValueType>* u = findMyUncle(node), *g;
        if ((u != NULL) && (u->getColor() == red)) {
            node->getParent()->setColor(black);
            u->setColor(black);
            g = findGrandparent(node);
            g->setColor(red);
            fixTree_case1(g);
        }
        else {
            fixTree_case4(node);
        }
    }
    
    void fixTree_case4(RedBlackNode<KeyType, ValueType>* node) {

        //Case 4: parent ia ews but uncle is black; added node is right child of parent (zig-zagg, case 5 in slides)
        RedBlackNode<KeyType, ValueType>* g = findGrandparent(node);
        
        if((node == node->getParent()->getRight()) && (node->getParent() == g->getLeft())) {
            LeftRotate(node, node->getParent());
            node = node->getLeft();
        }
        else if ((node == node->getParent()->getLeft()) && (node->getParent() == g->getRight())) {
            RightRotate(node, g);
            node = node->getRight();
        }
        fixTree_case5(node);
    }
    
    void fixTree_case5(RedBlackNode<KeyType, ValueType>* node) {

        RedBlackNode<KeyType, ValueType>* g = findGrandparent(node);
        
        node->getParent()->setColor(black);
        g->setColor(red);
        if (node == node->getParent()->getLeft()) {
            RightRotate(node->getParent(), g);
            
        }
        else {
            LeftRotate(node->getParent(), g);
        }
    }
    
    void RightRotate(RedBlackNode<KeyType, ValueType>* parent, RedBlackNode<KeyType, ValueType>* grandparent) {

        RedBlackNode<KeyType, ValueType>* saved_right_parent = parent->getRight();
        RedBlackNode<KeyType, ValueType>* grandgrandparent = grandparent->getParent();
        
        grandparent->setLeft(saved_right_parent);
        grandparent->setParent(parent);
        grandparent->setColor(red);
        
        parent->setRight(grandparent);
        parent->setParent(grandgrandparent);
        //set grandgrandparent;
        if (grandgrandparent != NULL) {
            if (grandparent == grandgrandparent->getLeft()) {
                grandgrandparent->setLeft(parent);
            }
            else if (grandparent == grandgrandparent->getRight()) {
                grandgrandparent->setRight(parent);
            }
        }
        
        parent->setColor(black);
        this->root = parent;
        while (this->root->getParent() != NULL) {
            this->root = this->root->getParent();
        }
        
        
    }
    
    void LeftRotate(RedBlackNode<KeyType, ValueType>* node, RedBlackNode<KeyType, ValueType>* parent) {

        RedBlackNode<KeyType, ValueType>* saved_left_n = node->getLeft();
        RedBlackNode<KeyType, ValueType>* grandparent = parent->getParent();
        node->setLeft(parent);
        node->setParent(grandparent);

        //set grandparent;
        if (grandparent != NULL) {
            if (parent == grandparent->getRight()) {
                grandparent->setRight(node);
            }
            else if (parent == grandparent->getLeft()) {
                grandparent->setLeft(node);
            }
        }
        node->setColor(black);
        
        parent->setRight(saved_left_n);
        parent->setParent(node);
        parent->setColor(red);
        
        this->root = node;
        while (this->root->getParent() != NULL) {
            this->root = this->root->getParent();
        }
        //and modify the parent's nodes properly
        
    }
    
    RedBlackNode<KeyType, ValueType>* search(RedBlackNode<KeyType, ValueType>* node, const std::pair<KeyType, ValueType>& query_item) {
        
        if(node == NULL)
            return NULL;    // found
        if(query_item.first == node->getItem().first)
            return node;    // go left
        if(query_item.first < node->getItem().first) {
            return search(node->getLeft(), query_item);
        } else {
            return search(node->getRight(), query_item);
        }
    }
    
    RedBlackNode<KeyType, ValueType>* findGrandparent(RedBlackNode<KeyType, ValueType>* n) {
        
        if ((n != NULL) && (n->getParent() != NULL)) {
            return n->getParent()->getParent();
        }
        else {
            return NULL;
        }
    }
    
    RedBlackNode<KeyType, ValueType>* findMyUncle(RedBlackNode<KeyType, ValueType>* n) {
        
        //how to know if I'm a left child or right child
        RedBlackNode<KeyType, ValueType>* g = findGrandparent(n);
        //could not find grandparent, so no uncle
        if (g == NULL) {
            return NULL;
        }
        if (n->getParent() == g->getLeft()) {
            return g->getRight();
        }
        else {
            return g->getLeft();
        }
    }
    
};



