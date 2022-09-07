from subprocess import Popen, PIPE
command = r"cmd"
p = Popen(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
usertext = "python script.py english день \n"
out, err = p.communicate(usertext)
print(out)
