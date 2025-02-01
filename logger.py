# 11. Create a class `Logger` with a method `log(message)`. 
# Implement method overloading to log different message types (`error`, `warning`, `info`).
class Logger:
    def log(self,message,level="hi"):
        if level=='error':
            self.error_log(message)
        elif level=='warning':
            self.warning_log(message)
        elif level=='info':
            self.info_log(message)
        else:
            print("Unknown level of error")
    def error_log(self,message):
        print("ERROR MESSAGE>>>>...")
    def warning_log(self,message):
        print("WARNING MESSAGE>>>>")
    def info_log(self,message):
        print("welcome to the world....")
l = Logger()
l.log("This is an info message")  
l.log("This is a warning", "warning")
l.log("This is an error", "error")
l.log("This is an error", "info")