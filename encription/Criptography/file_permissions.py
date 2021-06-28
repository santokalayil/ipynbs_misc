#!/usr/bin/python3

# Simply include permissions integer in octal (works for both python 2 and python3):

import subprocess
import os

# subprocess.call(['chmod', '0444', 'path'])
# subprocess.call(["chmod", "a-w", "file/path"])


'''
755 means read and execute access for everyone and also write access for the owner of the file. 
When you perform chmod 755 filename command you allow everyone to read and execute the file, 
the owner is allowed to write to the file as well.
'''

permission = {
	'readonly4all': {
					'code': 0o444,
					'print': "Read Only For All",
					},
	'read_exec_all_writeonly4owner': { 
					'code': 0o755,
					'print': "Read & Execute to All and Write only to Owner",
					}
}


option = "read_exec_all_writeonly4owner"

for pyfile in [i for i in os.listdir() if i.endswith('.py')]:
	path = pyfile
	os.chmod(path, permission[option]['code'])


print(f"Permission changed to {permission[option]['print']}")
