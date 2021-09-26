from collections import  defaultdict

class PhoneBook:
    def __init__(self):
        self.items = defaultdict(list)
    
    def is_empty(self):
        return not self.items
    
    def add_name(self, name):
        self.items[name]
    
    def add_number(self, name, number):
        self.items[name].append(number)

    def remove_name(self, name):
        self.items.pop(name)
    
    def delete_all(self):
        self.items.clear()
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return f"{self.items}"
    
    def __repr__(self):
        return f"{self.items}"
    

if __name__ == '__main__':
    ph = PhoneBook()
    print(ph)
    print(ph.is_empty())
    ph.add_name("Makiki")
    print(ph)
    ph.add_number("Makiki","0543789652")
    ph.add_number("Makiki","0543789689")
    ph.add_number("Rakiki","0543789652")   
    print(ph)
    print(ph.is_empty())
    print(ph.size())
    print(ph.remove_name("Rakiki"))
    print(ph.delete_all())
    print(ph)
