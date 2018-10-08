import unittest
import DoubleLinkedList



class TestDoubleLinkedList(unittest.TestCase):
    list = None

    def setUp(self):
        self.list = DoubleLinkedList.DoubleLinkedList()


    def test_push(self):
        self.list.push(1)
        self.assertEqual(str(self.list), '[1]')
        self.list.push(2)
        self.assertEqual(str(self.list), '[1, 2]')

    def test_unshift(self):
        self.list.unshift(1)
        self.assertEqual(str(self.list), '[1]')
        self.list.unshift(2)
        self.assertEqual(str(self.list), '[2, 1]')
    def test_pop(self):
        self.assertEqual(self.list.pop(), None)
        self.list.push(1)
        self.list.push(2)
        self.list.pop()
        self.assertEqual(str(self.list), '[1]')
        self.list.pop()
        self.assertEqual(str(self.list), '[]')
    def test_shift(self):
        self.assertEqual(self.list.pop(), None)
        self.list.push(1)
        self.list.push(2)
        self.list.shift()
        self.assertEqual(str(self.list), '[2]')
        self.list.shift()
        self.assertEqual(str(self.list), '[]')

    def test_first_elem(self):
        self.assertEqual(self.list.first_elem(), None)
        self.list.push(1)
        self.assertEqual(self.list.first_elem(), 1)
        self.list.unshift(2)
        self.assertEqual(self.list.first_elem(), 2)

    def test_last_elem(self):
        self.assertEqual(self.list.last_elem(), None)
        self.list.push(1)
        self.assertEqual(self.list.last_elem(), 1)
        self.list.push(2)
        self.assertEqual(self.list.last_elem(), 2)
    def test_len(self):
        self.assertEqual(self.list.len(), 0)
        self.list.push(221)
        self.assertEqual(self.list.len(), 1)
        self.list.unshift(12)
        self.assertEqual(self.list.len(), 2)
        self.list.pop()
        self.assertEqual(self.list.len(), 1)
        self.list.pop()
        self.list.pop()
        self.list.pop()
        self.assertEqual(self.list.len(), 0)
    def test_delete(self):
        self.assertEqual(self.list.delete(1), None)
        self.list.push(1)
        self.list.delete(0)
        self.assertEqual(str(self.list), '[1]')
        self.list.push(2)
        self.list.push(3)
        self.list.delete(1)
        self.assertEqual(str(self.list), '[2, 3]')
    def test_contains(self):
        self.assertEqual(self.list.contains(1), None)
        self.list.push(1)
        self.list.push(2)
        self.assertEqual(self.list.contains(3), False)
        self.assertEqual(self.list.contains(2), True)





if __name__ == '__main__':
        unittest.main()

