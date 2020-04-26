import unittest
import account as AccountClass

class Test(unittest.TestCase):
    accInfo = AccountClass.account()

    def test_check_pass(self):
        print ("Checking possible pass\n")
        passwordList = ['asdasdwer', 'asderesdsd', 'aderwqeqq']

        for passwd in passwordList:
            print ("checking pass " + passwd + "\n")
            passInfo = self.accInfo.check_p(passwd)

            self.assertTrue(passInfo)

if __name__ == '__main__':
    unittest.main()