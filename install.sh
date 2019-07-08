sudo su
apt-get update
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login --identity
touch test.txt
az group list > test.txt