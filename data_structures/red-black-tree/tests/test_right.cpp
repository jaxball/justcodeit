#include "./redblacktree.h"
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main () {
	int key = 2; 
	string val = "hello";
	RedBlackNode<int, string>* testRBNode = new RedBlackNode<int, string>(key, val, NULL);

	RedBlackTree<int, string> testRBT;
	testRBT.insert(make_pair(7, "seven"));
	testRBT.print();
	testRBT.insert(make_pair(10, "ten"));
	testRBT.print();
	testRBT.insert(make_pair(13, "thirteen"));
	testRBT.print();


	RedBlackTree<int, string>::iterator it = testRBT.begin();
	cout << it->first << endl;
	++it;
	cout << it->first << endl;

	// [[[[[ (-1, -one) ] (0, zero) ] (1, one) ] (2, two) [[ (3, three) ] (4, four) [ (5, five) ]]] (7, seven) ]
	return 0;
}