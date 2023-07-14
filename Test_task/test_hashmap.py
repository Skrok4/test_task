import unittest
import logging
from hashmap import HashMap

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("log.txt"))

# Tests for the HashMap class
class TestHashMap(unittest.TestCase):
    def setUp(self):
        self.map = HashMap()

    def test_put_and_get(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.assertEqual(self.map.get("key1"), "value1")
        self.assertEqual(self.map.get("key2"), "value2")
        self.assertIsNone(self.map.get("key3"))

    def test_remove(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.map.remove("key1")
        self.assertIsNone(self.map.get("key1"))
        self.assertEqual(self.map.get("key2"), "value2")

    def test_contains_key(self):
        self.map.put("key1", "value1")
        self.assertTrue(self.map.contains_key("key1"))
        self.assertFalse(self.map.contains_key("key2"))

    def test_keys(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.assertCountEqual(self.map.keys(), ["key1", "key2"])
        self.map.remove("key1")
        self.assertCountEqual(self.map.keys(), ["key2"])
        self.map.remove("key2")
        self.assertCountEqual(self.map.keys(), [])

    def test_values(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.assertCountEqual(self.map.values(), ["value1", "value2"])
        self.map.remove("key1")
        self.assertCountEqual(self.map.values(), ["value2"])
        self.map.remove("key2")
        self.assertCountEqual(self.map.values(), [])

    def test_items(self):
        self.map.put("key1", "value1")
        self.map.put("key2", "value2")
        self.assertCountEqual(self.map.items(), [("key1", "value1"), ("key2", "value2")])
        self.map.remove("key1")
        self.assertCountEqual(self.map.items(), [("key2", "value2")])
        self.map.remove("key2")
        self.assertCountEqual(self.map.items(), [])

if __name__ == "__main__":
    unittest.main()