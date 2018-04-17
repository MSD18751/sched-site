import threading
import subprocess
import random

class throd(threading.Thread):
    def __init__(self):
        self.stdout = None
        self.stderr = None
        threading.Thread.__init__(self)

    def run(self):
        r1 = random.randint(1,10)
        print(r1)
        r2 = random.randint(1,10)
        cmd = "sleep %d" % r1
        p = subprocess.Popen(cmd.split(),
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        self.stdout, self.stderr = p.communicate()

if __name__ == "__main__":
    t1 = throd()
    t2 = throd()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(t1.stdout)
    print(t2.stdout)
