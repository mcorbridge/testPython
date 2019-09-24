

import calendar
import testingMain
import singleton

s = singleton.Singleton.getInstance()

t = 4+6
print(s.foo + '{' + str(t) + "}")

class TestCalendar:

    def __init__(self):
        print("init TestCalendar")
        print("[" + s.foo + "]")


    def makeMonth(self):
        c = calendar.TextCalendar(calendar.SUNDAY)
        str = c.formatmonth(2019, 9)
        print(str)

    def htmlCalendar(self):
        c = calendar.HTMLCalendar(calendar.SUNDAY)
        str = c.formatmonth(2019, 9)
        print(str)

    def testCalendar(self):
        print(calendar.calendar(2019, 2, 1, 6))

    def testItermonthdates(self):
        obj = calendar.Calendar()
        # iteratign with itermonthdates
        for day in obj.itermonthdates(2019, 9):
            print(day)

    def testMonthdayscalendar(self):
        import calendar
        obj = calendar.Calendar()

        # iteratign with monthdayscalendar
        for day in obj.monthdayscalendar(2019, 9):
            print(day)
        print('-------------------------------')
        print(obj.monthdayscalendar(2019, 9)[0])
        print(obj.monthdayscalendar(2019, 9)[1])
        print(obj.monthdayscalendar(2019, 9)[2])
        print(obj.monthdayscalendar(2019, 9)[3])
        print(obj.monthdayscalendar(2019, 9)[4])
        print(obj.monthdayscalendar(2019, 9)[5])


testCalendar = TestCalendar()
testCalendar.makeMonth()
testCalendar.htmlCalendar()
testCalendar.testCalendar()
testCalendar.testItermonthdates()
testCalendar.testMonthdayscalendar()