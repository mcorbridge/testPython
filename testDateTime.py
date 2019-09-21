from datetime import datetime, timedelta


# todo: when I create the timesheet app, I need to know the start date and the end date (Monday - Sunday) of the week
# todo: where the timesheet is being submitted

class TestDateTime:

    def __init__(self):
        self.startProc = self.getStartProcess()
        print("******* init TestDateTime *******")
        self.days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        self.months = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November',
            'December')
        self.dateNow = None
        self.date_obj = None
        self.start_of_week = None
        self.end_of_week = None

    def getStartProcess(self):
        return datetime.now().microsecond

    def getEndProcess(self):
        return datetime.now().microsecond

    def getProcessTime(self):
        processTime = (self.getEndProcess() - self.startProc) / 1000
        return str(processTime) + " msec"

    def dateTimeFormatter(self, date, isDayName=True):
        year = date.year
        month = date.month
        day = date.day
        dayName = self.days[date.weekday()]
        monthName = self.months[date.month - 1]
        if isDayName:
            return str(year) + '-' + str(month) + '-' + str(day) + ' [' + dayName + ' ' + monthName + ' ' + str(
                day) + ', ' + str(year) + ']'
        else:
            return str(year) + '-' + str(month) + '-' + str(day)

    def getNow(self):
        self.dateNow = datetime.now()
        date_str = str(self.dateNow.year) + '-' + str(self.dateNow.month) + '-' + str(self.dateNow.day)
        self.date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    def showDateNow(self):
        return self.dateTimeFormatter(self.dateNow)

    def getStartOfWeek(self):
        self.start_of_week = self.date_obj - timedelta(days=self.date_obj.weekday())
        return self.dateTimeFormatter(self.start_of_week)

    def getEndOfWeek(self):
        self.end_of_week = self.start_of_week + timedelta(days=6)
        return self.dateTimeFormatter(self.end_of_week)


testDateTime = TestDateTime()
testDateTime.getNow()
print(testDateTime.showDateNow())
print(testDateTime.getStartOfWeek())
print(testDateTime.getEndOfWeek())



