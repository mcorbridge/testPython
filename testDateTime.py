from datetime import datetime, timedelta

# todo: when I create the timesheet app, I need to know the start date and the end date (Monday - Sunday) of the week where
# todo: the timesheet is being submitted

class TestDateTime:

    def __init__(self):
        print("init TestDateTime")
        self.days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        self.months = (
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
        'December')
        self.now = datetime.now()
        self.start_of_week = ""
        self.end_of_week = ""

    def dateTimeFormatter(self, date,isDayName=True):
        year = date.year
        month = date.month
        day = date.day
        dayName = self.days[date.weekday()]
        monthName = self.months[date.month-1]
        if isDayName:
            return str(year) + '-' + str(month) + '-' + str(day) + ' [' + dayName + ' ' + monthName + ' ' + str(day) + ', ' + str(year) + ']'
        else:
            return str(year) + '-' + str(month) + '-' + str(day)

    def getNow(self):
        return self.dateTimeFormatter(self.now)

    def getStartOfWeek(self):
        self.start_of_week = datetime.strptime(self.dateTimeFormatter(self.now, False), '%Y-%m-%d')
        return self.dateTimeFormatter(self.start_of_week)

    def getEndOfWeek(self):
        self.end_of_week = self.start_of_week + timedelta(days=6)
        return self.dateTimeFormatter(self.end_of_week)

testDateTime = TestDateTime()
print(testDateTime.getNow())
print(testDateTime.getStartOfWeek())
print(testDateTime.getEndOfWeek())




