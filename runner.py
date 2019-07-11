import subprocess
import sys

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
           
            print(f'step {stepName} start')
            for cmdIndex, cmdValue in enumerate(commands):
                cmd = Command(cmdValue['do'], cmdValue['undo'])
                exitCode, output = cmd.doExecute()

                if exitCode:
                    if cmd.canUndo():
                        cmd.undoExecute()
                        retryCode, output = cmd.doExecute()
                        
                        if retryCode :
                            self.__reportError(opName,stepName, stepIndex, cmdIndex, cmdValue, output)
            
            print(f'step {stepName} complete')
            print('#########################')
                    
        

    def __reportError(self, opName, stepName, stepIndex, cmdIndex, cmdValue, output):
        sys.exit(1)
        print(f'Operation {opName} error\n at step {stepName}: {stepIndex}:{cmdIndex} \n command: {cmdValue} \n errormsg: {output}')




class Command:
    def __init__(self, doCmd, undoCmd):
        self.__doCmd = doCmd
        self.__undoCmd = undoCmd
        self.__canUndo = undoCmd == ''
    
    def doExecute(self):
        p = subprocess.Popen(self.__doCmd, shell=True)
        exitcode, output = p.communicate()
        return exitcode, output

    def undoExecute(self):
        p = subprocess.Popen(self.__undoCmd, shell=True)
        exitcode, output = p.communicate()
        return exitcode, output

    def canUndo(self):
        return self.__canUndo