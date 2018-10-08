import unittest


class DoubleLinkedList:
    class Item(object):
        def __init__(self, elem, prev_item, next_item):
            self.elem = elem
            self.prev_item = prev_item
            self.next_item = next_item


    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0





    

    def unshift(self, elem):
        if self.count == 0:
            self.first = self.Item(elem, None, None)
            self.last = self.first
        elif self.count > 0:
            x = self.Item(elem, None, self.first)
            self.first.prev_item = x
            self.first = x
        self.current = self.first
        self.count += 1


    def shift(self):
        if self.count == 0:
            return None
        if self.count == 1:
            self.first = None
            self.last = None
        elif self.count > 1:
            self.first = self.first.next_item
            self.first.prev_item = None
        self.current = self.first
        self.count -= 1



    def pop(self):
        if self.count==0:
            return None
        if self.count == 1:
            self.first = None
            self.last = None
        elif self.count > 1:
            self.last = self.last.prev_item
            self.last.next_item = None
        self.count -= 1


    def push(self, elem):
        if self.count == 0:
            self.first = self.Item(elem, None, None)
            self.last = self.first
        else:
            self.last.next_item = self.Item(elem, self.last, None)
            self.last = self.last.next_item
        self.count += 1

    def first_elem(self):
        if self.first == None:
            return None
        else:
            return self.first.elem
    def last_elem(self):
        if self.last == None:
            return None
        else:
            return self.last.elem



    def delete(self, elem):
        if self.count == 0:
            return None
        current_elem = self.first
        previous_elem = None
        while current_elem is not None:
            if current_elem.elem == elem:
                self.count -= 1
                if previous_elem is not None:
                    previous_elem.next_item = current_elem.next_item
                else:
                    self.first = current_elem.next_item


            previous_elem = current_elem
            current_elem = current_elem.next_item

    def contains(self, elem):
        if self.count == 0:
            return None
        current_elem = self.first
        previous_elem = None

        while current_elem is not None:
            if current_elem.elem == elem:
                return True

            previous_elem = current_elem
            current_elem = current_elem.next_item
        return False

    def len(self):
        return self.count

    def __str__(self):
        current = self.first
        to_print = []
        while current:
            to_print.append(current.elem)
            current = current.next_item
        return str(to_print)

