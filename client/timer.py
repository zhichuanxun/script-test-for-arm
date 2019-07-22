from threading import Timer

class MyTimer:
    def __init__(self, time, job):
        self.timer = Timer(time, job)
    
    def start(self):
        self.timer.start()
        
    #TODO check


def TestJob(self):
    f = open('./test.txt', 'a')
    f.write("test.\n")
    f.close()