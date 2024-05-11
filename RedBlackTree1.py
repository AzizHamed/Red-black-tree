# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 20:55:46 2024

@author: azizh
"""
import time

class Tree:
    def __init__(self):
        self.Root = None

    def __repr__(self):
        repr = ""
        return self.inOrderTraversal(self.Root, repr)

    def inOrderTraversal(self, node, repr):
        if node is None:
            return repr
        repr = self.inOrderTraversal(node.left, repr)
        repr += "------------------\n(" + str(node.value) + "," + node.color + ")\n"
        repr = self.inOrderTraversal(node.right, repr)
        return repr
    
    
    def in_order_traversal2(self, root):
        if root is not None:
            yield from self.in_order_traversal2(root.left)
            yield root
            yield from self.in_order_traversal2(root.right)
            
            
    def addGroup(self, group):
        
        for value in group:
            self.Insert(value)
            
            
    #def DeleteGroup(self, group):
       # for value in group:
         #   self.Delete(value)
            
    def writeToFile(self, filename):
        with open(filename, 'w') as file:
            self._writeTreeToFile(self.Root, file) 
            
            
    def _writeTreeToFile(self, node, file):
        if node is None:
            return
        self._writeTreeToFile(node.left, file)
        file.write("{:f}\n".format(node.value))  # Use {:f} for standard notation
        self._writeTreeToFile(node.right, file)  
    
    
    
    #get black height of the tree
    
            
        
    
    
    

    def maximum(self):
        if self.Root.right is None:
            return self.Root
        return self.Root.right.maximum()

    def minimum(self):
        if self.Root.left is None:
            return self.Root
        return self.Root.left.minimum()
    
    
    def Insert (self, value) : 
        if(self.Root is None) : 
            self.Root = Node(value, "BLACK")
            
        else:
            self.RBinsert(Node(value,"RED"))
        
        
        
        
    def RBinsert(self, node) : 
        self.BstInsert(self.Root, node)
        while node and node.parent and node.parent.color == "RED" : 
            if node.parent.parent and node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u and u.color == "RED": # IF MY PARENT RED AND UNCLE IS RED ONLY RECOLOR PARENT AND UNCLE AND GRANDPARENT
                    u.color = "BLACK"
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                    
                else : 
                    if node == node.parent.left : 
                        node = node.parent
                        self.RIGHTROTATE(node)
                        
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.LEFTROTATE(node.parent.parent)
                    
                    
            else : 
                    
                    if node.parent.parent is not None : 
                      u = node.parent.parent.right
                      
                    else : 
                          u = None
                    if u and u.color == "RED": # IF MY PARENT RED AND UNCLE IS RED ONLY RECOLOR PARENT AND UNCLE AND GRANDPARENT
                        u.color = "BLACK"
                        node.parent.color = "BLACK"
                        node.parent.parent.color = "RED"
                        node = node.parent.parent
                    else : 
                        if node == node.parent.right : 
                            node = node.parent
                            self.LEFTROTATE(node)
                            
                            
                        node.parent.color = "BLACK"
                        if node.parent.parent :
                            node.parent.parent.color = "RED"
                            self.RIGHTROTATE(node.parent.parent) 
        self.Root.color = "BLACK"
        
        
        
        
        
    def RIGHTROTATE (self, x):
       y = x.left
       x.left = y.right
       if y.right != None:
           y.right.parent = x

       y.parent = x.parent
       if x.parent == None:
           self.Root = y
       elif x == x.parent.right:
           x.parent.right = y
       else:
           x.parent.left = y
       y.right = x
       x.parent = y
       
       
    def LEFTROTATE(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
            
            
        y.parent = x.parent
        if x.parent == None:
            self.Root = y
        
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
        
        
    def BstInsert (self,Root,node) : 
        y = None
        x = self.Root
        
        while x is not None:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
                
        node.parent = y
        if y is None:
            self.Root = node
            
        else : 
            if node.value < y.value:
                y.left = node
            else : 
                y.right = node
                
                
                
    def Delete (self, value): 
            self.RBdelete(value)
        
        
    def RBdelete(self, value):
 
        x = self.bstDelete(self.Root, value)
        while x and x != self.Root and x.color == "BLACK":
            if x.parent.left and x == x.parent.left:
                s = x.parent.right
                if s and s.color == "RED": # sibling is red recolor it and recolor x father and left rotate on x father case 3.1
                    s.color = "BLACK"
                    x.parent.color = "RED"
                    self.LEFTROTATE(x.parent)
                    s = x.parent.right
                    
                if (s.left is None or s.left.color == "BLACK") and (s.right is None and s.right.color == "BLACK"): # sibling has 2 black childs case 3.2
                    s.color = "RED"
                    x = x.parent
                    
                else : 
                    if (s.right is None or s.right.color == "BLACK"): # case 3.3 left child is red replace colors between the sibling and his left child and Right rotate on the sibling
                        s.left.color = "BLACK"
                        s.color = "RED"
                        self.RIGHTROTATE(s)
                        s = x.parent.right
                        
                    #case 3.4
                    #s.color = x.parent.right.color  #####
                    x.parent.color = "BLACK"
                    s.right.color = "BLACK"
                    self.LEFTROTATE(x.parent)
                    x = self.Root
                    
            #mirror        
            else :
                
                if x.parent.right and x == x.parent.right:
                    s = x.parent.left
                    if s and s.color == "RED": # sibling is red recolor it and recolor x father and left rotate on x father case 3.1
                        s.color = "BLACK"
                        x.parent.color = "RED"
                        self.RIGHTROTATE(x.parent)
                        s = x.parent.left
                        
                    if (s.left is None or s.left.color == "BLACK") and (s.right is None and s.right.color == "BLACK"): # sibling has 2 black childs case 3.2
                        s.color = "RED"
                        x = x.parent
                        
                    else : 
                        if (s.left is None or s.left.color == "BLACK"): # case 3.3 left child is red replace colors between the sibling and his left child and Right rotate on the sibling
                            s.right.color = "BLACK"
                            s.color = "RED"
                            self.LEFTROTATE(s)
                            s = x.parent.left
                            
                        #case 3.4
                        #s.color = x.parent.left.color  #####
                        x.parent.color = "BLACK"
                        s.left.color = "BLACK"
                        self.RIGHTROTATE(x.parent)
                        x = self.Root
                    
            x.color = "BLACK"
        
                    
                    
        
                    
        
    
        
        
    def bstDelete(self, node, value): 
        
        if node is None:
            return node

        if value < node.value:
            node.left = self.bstDelete(node.left, value)
        elif value > node.value:
            node.right = self.bstDelete(node.right, value)
        else:
            # Node to be deleted found

            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                if temp:
                    temp.parent = node.parent
                return temp
            elif node.right is None:
                temp = node.left
                if temp:
                    temp.parent = node.parent
                return temp

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.Root.successor(node)

            # Copy the inorder successor's content to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self.bstDelete(node.right, temp.value)

        return node
    
    
    
    def returnColor (self,node): 
        if node and node.color == "RED":
            return "RED"
        
        return "BLACK"
    
    
    def joinRightRB (self,tl,k,tr) :
       if self.returnColor(tl) == "BLACK" and (self.Root.blackHeight2(tl) == self.Root.blackHeight2(tr)):
           node = Node(k,"RED")
           node.left = tl
           node.right = tr
           return node
       
       T = Node(tl.value, tl.color)
       T.left = tl.left
       T.right = self.joinRightRB(tl.right,k ,tr)
       
       if self.returnColor(tl) == "BLACK" and self.returnColor(T.right) == "RED" and self.returnColor(T.right.right) == "RED" : 
           T.right.right.color = "BLACK"
           self.LEFTROTATE(T)
           return T.parent
       
       return T
   
    
    def joinLeftRB(self, tl, k, tr):
        if self.returnColor(tr) == "BLACK" and (self.Root.blackHeight2(tl) == self.Root.blackHeight2(tr)):
            node = Node(k, "RED")
            node.left = tl
            node.right = tr
            return node
    
        T = Node(tr.value, tr.color)
        T.right = tr.right
        T.left = self.joinLeftRB(tl, k, tr.left)
        
    
        if self.returnColor(tr) == "BLACK" and self.returnColor(T.left) == "RED" and self.returnColor(T.left.left) == "RED":
            T.left.left.color = "BLACK"
            self.RIGHTROTATE(T)
            return T.parent
    
        return T
      

    def join (self,tl,k,tr) :
        if self.Root.blackHeight2(tl) > self.Root.blackHeight2(tr): 
            T = self.joinRightRB(tl,k,tr)
            if self.returnColor(T) == "RED" and self.returnColor(T.right) == "RED":
                T.color = "BLACK"
            return T
        
        if self.Root.blackHeight2(tl) < self.Root.blackHeight2(tr) : 
            T = self.joinLeftRB(tl, k, tr)
            if self.returnColor(T) == "RED" and self.returnColor(T.left) == "RED": 
                T.color = "BLACK"
                
            return T
        
       
        if self.returnColor(tl) == "BLACK" and self.returnColor(tr) == "BLACK":
            node = Node(k,"RED")
            node.left = tl
            node.right = tr
            
            return node
        
        node = Node(k,"BLACK")
        node.left = tl
        node.right = tr
        return node
    
    def updateSonFather (self, node) : 
        if node.left:
            node.left.parent = node
            
        if node.right:
            node.right.parent = node
    
    
    
    def split (self,t,k):
        if t == None : 
            return None,False,None
        
        if t.value == k : 
            return t.left, True , t.right
        
        if t.value > k : 
            l , b , r = self.split(t.left, k)
            node = self.join(r, t.value, t.right)
            self.updateSonFather(node)
            return l,b,node
        
        l,b,r = self.split(t.right,k)
        node = self.join(t.left,t.value,l)
        self.updateSonFather(node)
        return node, b , r
        
    
    def unionTrees (self, t1,t2) :
        if t1 == None :
            return t2
        
        if t2 == None : 
            return t1
        
        l , b , r = self.split(t1,t2.value)
        tl = self.unionTrees(l, t2.left)
        tr = self.unionTrees(r, t2.right)
        
        
        
        node = self.join(tl, t2.value, tr)
        self.updateSonFather(node)
        return node
    
    
    def DeleteMinimum(self,root,value) : 
        if root.value == value:
            if root.parent:
                node = Node(root.parent.value,root.parent.color)
                if root.parent.parent:
                    node.parent = root.parent.parent
            else : 
                return None
            
            if root.right:
                root.right.color = root.color
                root.right.parent = node
                node.right = root.right
                
            return node
                
        if root.value > value : 
            return self.DeleteMinimum(root.left,value)
        
        return self.DeleteMinimum(root.right,value)
    
    
    def union(self,t1,t2):
        if t1.blackHeight2(t1) < t2.blackHeight2(t2):
            t = self.unionTrees(t1,t2)
        
        else :
            t = self.unionTrees(t2,t1)
            
        t.color = "BLACK"
        return t
    
    
    def IntersectionTrees(self, t1,t2):
        if t1 is None:
            return None
        
        if t2 is None:
            return None
        
        l , b , r = self.split(t1,t2.value)
        tl = self.IntersectionTrees(l, t2.left)
        tr = self.IntersectionTrees(r, t2.right)
        
        if b == False:
            if tr is None and tl is None: 
                return None
            
            if tr is None : 
                return tl
            
            if tl is None:
                return tr
            
            t = Tree(tr)
            min1 = tr.minimum(tr)
            value = min1.value
            t.Root = self.DeleteMinimum(t.Root,value)
            node = self.join(tl,value,t.Root)
            self.updateSonFather(node)
            return node
        node = self.join(tl,t2.value,tr)
        self.updateSonFather(node)
        return node
    
    
    def DifferenceTrees(self,t1,t2) : 
        if t1 is None:
            return None
        
        if t2 is None:
            return t1
        
        l , b , r = self.split(t1,t2.value)
        tl = self.DifferenceTrees(l, t2.left)
        tr = self.DifferenceTrees(r, t2.right)
        
        if b == True:
            if tr is None and tl is None: 
                return None
            
            if tr is None : 
                return tl
            
            if tl is None:
                return tr
            
            t = Tree(tr)
            min1 = tr.minimum(tr)
            value = min1.value
            t.Root = self.DeleteMinimum(t.Root,value)
            node = self.join(tl,value,t.Root)
            self.updateSonFather(node)
            return node
        
        
        node = self.join(tl,t2.value,tr)
        self.updateSonFather(node)
        return node
            
            
    
    
    def Intersection (self, t1,t2):
       if t1.blackHeight2(t1) < t2.blackHeight2():
           t = self.IntersectionTrees(t1,t2)
           
       else:
           t = self.IntersectionTrees(t2,t1)
            
       if t:
            t.color = "BLACK"
       return t
    
    
    def Difference (self,t1,t2):
        if t1.blackHeight2(t1) < t2.blackHeight2():
           t = self.DifferenceTrees(t1,t2)
           
        else : 
            t = self.DifferenceTrees(t2,t1)
        if t:
            t.color = "BLACK"
        return t
        
        
        
       
   


class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node('{self.value}', '{self.color}')"
    

    
    def minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    # find the node with the maximum key
    def maximum(self, node):
        while node.right != None:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not None,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y
    
    
    def blackHeight (self):
        count = 0
        
        if self is None :
            return 0
        
        while self is not None:
            if self.color == "BLACK":
                count = count + 1
                
            self = self.right
            
            
    def blackHeight2 (self,node):
         count = 0
         
         if node is None :
             return count
         
         while node is not None:
             if node.color == "BLACK":
                 count = count + 1
                 
             node = node.right
             
         return count
     
        
     

def read_groups(filename):
    
    with open(filename, 'r') as file:
        groups = []
        current_group = []
        for line in file:
            numbers = line.split(',')
            numbers = [float(num.strip()) for num in numbers if num.strip()]
            current_group.extend(numbers)
            if not line.endswith(',') and '\n' in line:
                groups.append(current_group)
                break
        return groups

def write_to_file(self, file):
    
    if self.Root is None:
        return
    stack = []
    current = self.Root
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            file.write(str(current.value) + '\n')
            if current.right and current.right.value < current.value:
                break  # Stop writing if the next value is less than the current value
            current = current.right
        else:
            break



def getFile():

    start_time = time.time()
    # Initialize an empty tree
    tree = None
    # Read each line from the input file
    with open("data.txt", "r") as file:
        for line in file:
            # Parse numbers from the line and create a new tree
            numbers = [float(num.strip()) for num in line.split(",") if num.strip()]
            new_tree = Tree()
            new_tree.addGroup(numbers)

            # Union the new tree with the existing tree
            if tree is None:
                tree = new_tree
            else:
                tree.Root = tree.union(tree.Root, new_tree.Root)

                
    end_time = time.time()  # End measuring total time
    total_time = end_time - start_time
    
    
    

    print(f"Total time for all unions: {total_time:.6f} seconds")
    # Write the resulting tree to the output file
    if tree:
        with open("output.txt", "w") as file:
            tree.writeToFile("output.txt")
            
           

getFile()



        
    
    
    
    


t = Tree()
t.Insert(5)
t.Insert(3)
t.Insert(6)
t.Insert(7)


#print(t.Root)







t2 = Tree()
t2.Insert(50)
t2.Insert(90)
t2.Insert(20)
t2.Insert(19)
t2.Insert(40)
t2.Insert(60)






#tt5 = Tree(tt2.union(t2.Root,t.Root))
#print(tt5)

print("_______________________________________")
#print(t2)
#t3 = Tree(t.Difference(t.Root,t2.Root))
print("_______________________________________")
#print(t3)