from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def isBinaryHeapTree(root):
  # List to store 'node, position'.
  nodeArr = [(root, 1)]
  i = 0

  while i < len(nodeArr):

    node, position = nodeArr[i]
    i += 1

    # If left child is not 'None'.
    if(node.left):

    # Append left child.
      nodeArr.append((node.left, 2*position))

           
      if(node.left.data > node.data):

        return False

        # If right child is not 'None'.
    if(node.right):

            # Append right child.
      nodeArr.append((node.right, 2*position+1))

           
      if(node.right.data > node.data):

        return False

  return nodeArr[-1][1] == len(nodeArr)


    # Write your code here.
  