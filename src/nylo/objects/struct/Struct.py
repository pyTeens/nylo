from nylo.objects.NyObject import NyObject
from nylo.objects.struct.StructEl import Set, TypeDef
from nylo.objects.values.Keyword import Keyword
from copy import deepcopy

class Struct(NyObject):
    
    def __init__(self, elements): *self.value, self.toreturn = elements
    
    def __str__(self): return '(%s -> %s)' % (', '.join(map(str, self.value)), str(self.toreturn))

    def evaluate(self, stack): 
        return self
    
    def calculate(self, stack):
        stack.append(self)
        if not self.toreturn is False: 
            value = self.toreturn.evaluate(stack)
        else: value = self
        stack.pop()
        return value
        
    def update(self, other, stack):
        for element in other.value:
            if isinstance(element, Set):
                # example(locals: globals)
                if isinstance(element.by, Keyword) or element.to in stack[-1]:
                    element.to = element.to.evaluate(stack)
                    self.value.append(element)
                elif isinstance(element.to, Keyword) or element.by in self:
                    stack.append(self)
                    stack[-2].value.append(Set(element.to,
                            element.by.evaluate(stack)))
                    stack.pop()
                else: raise TypeError(self, other)
        
    def getitem(self, value, stack):
        stack.append(self)
        out = None
        for element in self.value:
            if isinstance(element, Set) and element.by == value:
                out = element.to.evaluate(stack)
        stack.pop()
        if not out: raise NameError(value)
        return out
        
    def __contains__(self, value):
        for element in self.value:
            if isinstance(element, Set) and element.by == value: 
                return True
        return False

class Call(NyObject):
    
    def __init__(self, kw, struct): 
        self.kw, self.struct, self.value = kw, struct, (kw, struct)

    def __str__(self): return '%s%s' % (self.kw, self.struct)

    def evaluate(self, stack):
        self.caller = self.struct
        self.called = deepcopy(stack[self.kw])
        self.called.update(self.caller, stack)
        if self.caller.toreturn:
            self.called.toreturn = self.caller.toreturn
        return self.called.calculate(stack)