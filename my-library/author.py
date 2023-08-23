class Author:
    def __init__(self, _first_name, _last_name):
        self._first_name = _first_name
        self._last_name = _last_name
    
    def get_first_name():
        return _first_name
    
    def get_last_name():
        return _last_name
    
    def set_first_name(self,_first_name):
        self._first_name = _first_name
    
    def set_last_name(self, _last_name):
        self._last_name = _last_name
    
    def display_author():
        print(f"Author:\nFirst Name: {get_first_name}\nLast Name: {get_last_name}")
