import subprocess
import sys
from logs import *

class Runner:
    def __init__(self):
        pass
    
    def run(self, operation):
        opName = operation['name']
        steps = operation['steps']
        
        # TODO: record last success postion and skip if restart
        for stepIndex, step in enumerate(steps):
            stepName = step['name']
            commands = step['commands']
           
            print(f'step: {stepName} start')
            print('#########################')
            for cmdIndex, cmdValue in enumerate(commands):
                cmd = Command(cmdValue['do'], cmdValue['undo'])
                exitCode = cmd.doExecute()

                if exitCode:
                    if cmd.canUndo():
                        cmd.undoExecute()
                        retryCode = cmd.doExecute()
                        
                        if retryCode :
                            reportError(opName, stepName, stepIndex, cmdIndex, cmdValue['do'])


# TODO: implement a iterable Operation class to achieve a better encapsulating
# class Operation:
#     def __init__(self, opt):
#         self.opName = opt['name']
#         self.steps = opt['steps']
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):

    


class Command:
    def __init__(self, doCmd, undoCmd):
        self.doCmd = doCmd
        self.undoCmd = undoCmd
        self.canUndo = undoCmd == ''
    
    @cmdLogging
    def doExecute(self):
        p = subprocess.Popen(self.doCmd, shell=True)
        output = p.communicate()[0]
        return p.returncode, output

    def undoExecute(self):
        p = subprocess.Popen(self.undoCmd, shell=True)
        output = p.communicate()[0]
        return p.returncode, output

    