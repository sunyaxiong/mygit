class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)

class ChildB(Base):
    def __init__(self):
        print "this in B "
        super(ChildB, self).__init__()
print "child A :"
ChildA() 
print "child B :"
ChildB()