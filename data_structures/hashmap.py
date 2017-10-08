# KPCB Engineering Fellows Coding Challenge #
# author: Jason Lin <uscjlin@gmail.com> #

class HashMap:
    """ Hash table which uses strings for key_list. Value can be any object.

    Supported methods:
        # HashMap(size): returns new instance with underlying array of capacity = size
        > hashtable = HashMap(10)

        # set(key, value): stores given key/value pair into the hashtable. 
        > hashtable.set('hello', 'world')
        > ht['hello'] = 30 # alternative syntactic sugar using 
        
        # instead of returning a bool, set(key, value) return 'self' to support method chaining:
        > hashtable.set('a', 1).set('b', 2).set('c', 3)

        # get(key): return the value associated with given key, None if no value is set.
        > hashtable.get('hello')

        # delete(key): delete value associated with given key, return None if key not found.
        > hashtable.delete('hello') # hashtable.get('hello') = None

        # float load(): return a float value representing the load factor
        > hashtable.load() # = size/capacity
    """

    def __init__(self, capacity=997):
        """ Use prime number closest to 1000 as default capacity. 
        
        data = [ [ [key, value], [key, value], [key, value] ] ]
        1st level [] -> hashcode-index mapped cell
        2nd level [] -> array under each mapped bucket for linear chaining (collision resolution)
        3rd level [] -> actual (key, value) pair 
        """
        self.size = 0
        self.capacity = capacity
        self.table = [ [] for _ in range(capacity) ]
        self.key_list = []

    """ Simple metaprogramming support (i.e. set/get with square brackets) """
    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def key_list(self):
        return self.key_list


    def _index_first_level(self, key, _caller_funcptr):
        """ magic wrapper to index into 2nd level bucket of the table by hashcode, 
        which then makes callback to caller function with the corresponding bucket 
        and 3rd level (key, value) pair to operate on.
        """
        loc = self.hash_function(key, self.capacity)
        parent_bucket = self.table[loc]

        item_found = None
        for item in parent_bucket:
            if item[0] == key:
                item_found = item
                break

        return _caller_funcptr(item_found, parent_bucket)

    def hash_function(self, key, size):
        """ Naive hash function by remainder with modulo
        To support arbitrary data objects as key:
        https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
        """
        try: # check whether python knows about 'basestring'
            basestring
        except NameError: # no, it doesn't (it's Python3); use 'str' instead
            basestring=str

        if not isinstance(key, str):
            key = str(key)  # key is custom object
        return sum([ord(c) for c in key]) % size

    def set(self, key, value):
        """ Insert (key, value) pair into underlying table. Updates value if key already exists.
        Non-string key_list will be turned into a string using __str__() before hashing. Value can be of 
        any type. Returns False if insertion fails (i.e. size > capacity) to ensure fixed-size 
        property of hash map. 
        """
        if self.size == self.capacity: 
            return False

        def _caller_funcptr(item_found, parent_bucket):
            if item_found:
                item_found[1] = value
            else:
                parent_bucket.append([key, value])
                self.key_list.append(key)
                self.size += 1

        self._index_first_level(key, _caller_funcptr)
        return True

    def get(self, key):
        """ return the value associated with the given key, or null if no value is set. """
        def _caller_funcptr(item_found, _):
            if item_found:
                return item_found[1]
            else:
                return None

        return self._index_first_level(key, _caller_funcptr)

    def delete(self, key):
        """ delete the value associated with the given key, returning the value on success 
        or null if the key has no value. 
        """
        def _caller_funcptr(item_found, parent_bucket):
            if item_found:
                self.key_list.remove(key)
                parent_bucket.remove(item_found)
                self.size -= 1
                return item_found[1]
            else:
                return None

        return self._index_first_level(key, _caller_funcptr)

    def load(self):
        """ return a the load factor (`(items in hash map)/(size of hash map)`) of the data structure. """
        return float(self.size)/self.capacity

    def clear(self):
        """ clears all entry pairs in the underlying table. """
        self.table = [[] for _ in range(self.capacity)]
        self.key_list = []
        self.size = 0 


if __name__ == "__main__":
    """ run `python hashmap.py` in CLI to execute all class-specific unit tests in 'tests' directory """
    import unittest
    testsuite = unittest.TestLoader().discover('tests', pattern="*hashmap*")
    unittest.TextTestRunner(verbosity=1).run(testsuite)