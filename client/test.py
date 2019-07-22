from runner import Runner
import sys


# paras = {
#     'appid': sys.argv[0],
#     'pw': sys.argv[1],
#     'tenant': sys.argv[2],
#     'location': sys.argv[3],
#     # TODO: find other way to check kubectl version

# }

custom = {
    'version': 'v1.15.0',
    'nodeCount': '1',
    'rgName': 'aksRG',
    'aksName': 'aksTest'
}

operation = {
    'name': 'Install aks cluster',
    'comment': 'install aks if user first apply the product',
    'steps': [
        {
            'name': 'login through azure service principal',
            'commands': [
                {
                    'do': 'whoami > test.txt',
                    'undo': 'ls'
                }
            ]
        }
    ]
}

Runner().run(operation)
