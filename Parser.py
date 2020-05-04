from typing import List
from Scanner import Scanner

class Parser:

	def __init__(self, a: List):
		self.s = Scanner(a)
		self.tokens = self.s.scan()
		self.list = self.s.list()

	def program(self):
		pass

	def stmt_list(self):
		pass

	def stmt(self):
		pass

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

       
