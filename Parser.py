from typing import List
from Scanner import Scanner
class Parser:

    def __init__(self, a: List):
        self.s = Scanner(a)
        self.tokens = self.s.scan()
        self.list = self.s.list()   


    def parse(self):
        
        print('token list: {0}'.format(self.tokens[:]))
        print('<Program>\n\t<stmt_list>\n\t\t<stmt>')
        #put code here...
        print('\t\t</stmt>\n\t\t<stmt_list>\n\t\t</stmt_list>\n\t</stmt_list>\n</Program>')
    
