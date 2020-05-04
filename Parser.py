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
		if self.currentTokenPosition < len(self.tokenValues):
			self.__stmt__(level + 1)
			self.__stmt_list__(level + 1)
		self.__print_with_indent__('</stmt_list>', level)

	def __stmt__(self, level: int):
		self.__print_with_indent__('<stmt>', level)
		# If the next token is an id
		if self.__match__('id'):
			self.__print_with_indent__('<id>', level)
			self.__print_with_indent__(self.tokenValues[self.currentTokenPosition], level + 1)
			self.__print_with_indent__('</id>', level)
		
		self.currentTokenPosition += 1

		self.__print_with_indent__('</stmt>', level)

	def expr(self):
		pass

	def term(self):
		#if factor then:
		#	factor()
		#   factor_tail()
		#else:
		#	returnpass
		pass

	def term_tail(self):
		#if nothing:
		#	return
		#else:
		#	mult_op()
		#	term()
		#	term_tail()
		pass

	def factor(self):
		pass

	def fact_tail(self):
		pass

	def add_op(self):
		pass

	def mult_op(self):
		pass

	# Returns true if the next value matches the value provided
	def __match__(self, value):
		# If we are about to look ahead into out of bounds for the array, error out
		try:
			return self.tokens[self.currentTokenPosition + 1] == value
		except:
			return False


	def __print_with_indent__(self, value, level: int):
		print(level * '\t' + value)
