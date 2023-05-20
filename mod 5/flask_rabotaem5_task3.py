class BlockErrors:
    def __init__(self, error_types):
        self.error_types = error_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None and issubclass(exc_type, self.error_types):
            return True