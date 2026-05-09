class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=None, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    def get_hours(self):
        if self.hours is None:
            if self.rest_days is None:
                return None
            return (7 - self.rest_days) * 8
        return self.hours

    def get_email(self):
        if not self.email:
            return f"{self.name}@email.com"
        return self.email

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        hrs = self.get_hours()
        return hrs * self.hourly_payment


e = EmployeeSalary("Timur", rest_days=2)
print(e.get_hours())       # (7-2)*8 = 40
print(e.get_email())       # ivan@email.com
print(e.salary())          # 40 * 400 = 16000

EmployeeSalary.set_hourly_payment(500)
print(e.salary())          # 40 * 500 = 20000
