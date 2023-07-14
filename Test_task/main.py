import logging
import asyncio
import unittest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base
from hashmap import HashMap
from userservice import UserService, UserDTO
from test_hashmap import TestHashMap
from test_userservice import TestUserService

# Configure logging
def configure_logging():
    log_file_path = "log.txt"
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    logging.basicConfig(level=logging.DEBUG, format=log_format)

    # Add file handler to the root logger
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(logging.Formatter(log_format))
    logging.getLogger().addHandler(file_handler)

configure_logging()

async def setup_database():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, future=True)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return async_session
async def main():
    print("===TASK 1===")
    # Create an instance of HashMap
    hash_map = HashMap()

    hash_map.put("key1", "value1")
    hash_map.put("key2", "value2")
    print(hash_map.get("key1"))  # Output: value1
    print(hash_map.get("key2"))  # Output: value2
    print(hash_map.get("key3"))  # Output: None

    print("===TASK 2===")
    # Set up the database connection
    async_session = await setup_database()
    # Create an instance of UserService
    user_service = UserService(async_session)

    # Test the UserService class
    user = UserDTO(id=1, name="John", age=25)
    await user_service.add(user)
    retrieved_user = await user_service.get(1)
    if retrieved_user:
        print(retrieved_user.name, retrieved_user.age)  # Output: John 25

    # Close the database session
    await async_session.close()

    # Run the tests
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestHashMap))
    test_suite.addTest(unittest.makeSuite(TestUserService))
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

# Run the main coroutine
asyncio.run(main())

