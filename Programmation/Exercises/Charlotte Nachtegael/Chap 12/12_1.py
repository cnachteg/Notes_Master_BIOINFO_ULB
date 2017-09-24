import time
class StopWatch(object):
    def __init__(self):
        self.start = time.time()
        self.stop = None
    def __repr__(self):
        s = "StopWatch({},{})".format(self.start, self.stop)
        return s
    def __str__(self):
        return self.__repr__()
    def get_start_time(self):
        return self.start
    def get_end_time(self):
        if self.stop is None:
            raise Exception
        return self.stop
    def start(self):
        self.start = time.time()
        self.stop = None
    def stop(self):
        self.stop = time.time()
    def get_elapsed_time(self):
        if self.stop is not None:
            res = self.stop-self.start
        else:
            res = time.time()-self.start
        return res



X = StopWatch()
print(X.__str__())
print(X.get_start_time())