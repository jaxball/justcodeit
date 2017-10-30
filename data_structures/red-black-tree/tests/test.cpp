#include "../redblacktree.h"
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main () {
    string val = "hello";
    // RedBlackNode<int, string>* testRBNode = new RedBlackNode<int, string>(key, val, NULL);
    
    RedBlackTree<int, string> testRBT;
    testRBT.insert(make_pair(7, "seven"));
    testRBT.print();
    testRBT.insert(make_pair(2, "two"));
    testRBT.print();
    testRBT.insert(make_pair(1, "one"));
    testRBT.print();
    testRBT.insert(make_pair(4, "four"));
    testRBT.print();
    testRBT.insert(make_pair(0, "zero"));
    testRBT.print();
    testRBT.insert(make_pair(-1, "-one"));
    testRBT.print();
    // // testRBT.insert(make_pair(7, "seven"));
    testRBT.insert(make_pair(3, "three"));
    testRBT.print();
    testRBT.insert(make_pair(5, "five"));
    testRBT.print();
    testRBT.insert(make_pair(6, "six"));
    testRBT.print();
    
    //testRBT.print();
    
    RedBlackTree<int, string>::iterator it = testRBT.begin();
    for (it=testRBT.begin(); it != testRBT.end(); ++it) {
        cout << it->first << endl;
    }
    
    try {
        ++it;
        cout << it->first << endl;
        
    }
    catch (std::out_of_range& o) {
        std::cout << o.what() << std::endl;
    }

	return 0;
}