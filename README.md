## Project Tasks

This project involves the completion of two tasks: implementing a hashmap class and writing a small service class. Below is an overview of the tasks and their completion status.

✅ - **Completed**
❌- **Missing**
##
Task 1:
Implementation of the HashMap class with put, get, remove, keys, contains_key, values, and items methods: ✅ 
Tests for the HashMap class in test_hashmap.py: ✅ 
Notes with argumentation for the chosen implementation: ✅ 
##

Task 2:
Implementation of the UserService class with get and add methods: ✅ 
Tests for the UserService class in test_userservice.py: ✅ 
Notes with argumentation for the chosen implementation: ✅ 
##

#### Notes with argumentation for the chosen implementation:
### Task 1: Implement own hashmap class



- The chosen implementation uses a dictionary (`self.map`) to store key-value pairs, providing fast access to values based on their keys.
- The `put` method allows adding or updating a key-value pair in the hashmap by assigning the value to the corresponding key in the dictionary.
- The `get` method retrieves the value for a given key from the hashmap using the `get` method of the dictionary, which has an average time complexity of O(1).
- The `remove` method deletes a key-value pair from the hashmap using the `del` keyword, with an average time complexity of O(1).
- The `keys`, `values`, and `items` methods return lists of all keys, values, and key-value pairs in the hashmap, respectively. They utilize the corresponding dictionary methods, which have an average time complexity of O(1).
- The `contains_key` method checks if a given key exists in the hashmap using the `in` operator on the dictionary, with an average time complexity of O(1).

### Task 2: Write a small service class


- The chosen implementation of the `UserService` class utilizes an asynchronous SQLAlchemy session (`self.session`) for efficient and non-blocking database operations.
- The `get` method retrieves a user from the database based on the provided `user_id` using SQLAlchemy's `select` statement. It returns the result as a `UserDTO` object. If no user is found, it returns `None`.
- The `add` method adds a new user to the database by creating a `User` object based on the provided `UserDTO` and adding it to the session. The changes are committed asynchronously to the database using `await self.session.commit()`.
- The implementation follows the separation of concerns principle by encapsulating database operations within the `UserService` class.
- The chosen implementation supports efficient and non-blocking database operations through the use of an asynchronous session and async/await syntax.


