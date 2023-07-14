import asyncio
import unittest
import logging
from models import Base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from userservice import UserService, UserDTO

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("log.txt"))

async def setup_database():
    # Set up the database connection
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=True)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False, future=True)

    # Create the tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    return async_session

class TestUserService(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create the tables
        cls.async_session = None

    @classmethod
    async def asyncSetUpClass(cls):
        # Create the tables
        cls.async_session = await setup_database()

    def setUp(self):
        self.loop = asyncio.get_event_loop()

    async def add_user(self, user, user_service):
        try:
            await user_service.add(user)
        except:
            self.fail("Failed to add user.")

    async def get_user(self, user_id, user_service):
        result = await user_service.get(user_id)
        return result

    async def add_and_get(self, user, user_service):
        await self.add_user(user, user_service)
        return await self.get_user(user.id, user_service)

    async def asyncTearDownClass(cls):
        if cls.async_session is not None:
            await cls.async_session.close()

    def test_add_and_get(self):
        user = UserDTO(id=1, name="John", age=25)
        user_service = UserService(self.async_session)
        retrieved_user = self.loop.run_until_complete(self.add_and_get(user, user_service))
        self.assertEqual(retrieved_user.id, user.id)
        self.assertEqual(retrieved_user.name, user.name)
        self.assertEqual(retrieved_user.age, user.age)

    def test_add_duplicate_user(self):
        user = UserDTO(id=1, name="John", age=25)
        user_service = UserService(self.async_session)
        self.loop.run_until_complete(self.add_user(user, user_service))
        with self.assertRaises(Exception):
            self.loop.run_until_complete(self.add_user(user, user_service))

    def test_get_nonexistent_user(self):
        user_service = UserService(self.async_session)
        retrieved_user = self.loop.run_until_complete(self.get_user(999, user_service))
        self.assertIsNone(retrieved_user)

    def test_add_and_get_existing_user(self):
        user = UserDTO(id=1, name="John", age=25)
        user_service = UserService(self.async_session)
        self.loop.run_until_complete(self.add_user(user, user_service))
        retrieved_user = self.loop.run_until_complete(self.get_user(user.id, user_service))
        self.assertEqual(retrieved_user.id, user.id)
        self.assertEqual(retrieved_user.name, user.name)
        self.assertEqual(retrieved_user.age, user.age)

    def test_add_multiple_users(self):
        user1 = UserDTO(id=1, name="John", age=25)
        user2 = UserDTO(id=2, name="Alice", age=30)
        user_service = UserService(self.async_session)
        self.loop.run_until_complete(self.add_user(user1, user_service))
        self.loop.run_until_complete(self.add_user(user2, user_service))
        retrieved_user1 = self.loop.run_until_complete(self.get_user(user1.id, user_service))
        retrieved_user2 = self.loop.run_until_complete(self.get_user(user2.id, user_service))
        self.assertEqual(retrieved_user1.id, user1.id)
        self.assertEqual(retrieved_user1.name, user1.name)
        self.assertEqual(retrieved_user1.age, user1.age)
        self.assertEqual(retrieved_user2.id, user2.id)
        self.assertEqual(retrieved_user2.name, user2.name)
        self.assertEqual(retrieved_user2.age, user2.age)

if __name__ == "__main__":
    unittest.main()
