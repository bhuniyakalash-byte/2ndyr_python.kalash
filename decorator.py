def decorator(function):
    def wrapper(*args, **kwargs):
        print("*" * 20)
        function(*args, **kwargs)
        print("*" * 20)
    return wrapper


class Report:
    template = "New Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return (
            f"Template: {self.template}\n"
            f"Title: {self.title}\n"
            f"Content: {self.content}"
        )

    @decorator
    def show_report(self):
        print(self)


Report.change_template("Student Report")
r1 = Report("The 48 laws of Power", "self help")
r1.show_report()