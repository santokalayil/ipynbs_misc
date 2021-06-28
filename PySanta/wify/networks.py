import subprocess

class network():
    def __init__(self,):
        self.net_info = self.info()
        self.networks = self.dict()
    def info(self):
        devices = subprocess.check_output('netsh wlan show network'.split())
        networks_info = devices.decode('ascii')
        self.net_info = networks_info
        return self.net_info
    def dict(self):
        ssid_list = [j.strip() for j in [i for i in self.net_info.split('\r')]]
        idx_ntwk = [idx for idx, ID in enumerate(ssid_list) if "SSID " in ID]
        networks = [ssid_list[i:i+4] for i in idx_ntwk]
        networks = [{i.split(' : ')[0].strip() : i.split(' : ')[1] for i in network if len(i.split(' : '))==2} \
                    for network in networks]
        self.networks = networks
        return self.networks
    def show_info(self):
        print(self.net_info)

if __name__ == '__main__':
    nw = network()
    nw.show_info()