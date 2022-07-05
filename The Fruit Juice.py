class Jar():
    def __init__(self):
        self.components = {}
    
    def add (self, amount, kind):
        if kind in self.components:
            self.components[kind] += amount
        else:
            self.components[kind] = amount
    
    def pour_out (self, amount):
        self.components = {x: y - y*(amount / self.get_total_amount()) for x, y in self.components.items()}
    
    def get_total_amount(self):
        return sum(self.components.values())
    
    def get_concentration(self, kind):
        if self.components.get(kind):
            return self.components.get(kind) / self.get_total_amount()
        return 0
    