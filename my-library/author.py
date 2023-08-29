class Author:
    def __init__(self, _first_name, _last_name):
        self._first_name = _first_name
        self._last_name = _last_name
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
    
    def set_first_name(self,_first_name):
        self._first_name = _first_name
    
    def set_last_name(self, _last_name):
        self._last_name = _last_name
    
    def display_author(self):
        print(f"Author:\nFirst Name: {self.get_first_name()}\nLast Name: {self.get_last_name()}")

