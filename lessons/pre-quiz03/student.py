


class Student:

    name: str
    schedule: Dict[str, str]
    credit_hours: int
    full_time: bool

    def __init__(self, name: str, status: bool):
        self.name = name
        self.full_time = status
        self.credit_hours = 0
        self.schedule = {}