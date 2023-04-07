class CountingClicker:
    """Classes as well as functions may have a docstring"""
    def __init__(self, count:int = 0):
        """Class constructor, self  arg by default is the instance"""
        self.count = count

    def __repr__(self) -> str:
        """DUNDER methods (Double-UNDERscores), always are something meaningful, __repr__ return a string representation of the class"""
        return f"CountingClicker(count={self.count})"

    def click(self, num_times:int = 1)->None:
        """Click in the counter for n times, 1 by default"""
        self.count+=num_times
        return

    def read(self)->int:
        """Return the number of clicks"""
        return self.count

    def reset(self)->None:
        """Resets the clicks counter"""
        self.count = 0
        return

clicker = CountingClicker()
clicker2 = CountingClicker(2)
assert clicker.read() == 0, "Clicker default start 0"
assert clicker2.read() == 2, "Clicker started with 2"
clicker.click()
clicker2.click(2)
assert clicker.read() == 1, "Clicker clicked one time"
assert clicker2.read() == 4, "Clicker clicked 2 times, started with 2"
clicker.reset()
clicker2.reset()
assert clicker.read() == 0, "Clicker reset"
assert clicker2.read() == 0, "Clicker reset"

#Inheritance
class NoResetClicker(CountingClicker):
    """Same as CountingClicker but with no reset method"""
    def reset(self) -> None:
        """Does Nothing :)"""
        pass

clicker3 = NoResetClicker()
assert clicker3.read() == 0, "Clicker default start 0"
clicker3.click()
assert clicker3.read() == 1, "Clicker clicked one time"
clicker3.reset()
assert clicker3.read() == 1, "Clicker reset not working"
