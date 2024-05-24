class ApplicationError(Exception):
    """Base class for all application-specific errors."""
    pass

class DatabaseOperationError(ApplicationError):
    """Exception raised for errors that occur during database operations."""
    def __init__(self, original_exception):
        self.original_exception = original_exception
        super().__init__(str(original_exception))

class NotFoundError(ApplicationError):
    """Exception raised when an entity is not found in the database."""
    def __init__(self, entity_name, entity_id):
        super().__init__(f"{entity_name} with ID {entity_id} not found")
        self.entity_name = entity_name
        self.entity_id = entity_id
