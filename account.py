class account:
    def check_p(self, passw):
        if len(passw) > 8:
            return True
        else:
            return False

if __name__ == '__main__':
    accVer = account()
    print ('The pass length is ' + str(accVer.check_p('adasdqwea')))