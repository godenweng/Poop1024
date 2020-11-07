import unittest


def fun(x):
    return x + 1


class MyTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("one term startup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("one term clean up")

    def setUp(self) -> None:
        print("prepare something")

    def tearDown(self) -> None:
        print("clean up and store data")

    def test1(self):
        print("run test1")
        self.assertEqual(fun(3), 4)

    @unittest.skip("not yet implemented")
    def testFoo(self):
        print("run test2")
        self.assertEqual(fun(2), 3)

    def test3(self):
        print("run test3")
        self.assertEqual(fun(0),1)

if __name__ == '__main__':
    unittest.main()