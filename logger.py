from spike import PrimeHub
import hub as rawhub
hub = PrimeHub()

class Logger(object):
    def __init__(self):
        self.current_row=1
        self.current_col=1
        self.reset()

    def log_step(self,text):
        if DEBUG:
            print("Step '{}'".format(text))
        hub.light_matrix.set_pixel(self.current_col, self.current_row)
        self.increment()

    def increment(self):
        self.current_col += 1        
        if self.current_col==5:
            self.current_col = 1
            self.current_row += 1

    def log_success(self):
        wait_for_ms(500)
        hub.light_matrix.show_image('YES')
        wait_for_ms(500)

    def reset(self):
        self.current_row=1
        self.current_col=1
        rawhub.display.clear()
