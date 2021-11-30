import random
class RottenTest(object):
    
    assert_choice = [True, False]

    def testDEF(self):
        self.badHelper()
        assert(True)
    
    def badHelper(self):
        if False:
            self.secondHelper()
    
    def secondHelper(self):
        if True:
            self.thirdHelper()

    def thirdHelper(self):
        assert (random.choice(self.assert_choice))

Test = RottenTest()
Test.testDEF()