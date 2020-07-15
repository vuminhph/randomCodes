class MinStack:
	def __init__(self):
		self._stack = []
    
	def push(self, val):
		self._stack.append(val)
      
	def pop(self):
		return self._stack.pop()
    
	def peek(self):
		return self._stack[-1]
  
	def min(self):
		return min(self._stack)


