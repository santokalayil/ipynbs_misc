import subprocess

# subprocess.run('dir', shell=True)

# subprocess.run(['dir'], shell=True, stdout=False)
# subprocess.run(['dir'], shell=True, stdout=True)
# out = subprocess.run(['dir'], shell=True, stdout=True); print(out)

# print(150*'=')
# print(out.returncode);# return return code if yes then 0 is outputed
# print(out.stdout)# std out shows none becz it is sent to console if we want to catch it put capture_output=True
# out = subprocess.run(['dir'], shell=True, capture_output=True); print(out.stdout) # it is binary if we want we need to dcode it
# print(150*'-'); print(out.stdout.decode('utf-8')) # decoded output
# or else do this
# out = subprocess.run('dir', shell=True, capture_output=True, text=True); print(out.stdout);  print(out.stderr) # if there is error
out = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, text=True); print(out.stdout) # redirects to subprocess.PIPE - same output as above

#with open('log.txt','w') as f: out = subprocess.run('dir', shell=True, stdout=f, text=True) # redriects out to a text file -- usefull for logging
#out = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, text=True); print(out.stdout)


