import os
from time import sleep

class base(object):
    def __init__(self):
        pass
    
    def a(self):
        print('this is base().a()')

    def b(self, name):
        print('this is base().b() print hello:', name)

if __name__ == "__main__":
    base().a()
    base().b('python')
        