from abc import ABC,abstractmethod
class android(ABC):
  @abstractmethod
  def navbar(self):
    pass
  @abstractmethod
  def statusbar(self):
    pass
class realme(android):
  def navbar(self):
    print('it is a realme nav bar')
  def statusbar(self):
    print('it is a realme status bar')
r1=realme()
r1.navbar()
r1.statusbar()
