import time

class Timer():
    def __init__(self):
        self.start =  int(round(time.time() * 1000))
        self.passed = 0
        self.duration = 0
        self.action = None
        self.done = False

    def cancel(self):
        self.done = True

    def update(self):
        if not self.done:
            current = int(round(time.time() * 1000))
            dt =  current - self.start
            self.start = current
            self.passed += dt
            if self.passed >= self.duration:
                self.action()
                self.cancel()

class RepeateTimer(Timer):
    def __init__(self):
        super().__init__()
    
    def update(self):
        if not self.done:
            current = int(round(time.time() * 1000))
            dt =  current - self.start
            self.start = current
            self.passed += dt
            if self.passed >= self.duration:
                self.action()
                self.passed = 0

class RepeateNTimer(Timer):
    def __init__(self):
        super().__init__()
        self.ntimes = 0
        self.executions = 0
    
    def update(self):
        if not self.done and self.executions < self.ntimes:
            current = int(round(time.time() * 1000))
            dt =  current - self.start
            self.start = current
            self.passed += dt
            if self.passed >= self.duration:
                self.action()
                self.passed = 0
                self.executions += 1
                if self.executions >= self.ntimes:
                    self.cancel()

if __name__ == "__main__":

    def do1():
        print("Repeate once")

    def do2():
        print("Repeate forever")

    def do3():
        print("Repeate 3 times")


    timers = []

    t1 = Timer(3000, do1)
    t2 = RepeateTimer(3000,do2)
    t3 = RepeateNTimer(3000, 3, do3)

    timers.append(t1)
    timers.append(t2)
    timers.append(t3)

    done = 0

    while done < 3:
        for t in timers:
            t.update()
        timers = [t for t in timers if not t.done]
   
    
    