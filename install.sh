sudo su
apt-get update
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login -u zhichuanxun@outlook.com -p qaz123qaz
touch test.txt
az group list > test.txt