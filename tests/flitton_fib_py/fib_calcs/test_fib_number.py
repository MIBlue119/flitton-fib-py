from unittest import main, TestCase
from flitton_fib_py.fib_calcs.fib_number import recurring_fibonacci_number

# The main function is to run all tests
# We also rely on the TestCase class by writing our own test class that inherits TestCase


class RecurringFibNumberTest(TestCase):
    def test_zero(self):
        self.assertEqual(0,
            recurring_fibonacci_number(0)
        )
    
    def test_negative(self):
        self.assertEqual(None,
            recurring_fibonacci_number(number=-1)
        )
    
    def test_one(self):
        self.assertEqual(1,
            recurring_fibonacci_number(1)
        )
    
    def test_two(self):
        self.assertEqual(1,
            recurring_fibonacci_number(2)
        )

    def test_ten(self):
        self.assertEqual(55,
            recurring_fibonacci_number(10)
        )
if __name__ == "__main__":
    main()
    