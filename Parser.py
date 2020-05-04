from typing import List
from Scanner import Scanner
class Parser:

    def __init__(self, a: List):
        self.s = Scanner(a)
        self.tokens = self.s.scan()
        self.tokenValues = self.s.list()
        self.currentTokenPosition = 0


    def parse(self):
        
        print('token list: {0}'.format(self.tokens[:]))
        self.__program__(0)
    
    def __program__(self, level: int):
        self.__print_with_indent__('<program>', level)
        self.__stmt_list__(level + 1)
        self.__print_with_indent__('</program>', level)

    def __stmt_list__(self, level: int):
        self.__print_with_indent__('<stmt_list>', level)
		# If there is still something left to read
        if self.currentTokenPosition != len(self.tokenValues) - 1:
            self.__stmt__(level + 1)
            self.__stmt_list__(level + 1)
        self.__print_with_indent__('</stmt_list>', level)

    def __stmt__(self, level: int):
        self.__print_with_indent__('<stmt>', level)
        # Just so that we don't go into stack overflow
        self.currentTokenPosition += 1
        self.__print_with_indent__('</stmt>', level)

    def __print_with_indent__(self, value, level: int):
        print(level * '\t' + value)