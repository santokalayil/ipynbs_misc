import subprocess, json

class Wify():
    def __init__(self, ):
        #self.profiles = self.find_profiles()
        #self.passwords = self.find_passwords()
        #self.save_result()
        self.profiles = None
        self.passwords = None
    
    def find_profiles(self,):
        output = subprocess.check_output('netsh wlan show profiles'.split())
        output = output.decode('utf-8')
        profiles = [p.strip() for p in [o for o in output.split('User profiles\r\n-------------\r\n    ')][1]
                    .split('All User Profile     : ')]
        self.profiles = [p for p in profiles if p != '']
        return self.profiles
    
    def profile_info(self, profile):
        try:
            cmd_list = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
            output = subprocess.check_output(cmd_list)
            output = output.decode('utf-8').replace('\r','')
        except:
            output = None
        return output
    
    def find_passwords(self):
        d = {}
        for profile in self.profiles:
            output = self.profile_info(profile)
            if output is not None:
                d.update({profile:[line.split(': ')[1] for line in output.split('\n') if 'Key Content' in line][0]})
        self.passwords = d
        return self.passwords
    def save_result(self):
        file_name = 'results.txt'
        with open('results.json', 'w') as f:
            json.dump(self.passwords, f)

    def ipconfig(self,):
        out = subprocess.check_output(['ipconfig','/all'])
        with open('ipconfig.cfg', 'wb') as f:
            f.write(out)


if __name__ == '__main__':
    wf = Wify()
    wf.find_profiles()
    wf.find_passwords()
    wf.save_result()
    wf.ipconfig()
    print('Success')
    #input('')