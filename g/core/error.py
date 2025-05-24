class GError(Exception):
    """Base class for all G errors."""
    def __init__(self, message):
        super().__init__(message)
        self.message = message
        pass

    def __str__(self):
        return f"{self.message}"

class GValueError(GError):
    """Exception raised for value errors."""
    def __init__(self, message):
        super().__init__(message)
    
    def __str__(self):
        return f"value error: {self.message}"

class GSyntaxError(GError):
    """Exception raised for syntax errors."""
    def __init__(self, message):
        super().__init__(message)
    
    def __str__(self):
        return f"syntax error: {self.message}"