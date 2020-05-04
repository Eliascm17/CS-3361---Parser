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
		self.program(0)
	
	def program(self, level: int):
		self.print_with_indent('<program>', level)
		self.stmt_list(level + 1)
		self.print_with_indent('</program>', level)

	def stmt_list(self, level: int):
		self.print_with_indent('<stmt_list>', level)
		# If there is still something left to read
		if self.currentTokenPosition < len(self.tokenValues):
			self.stmt(level + 1)
			self.stmt_list(level + 1)
		self.print_with_indent('</stmt_list>', level)

	def stmt(self, level: int):
		self.print_with_indent('<stmt>', level)
		# If the next token is an id
		if self.match('id'):
			self.print_with_indent('<id>', level)
			self.print_with_indent(self.tokenValues[self.currentTokenPosition], level + 1)
			self.print_with_indent('</id>', level)
			# Next one should be an assign
			self.currentTokenPosition += 1
			if self.match('assign'):
				self.print_with_indent('<assign>', level)
				self.print_with_indent(self.tokenValues[self.currentTokenPosition], level + 1)
				self.print_with_indent('</assign>', level)
				self.currentTokenPosition += 1
			else:
				raise Exception()
			self.expr()

		elif self.match('read'):
			self.print_with_indent('<read>', level)
			self.print_with_indent(self.tokenValues[self.currentTokenPosition], level + 1)
			self.print_with_indent('</read>', level)
			self.currentTokenPosition += 1
			if self.match('id'):
				self.print_with_indent('<id>', level)
				self.print_with_indent(self.tokenValues[self.currentTokenPosition], level + 1)
				self.print_with_indent('</id>', level)
				self.currentTokenPosition += 1
			else:
				raise Exception()

		elif self.match('write'):
			self.print_with_indent('<write>', level)
			self.print_with_indent('write', level + 1)
			self.print_with_indent('<write>', level)
			self.expr(level)
		
		else:
			raise Exception()

		self.print_with_indent('</stmt>', level)

	def expr(self, level):
		self.print_with_indent('<expr>', level)
		self.term()
		self.term_tail()
		self.print_with_indent('</expr>', level)

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

	def factor(self, level: int):
		if self.tokens[self.currentTokenPosition] == 'lparen':
			self.print_with_indent('<lparen>', level)
			self.print_with_indent('(', level + 1)
			self.print_with_indent('</lparen>', level)
			self.currentTokenPosition += 1
			self.expr(level + 1)
			if(self.tokens[self.currentTokenPosition] == 'rparen'):
				self.print_with_indent('<rparen>', level)
				self.print_with_indent(')', level + 1)
				self.print_with_indent('</rparen>', level)
				self.currentTokenPosition += 1
			else:
				raise Exception

		elif self.tokens[self.currentTokenPosition] == 'id':
			self.print_with_indent('<id>', level)
			self.print_with_indent(self.tokenValues[self.currentTokenPosition], level + 1)
			self.currentTokenPosition += 1
			self.print_with_indent('</id>', level)

		elif self.tokens[self.currentTokenPosition] == 'number':
			self.print_with_indent('<number>', level)
			self.print_with_indent(self.tokenValues[self.currentTokenPosition], level + 1)
			self.currentTokenPosition += 1
			self.print_with_indent('</number>', level)

	def fact_tail(self):
		pass

	def add_op(self):
		pass

	def mult_op(self):
		pass

	# Returns true if the next value matches the value provided
	def match(self, value):
		# If we are about to look ahead into out of bounds for the array, return false
		try:
			return self.tokens[self.currentTokenPosition] == value
		except:
			return False


	def print_with_indent(self, value, level: int):
		print(level * '\t' + value)
