import sys

def cmdLogging(func):
    def wrapper(self, *args, **kwargs):
        print(f'>>>execute command: {self.doCmd}')
        print('------------------------------------------')
    return wrapper




def reportError(opName, stepName, stepIndex, cmdIndex, cmdValue):
    sys.exit(1)
    print(f'Operation {opName} error\n at step {stepName}: {stepIndex}:{cmdIndex} \n command: {cmdValue}')