from xml.etree.cElementTree import Element

from variables import Variables
from block import Block
import util

class Script:
	"Represents a sequence of instructions"
	
	def __init__(self, target):
	
		self.target = target	# this is a sprite or stage that we modify
	
		self.x = 0
		self.y = 0

		self.blocks = []
		
		self.code_pos = None
	
	def deserialize(self, elem):
		"Loads this class from an element tree representation"
		assert(elem.tag == "script")

		# attributes
		self.x = int(elem.get("x"))
		self.y = int(elem.get("y"))

		# our children are a sequence of blocks or custom blocks
		for block in elem:
			b = Block()
			b.deserialize(block)
			self.blocks.append(b)

	def serialize(self):
		"Return an elementtree representing this object"
		
		# We have sprite objects and watcher nodes; make a tree of nodes
		script = Element("script", 
						 x=util.number_to_string(self.x), 
						 y=util.number_to_string(self.y))
		
		for block in self.blocks:
			script.append(block.serialize())
						
		return script	

	def step(self):
		"Execute a line of code; raises StopIteration when there is no more code"
		self.block[self.code_index].evaluate(self.target)
		
		if not self.code_pos:
			self.code_pos = self.blocks.__iter__()
		current_block = self.code_pos.next()
		current_block.evaluate()
		
	def run(self):
		"Runs the code until it is done (if it ever finishes)"
		try:
			while True:
				self.step()
		except StopIteration:
			pass
				
		