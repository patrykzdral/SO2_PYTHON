import subprocess

print("HELLO")

#output = subprocess.Popen(['python3', 'example.py', "TY KURWO","12"], stdout=subprocess.PIPE, shell=True)
#list = output.communicate()
#print(list)

print("read:")
proc = subprocess.Popen(['echo', '"to stdout"'],
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate()[1]
print ("\tstdout:", repr(stdout_value))