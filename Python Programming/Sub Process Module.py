#Subprocess module -

# execute external system commands
# iterate with OS processess
# capture output , error and return codes
# control the process execution

# run the OS level commands - linux , macos, windows


import subprocess

# subprocess.run() - run command and wait
# subprocess.Popen() - run process asynchrously
# subprocess.PIPE - capture the output
# subprocess.TimeoutExpired - Time outexepction
# subprocess.CalledProcessError - command failure

result = subprocess.run("dir" , shell= True , capture_output=True, text = True)
print(result)

result = subprocess.run("ipconfig" , shell= True , capture_output=True, text = True)
print(result)

result = subprocess.run("python --version" , shell= True , capture_output=True, text = True)
print(result)
#print(result.stderr)


