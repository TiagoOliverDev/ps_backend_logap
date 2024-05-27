from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
import jwt
from datetime import datetime, timedelta

from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import LoginData, UserCreate

class AuthService:
    def __init__(self, db: Session):
        """
        Initializes the AuthService with a database session and attaches a UserRepository.

        Args:
            db (Session): The SQLAlchemy session for database interaction.
        """
        self.user_repository = UserRepository(db)

    def authenticate(self, email: str, password: str) -> str:
        """
        Authenticate a user and return a JWT token if valid.

        Args:
            login_data (LoginData): The data used for authenticating the user.

        Returns:
            str: A JWT token if authentication is successful.

        Raises:
            SQLAlchemyError: If a database error occurs during the authentication process.
            ValueError: If authentication fails (incorrect email or password).
        """
        try:
            user = self.user_repository.find_by_email(email)
            if user is None or not user.check_password(password):
                raise ValueError("Incorrect email or password")
            return self.create_token(user.id)
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Authentication process failed due to database error: {e}")

    def create_token(self, user_id: int) -> str:
        """
        Create a JWT token for a given user ID.

        Args:
            user_id (int): The user's ID for whom the token is created.

        Returns:
            str: A JWT token.
        """
        payload = {
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        SECRET_KEY = "9ba263503b01ce2ef81f6641f504b45333aa0662183d0184db79d9e92ccef620" 
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    

    def create_user(self, user_data: UserCreate):
        return self.user_repository.create_user(user_data.email, user_data.password)
