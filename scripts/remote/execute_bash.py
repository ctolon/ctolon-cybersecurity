import paramiko

hostname = "192.168.1.101"
username = "test"
password = "abc123"

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=hostname, username=username, password=password)
except:
    print("[!] Cannot connect to the SSH Server")
    exit()

# read the BASH script content from the file
bash_script = open("script.sh").read()
# execute the BASH script
stdin, stdout, stderr = client.exec_command(bash_script)
# read the standard output and print it
print(stdout.read().decode())
# print errors if there are any
err = stderr.read().decode()
if err:
    print(err)
# close the connection
client.close()