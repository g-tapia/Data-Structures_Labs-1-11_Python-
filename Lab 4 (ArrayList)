class ArrayList:
    def __init__(self):
        self.data = ConstrainedList() # don't change this line!

    
    ### subscript-based access ###
    
    def _normalize_idx(self, idx):
        nidx = idx
        if nidx < 0:
            nidx += len(self.data)
            if nidx < 0:
                nidx = 0
        return nidx
    
    def __getitem__(self, idx):
        """Implements `x = self[idx]`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        return self.data[nidx]

    def __setitem__(self, idx, value):
        """Implements `self[idx] = x`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        self.data[nidx] = value

    def __delitem__(self, idx):
        """Implements `del self[idx]`"""
        assert(isinstance(idx, int))
        nidx = self._normalize_idx(idx)
        if nidx >= len(self.data):
            raise IndexError
        for i in range(nidx+1, len(self.data)):
            self.data[i-1] = self.data[i]
        del self.data[len(self.data)-1]
    

    ### stringification ###
    
    def __str__(self):
        """Implements `str(self)`. Returns '[]' if the list is empty, else
        returns `str(x)` for all values `x` in this list, separated by commas
        and enclosed by square brackets. E.g., for a list containing values
        1, 2 and 3, returns '[1, 2, 3]'."""
        if len(self.data) == 0:
            return '[]'
        string=''
        characters= '['
        string = string + characters
        for x in range(0,len(self.data)):
            characters=str(self.data[x])
            if len(self.data) > 1:
                if x <  len(self.data)-1:
                    string = string + characters + ', '
                else:
                    string = string + characters
            else:
                string = string + characters
        
        characters = ']'
        string = string +characters
        return string
        
    def __repr__(self):
        """Supports REPL inspection. (Same behavior as `str`.)"""
        return str(self)   


    ### single-element manipulation ###
    
    def append(self, value):
        """Appends value to the end of this list."""
        if self.data:
            self.data.append(None)
            self.data[len(self.data)-1]=value
        else:
            self.data.append(None)
            self.data[0]=value
    
    def insert(self, idx, value):
        """Inserts value at position idx, shifting the original elements down the
        list, as needed. Note that inserting a value at len(self) --- equivalent
        to appending the value --- is permitted. Raises IndexError if idx is invalid."""
        if(idx > len(self.data)):
            raise IndexError
        if idx < 0 :
            raise IndexError
        elif(idx==len(self.data)):
            self.append(value)
        else:
            self.data.append(None)
            for i in range(len(self.data)-1, idx, -1):
                self.data[i]=self.data[i-1]
                self.data[i-1]=None
            self.__setitem__(idx, value)
    
    def pop(self, idx=-1):
        """Deletes and returns the element at idx (which is the last element,
        by default)."""
        element = self.data[idx]
        self.__delitem__(idx)
        
        return element
    
    def remove(self, value):
        """Removes the first (closest to the front) instance of value from the
        list. Raises a ValueError if value is not found in the list."""
        found=0
        for x in range(0, len(self.data)-1):
            if self.data[x]==value:
                self.__delitem__(x)
                found+=1
                break
        if found == 0:
            raise ValueError()
    

    ### predicates (T/F queries) ###
    
    def __eq__(self, other):
        """Returns True if this ArrayList contains the same elements (in order) as
        other. If other is not an ArrayList, returns False."""
        sameElements = False
        if isinstance(other, ArrayList):
            for i in range(0, len(self.data)-1):
                if self.data[i] ==  other.data[i]:
                    sameElements = True
        else:
            return false
        return sameElements


    def __contains__(self, value):
        """Implements `val in self`. Returns true if value is found in this list."""
        found=False
        for x in range(0, len(self.data)-1):
            if self.data[x]==value:
                found = True
        return found


    ### queries ###
    
    def __len__(self):
        """Implements `len(self)`"""
        counter = 0
        for i in range(0, len(self.data)):
            counter+=1
        return counter
    
    def min(self):
        """Returns the minimum value in this list."""
        minumum = self.data[0]
        for x in range(0, len(self.data)-1):
            if minumum > self.data[x]:
                minumum = self.data[x]
        return minumum
    
    def max(self):
        """Returns the maximum value in this list."""
        maximum = self.data[0]
        for i in range(0, len(self.data)-1):
            if maximum < self.data[i]:
                maximum = self.data[i]
        return maximum
    
    def index(self, value, i=0, j=None):
        """Returns the index of the first instance of value encountered in
        this list between index i (inclusive) and j (exclusive). If j is not
        specified, search through the end of the list for value. If value
        is not in the list, raise a ValueError."""
        if j == None:
            j=len(self.data)
        start = self._normalize_idx(i)
        end = self._normalize_idx(j)
        
        for x in range(start, end):
            if self.data[x]==value:
                return x
        raise ValueError ('Value is not in the list')   
        
    def count(self, value):
        """Returns the number of times value appears in this list."""
        count = 0 
        for x in range(0, len(self.data)):
            if self.data[x]==value:
                count +=1
        return count
    
    ### bulk operations ###

    def __add__(self, other):
        """Implements `self + other_array_list`. Returns a new ArrayList
        instance that contains the values in this list followed by those 
        of other."""
        newarray = ArrayList()
    
        for x in range(0, len(self.data)):
            newarray.append(self.data[x])
        for i in range(0, len(other.data)):
            newarray.append(other.data[i])
        return newarray
    
    def clear(self):
        self.data = ConstrainedList() # don't change this!
        
    def copy(self):
        """Returns a new ArrayList instance (with a separate data store), that
        contains the same values as this list."""
        newarray = ArrayList()
        for i in range(0, len(self.data)):
            newarray.append(self.data[i])
        return newarray 

    def extend(self, other):
        """Adds all elements, in order, from other --- an Iterable --- to this list."""
        for x in other:
            self.append(x)
        return self 

            
    ### iteration ###
    
    def __iter__(self):
        """Supports iteration (via `iter(self)`)"""
        for x in range(0, len(self.data)):
            yield self.data[x]
