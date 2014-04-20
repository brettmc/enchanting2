
class Environment(object):
    "The environment keeps track of state, variables, sensor readings, etc."
    
    def __init__(self):
        self.stack = [] # the stack is used to know where to go when there is no sibling-level code to run
        
        # declare things for variables here.  Name map? value map?
        
    def am_on_top_of_stack(self, statement):
        "Is a (block-level) statement on top of the stack?"
        return (len(self.stack) > 0) and (self.stack[-1] == statement)
    
    def push_on_stack(self, statement):
        "Record that a block-level statement is on top of the stack"
        self.stack.append(statement)
        
    def pop_off_stack(self, statement):
        assert self.am_on_top_of_stack(statement)
        self.stack.pop()
        
    def run(self, statement):
        "Runs the specified code in the current environment"
        
        # Take the current statement
        # Execute it until we run out of statements
        # The stack contains a record of looping statements

        current = statement
        while current != None:
            current.evaluate(self)
            next = current.next_statement(self)
            if next == None and len(self.stack) > 0:
                next = self.stack[-1]
            current = next
        