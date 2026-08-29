# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TrainingDeck
import unittest


class TestTrainingDeck(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)
        self.assertEqual(0 + 0, 0)
        self.assertEqual(-3 + 3, 0)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)
        self.assertEqual(10 - 10, 0)
        self.assertEqual(0 - 5, -5)

    def test_multiplication(self):
        self.assertEqual(3 * 4, 12)
        self.assertEqual(0 * 100, 0)
        self.assertEqual(-2 * -2, 4)

    def test_division(self):
        self.assertEqual(8 / 2, 4.0)
        self.assertEqual(10 / 5, 2.0)
        with self.assertRaises(ZeroDivisionError):
            1 / 0

    def test_string_operations(self):
        self.assertEqual("hello" + " " + "world", "hello world")
        self.assertTrue("python" in "python is great")
        self.assertEqual("  text  ".strip(), "text")

    def test_list_operations(self):
        lst = [1, 2, 3]
        lst.append(4)
        self.assertEqual(lst, [1, 2, 3, 4])
        self.assertEqual(len([1, 2, 2, 3]), 4)
        self.assertIn(2, [1, 2, 3])

    def test_dict_operations(self):
        d = {"a": 1, "b": 2}
        d["c"] = 3
        self.assertEqual(d, {"a": 1, "b": 2, "c": 3})
        self.assertIn("a", d)
        self.assertEqual(d["a"], 1)

    def test_string_methods(self):
        self.assertEqual("HELLO".lower(), "hello")
        self.assertEqual("hello".upper(), "HELLO")
        self.assertEqual("hello world".split(), ["hello", "world"])


if __name__ == "__main__":
    unittest.main()
