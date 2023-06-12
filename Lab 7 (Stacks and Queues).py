delim_openers = '{([<'
delim_closers = '})]>'

def check_delimiters(expr):
    """Returns True if and only if `expr` contains only correctly matched delimiters, else returns False."""
    stack=Stack()
    for char in expr:
        if(char=='('):
            stack.push(')')
        elif(char=='['):
            stack.push(']')
        elif(char=='{'):
            stack.push('}')
        elif(char=='<'):
            stack.push('>')
        elif(char in delim_closers):
            if(not stack):
                return False
            elif(char!=stack.pop()):
                return False
    if not stack:
        return True
    else:
        return False
        
     
 # you may find the following precedence dictionary useful
delim_openers = '{([<'
delim_closers = '})]>'
prec = {'*': 2, '/': 2,
        '+': 1, '-': 1}

def infix_to_postfix(expr):
    """Returns the postfix form of the infix expression found in `expr`"""
    ops = Stack()
    postfix = []
    toks = expr.split()
    for char in toks:
        if(char.isdigit()):
            postfix.append(char)
        elif(char=='('):
            ops.push(')')
        elif(char=='['):
            ops.push(']')
        elif(char=='<'):
            ops.push('>')    
        elif(char=='{'):
            ops.push('}')
        elif(char in delim_closers):
            while(ops and ops.peek()!=char):
                postfix.append(ops.pop())
            if( ops and ops.peek()!=char):
                return "invalid expression"
            else:
                ops.pop()
        else:
            if(ops and ops.peek() not in delim_closers):
                while(ops and prec.get(char)<=prec.get(ops.peek())):
                    postfix.append(ops.pop())
            ops.push(char)
    while(ops):
        postfix.append(ops.pop())
    return ' '.join(postfix)
    
    
  

class Queue:
    def __init__(self, limit=10):
        self.data = [None] * limit
        self.head = -1
        self.tail = -1

    def enqueue(self, val):
        if self.head - self.tail == 1:
            raise NotImplementedError
        if len(self.data) - 1 == self.tail and self.head == 0:
            raise NotImplementedError
        if self.head == -1 and self.tail == -1:
            self.data[0] = val
            self.head = 0
            self.tail = 0
        else:
            if len(self.data) - 1 == self.tail and self.head != 0:
                self.tail = -1
            self.data[self.tail + 1] = val
            self.tail = self.tail + 1
        
    def dequeue(self):
        if self.head == self.tail:
            temp = self.head
            self.head = -1
            self.tail = -1
            return self.data[temp]
        if self.head == -1 and self.tail == -1:
            raise NotImplementedError
        if self.head != len(self.data):
            result = self.data[self.head]
            self.data[self.head] = None
            self.head = self.head + 1
        else:
            self.head = 0
            result = self.data[self.head]
            self.data[self.head] = None
            self.head = self.head + 1
        return result 
    
    def resize(self, newsize):
        assert(len(self.data) < newsize)
        newdata = [None] * newsize
        head = self.head
        current = self.data[head]
        countValue = 0
        while current != None:
            newdata[countValue] = current
            countValue += 1
            if countValue != 0 and head == self.tail:
                break
            if head != len(self.data) - 1:
                head = head + 1
                current = self.data[head]
            else:
                head = 0
                current = self.data[head]
        self.data = newdata
        self.head = 0
        self.tail = countValue - 1
        
    def empty(self):
        if self.head == -1 and self.tail == -1:
            return True
        else:
            return False
    
    def __bool__(self):
        return not self.empty()
    
    def __str__(self):
        if not(self):
            return ''
        return ', '.join(str(x) for x in self)
    
    def __repr__(self):
        return str(self)
    
    def __iter__(self):
        head = self.head
        current = self.data[head]
        countValue = 0
        while current != None:
            yield current
            countValue += 1
            if countValue != 0 and head == self.tail:
                break
            if head != len(self.data) - 1:
                head = head + 1
                current = self.data[head]
            else:
                head = 0
                current = self.data[head]
