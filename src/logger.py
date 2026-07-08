class Logger:
    def __init__(self, debug_mode=True):
        self.debug_mode = debug_mode

    def log(self, message):
        if self.debug_mode:
            print(message)

    def error(self, message):
        print(f"ERROR: {message}")
    