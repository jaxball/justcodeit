"""
Towers of Hanoi: In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes 
which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom
(i.e. each disk sits on top of an even larger one). You have the following constraints: 
(1) Only one disk can be moved at a time.
(2) A disk is slid off the top of one tower onto another tower.
(3) A disk cannot be placed on top of a smaller disk. 
Write a program to move the disks from the first tower to the last using Stacks.
"""

def towerHanoi(start, helper, dest, n):

	if n = 1: 
		move(start, dest)	# move disk from start to destination

	towerHanoi(start, dest, helper, n-1)
	move(start, dest)
	towerHanoi(helper, start, dest, n-1)


""" Rest needs to be implemented by stack, less trivial on the algorithms so come back later """