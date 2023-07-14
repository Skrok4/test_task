import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("log.txt"))

class HashMap:
    def __init__(self):
        self.map = {}
    def put(self, key, value):
        """
        Put a key-value pair into the HashMap.
        """
        self.map[key] = value
        logging.info(f"Put: {key} => {value}")


    def get(self, key):
        """
        Retrieve the value for the given key from the HashMap.
        Returns None if the key is not found.
        """
        value = self.map.get(key)
        logging.info(f"Get: {key} => {value}")
        return value

    def remove(self, key):
        """
       Remove the key-value pair for the given key from the HashMap.
       """
        if key in self.map:
            del self.map[key]
            logging.info(f"Remove: {key}")

    def keys(self):
        """
        Get a list of all keys in the HashMap.
        """
        return list(self.map.keys())

    def contains_key(self, key):
        """
        Check if the HashMap contains the given key.
        Returns True if the key is found, False otherwise.
        """
        return key in self.map

    def values(self):
        """
        Get a list of all values in the HashMap.
        """
        return list(self.map.values())

    def items(self):
        """
        Get a list of all key-value pairs in the HashMap.
        """
        return list(self.map.items())
