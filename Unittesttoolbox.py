import unittest


class TestStringMethonds(unittest.TestCase):

    def pos(numbers, self):
        numbers.sort()
        for n in numbers:
            if n < 0:
                numbers.remove(n)
        return numbers

    def test_something(self):
        test = [1, 4, 7, -2, -323, 5, 7, 3, 9, -3, -6, -2]
        result = [1, 3, 4, 5, 7, 7, 9]
        self.assertEqual(self.pos(test), result)

if __name__=='__main__':
    unittest.main()
