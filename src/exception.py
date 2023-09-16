class InstantiateCSVError(Exception):
    """
    Класс-исключение на случай, если файл csv поврежден
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
