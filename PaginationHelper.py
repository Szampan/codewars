import math

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page      

    def item_count(self):
        return len(self.collection)
  
    def page_count(self):
        return math.ceil(len(self.collection) / self.items_per_page)
	
    def page_item_count(self, page_index):
        if page_index + 1 > self.page_count(): return -1        
        if page_index + 1 < self.page_count(): return self.items_per_page
        return self.item_count() - self.items_per_page * page_index 

    def page_index(self,item_index):
        if item_index +1 > len(self.collection) or item_index < 0: return -1
        return item_index  // self.items_per_page
