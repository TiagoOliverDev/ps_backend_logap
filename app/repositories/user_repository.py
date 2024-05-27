from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import User
from werkzeug.security import check_password_hash, generate_password_hash

class UserRepository:
    def __init__(self, db: Session):
        """
        Initializes the UserRepository with a database session.

        Args:
            db (Session): The SQLAlchemy session for database interaction.
        """
        self.db = db

    def find_by_email(self, email: str) -> User:
        """
        Retrieves a user by their email.

        Args:
            email (str): The email of the user to find.

        Returns:
            User: The found user instance, or None if no user is found.
        """
        try:
            return self.db.query(User).filter(User.email == email).one_or_none()
        except SQLAlchemyError as e:
            raise SQLAlchemyError(f"Failed to retrieve user due to: {e}")
    
    def create_user(self, email: str, password: str) -> User:
        """
        Creates a new user with the provided email and password.
        
        Args:
            email (str): The email address for the new user, must be unique.
            password (str): The user's password, which will be hashed for security.
        
        Returns:
            User: The newly created user object, saved to the database.
        
        Raises:
            ValueError: If a user with the provided email already exists.
            SQLAlchemyError: If there are database operation failures during creation.

        Description:
        - Checks for an existing user with the provided email. If found, raises a ValueError to prevent duplicates.
        - Hashes the provided password to ensure passwords are not stored as plain text.
        - Creates a new user instance, adds it to the database session, and commits the transaction.
        - If any database errors occur during commit, a rollback is executed to undo the transaction,
        and an SQLAlchemyError is raised.
        - The new user's state is refreshed from the database to ensure it contains all updated fields like auto-generated IDs.
        """
        existing_user = self.find_by_email(email)
        if existing_user:
            raise ValueError("A user with the given email already exists.")
        
        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        try:
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except SQLAlchemyError as e:
            self.db.rollback()
            raise SQLAlchemyError(f"Failed to create user due to: {e}")
