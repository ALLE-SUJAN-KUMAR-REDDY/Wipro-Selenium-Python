import paramiko

host ="localhost"
port = 22
username ="Sujan Kumar Reddy"
password ="Skr@199394"

# create an object and connect to remote machines

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=host,
    port = port,
    username = username,
    password = password
)

stdin, stdout, stderr = client.exec_command("whoami")

print(stdout.read().decode())

client.close()