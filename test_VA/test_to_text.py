def test(a):
    return (a)

t = test(1)
print(t)

class Pt(object):

    def __init__(self, test):
        self.text = test
    
    def print_text(self):
        print self.text