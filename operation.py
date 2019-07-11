from runner import Runner
import sys


paras = {
    'appid': sys.argv[0],
    'pw': sys.argv[1],
    'tenant': sys.argv[2],
    'location': sys.argv[3],
    # TODO: find other way to check kubectl version

}

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
            'name': 'install azure cli',
            'commands': [
                {
                    'do': 'sudo apt-get update',
                    'undo': ''
                },
                {
                    'do': 'sudo curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash ',
                    'undo': ''
                }
            ]
        },
        {
            'name': 'login through azure service principal',
            'commands': [
                {
                    'do': f'az login --service-principal -u {paras["appid"]} -p {paras["pw"]}  --tenant {paras["tenant"]}',
                    # retry if login failure
                    'undo': 'ls'
                }
            ]
        },
        {
            'name': 'create aks resource group',
            'commands': [
                {
                    'do': f'az group create --name {custom["rgName"]} --location {paras["location"]}',
                    'undo': f'az group delete --name {custom["rgName"]}  --no-wait'
                }
            ]
        },
        {
            'name': 'download kubectl',
            'commands': [
                {
                    'do': f'sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/{custom["version"]}/bin/linux/amd64/kubectl',
                    'undo': 'rm ./kubectl'
                },
                {
                    'do': 'chmod +x ./kubectl',
                    'undo': ''
                },
                {
                    'do': 'sudo mv ./kubectl /usr/local/bin/kubectl',
                    'undo': 'rm /usr/local/bin/kubectl'
                }
            ]
        },
        {
            'name': 'create aks cluster',
            'commands': [
                {
                    'do': f'az aks create --resource-group {custom["rgName"]}  --name {custom["aksName"]}  --node-count {custom["nodeCount"]} --enable-addons monitoring --service-principal {paras["appid"]} --client-secret {paras["pw"]} --generate-ssh-keys',
                    # TODO
                    'undo': ''
                }
            ]
        },
        {
            'name': 'config credentials',
            'commands': [
                {
                    'do': f'az aks get-credentials --resource-group {custom["rgName"]}  --name {custom["aksName"]} ',
                    'undo': ''
                }
            ]
        },
    ]
}

Runner().run(operation)
