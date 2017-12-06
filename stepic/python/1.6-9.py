import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):
    def append(self, arg):
        self.log(arg)
        super(LoggableList, self).append(arg)

list = LoggableList()
list.append(2)
