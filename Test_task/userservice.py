import logging
from sqlalchemy import select
from models import Base, User
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler("log.txt"))

# Define the UserDTO model
class UserDTO(BaseModel):
    id: int
    name: str
    age: int


# Define the UserService class
class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, user_id):
        async with self.session.begin():
            result = await self.session.execute(
                select(User).where(User.id == user_id)
            )
            user = result.scalar_one_or_none()
            if user:
                return UserDTO(id=user.id, name=user.name, age=user.age)
            else:
                return None

    async def add(self, user: UserDTO):
        async with self.session.begin() as session:
            db_user = User(id=user.id, name=user.name, age=user.age)
            session.add(db_user)
            logging.info(f"Add user: {user.name}")
            await session.commit()
