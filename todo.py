class Todo:
  def __init__ (self, name):
    self.name = name
    self.items = []
  def add (self, item):
    self.items.append(item)
  def __repr__(self):  # referenced by programmers
    # return f" Todo {self.name}."
    return f"{__class__.__name__} ('{self.name}')"  # same thing - dunder way
  
  def __str__(self): # referenced by users
   return self.name

  def __len__(self):
    return len(self.items)

  def __gt__(self,other):  # gt = greater than
      return len(self.items) > len(other.items)
  def __lt__(self,other):  # lt = greater than
      return len(self.items) < len(other.items)