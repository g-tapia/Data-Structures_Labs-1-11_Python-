class BSTree(BSTree):
    def count_less_than(self, x):
        def count_util(node, x):
            if not node:
                return 0
            if(node.val<x):
                return (1 + count_util(node.left, x) + count_util(node.right, x))
            else:
                return(count_util(node.left, x))
        return count_util(self.root, x)
    def successor(self, x):
        def successor_util(node, x):
            if not node:
                return 1000000000
            if(node.val>x):
                return min(node.val, successor_util(node.left,x))
            else:
                return successor_util(node.right,x)
        ans = successor_util(self.root,x)
        if(ans==1000000000):
            return None
        else:
            return ans;
        
    def descendants(self, x):
        ans = []
        def inorder(node, y):
            if not node:
                return
            inorder(node.left,y)
            if node.val != y:
                ans.append(node.val)
            inorder(node.right,y)
  
        def descendants_util(node, x):
            if not node:
                return
            if node.val==x:
                inorder(node, node.val)
            elif node.val<x:
                descendants_util(node.right,x)
            else:
                descendants_util(node.left,x)
  
        descendants_util(self.root,x)
        return ans



class BSTree:
    class Node:
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            
    def __init__(self):
        self.size = 0
        self.root = None
        
    def __getitem__(self, key):
        def get_rec(node):
            if not node:
                raise KeyError
            elif key < node.key:
                return get_rec(node.left)
            elif key > node.key:
                return get_rec(node.right)
            elif key == node.key:
                return node.val
            else:
                raise KeyError
        return get_rec(self.root)
    
    def __setitem__(self, key, val):
        def set_rec(node):
            if not node:
                return BSTree.Node(key, val)
            elif key == node.key:
                node.val = val
                return node
            elif key < node.key:
                node.left = set_rec(node.left)
                return node
            elif key > node.key:
                node.right = set_rec(node.right)
                return node

        self.root = set_rec(self.root)
        self.size += 1
                       
    def __delitem__(self, key):
        def delitem_rec(node):
            if node.key < key:
                node.right = delitem_rec(node.right)
                return node
            elif node.key > key:
                node.left = delitem_rec(node.left)
                return node
            elif node.key == key:
                if not node.left and not node.right:
                    return None
                elif node.left and not node.right:
                    return node.left
                elif not node.left and node.right:
                    return node.right
                else:
                    t = node.left
                    if not t.right:
                        node.left = t.left
                        node.val = t.val
                        node.key = t.key
                    else:
                        n = t
                        while n.right.right:
                            n = n.right
                        t = n.right
                        n.right = t.left
                        node.val = t.val
                        node.key = t.key
                    return node
            else:
                raise KeyError

        self.root = delitem_rec(self.root)
        self.size -= 1
      
        
    def __contains__(self, key):
        def find(t):
            if not t:
                return False
            elif t.key == key:
                return True
            elif t.key > key:
                return find(t.left)
            elif t.key < key:
                return find(t.right)

        return find(self.root)        
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        def iter_rec(node):
            if node:
                yield from iter_rec(node.left)
                yield node.key
                yield from iter_rec(node.right)
        return iter_rec(self.root)

    def keys(self):
        def iter_rec(node):
            if node:
                yield from iter_rec(node.left)
                yield node.key
                yield from iter_rec(node.right)
        return iter_rec(self.root)
    
    def values(self):
        def iter_rec(node):
            if node:
                yield from iter_rec(node.left)
                yield node.val
                yield from iter_rec(node.right)
        return iter_rec(self.root)  
    def items(self):
        def iter_rec(node):
            if node:
                yield from iter_rec(node.left)
                yield (node.key, node.val)
                yield from iter_rec(node.right)
        return iter_rec(self.root)   
        
    def pprint(self, width=64):
        """Attempts to pretty-print this tree's contents."""
        height = self.height()
        nodes  = [(self.root, 0)]
        prev_level = 0
        repr_str = ''
        while nodes:
            n,level = nodes.pop(0)
            if prev_level != level:
                prev_level = level
                repr_str += '\n'
            if not n:
                if level < height-1:
                    nodes.extend([(None, level+1), (None, level+1)])
                repr_str += '{val:^{width}}'.format(val='-', width=width//2**level)
            elif n:
                if n.left or level < height-1:
                    nodes.append((n.left, level+1))
                if n.right or level < height-1:
                    nodes.append((n.right, level+1))
                repr_str += '{val:^{width}}'.format(val=n.key, width=width//2**level)
        print(repr_str)
    
    def height(self):
        """Returns the height of the longest branch of the tree."""
        def height_rec(t):
            if not t:
                return 0
            else:
                return max(1+height_rec(t.left), 1+height_rec(t.right))
        return height_rec(self.root)
