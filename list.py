#!/usr/bin/python2

class List:
    def __init__(self, initlist):
        # just pretend that you can't access this variable directly
        # like a private var in Java
        self._list = initlist

    def testsorted(self):
        for i in range(1,len(self._list)):
            if self._list[i] < self._list[i-1]:
                return False
            return True 


class MutableListOne(List):
    def __init__(self, initlist):
        self._list = initlist

    def get(self):
        """ 
        This class is mutable because returning a 
        reference to a mutable object allows it to be changed
        """
        return self._list

class MutableListTwo(List):
    def __init__(self, initlist):
        """
        This class is also mutable because holding on to a reference
        of the list this is initialized to also allows it to be changed
        """
        self._list = initlist

    def get(self):
        # Slicing copies the list
        return self._list[:]

class ImmutableList(List):
    def __init__(self, initlist):
        # Make a copy of the list now
        self._list = initlist[:]

    def get(self):
        # And only ever return a copy
        return self._list[:]

if __name__ == "__main__":
    one=MutableListOne([1,2,3,4,5,6])
    one.get().reverse()
    if one.testsorted():
        print "List One is immutable"
    else:
        print "List One is mutable"

    list2 = [1,2,3,4,5]
    two = MutableListTwo(list2)
    two.get().reverse()
    if two.testsorted():
        print "List Two might be immutable"
    else:
        print "List Two definitely is not mutable"

    list2[0] = -1000
    if two.get()[0] > 0:
        print "And it is"
    else:
        print "But it isn't"

    list3 = [1,2,3,4,5]
    three = ImmutableList(list3)
    list3.reverse()
    if three.testsorted():
        print "List Three might be immutable"
    else:
        print "List Three is mutable"

    three.get().reverse()
    if three.testsorted():
        print "List Three is immutable! :)"
    else:
        print "The author fucked up"
