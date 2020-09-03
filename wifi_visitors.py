import subprocess

ip = "192.168.1.102"
person = "192.168.1.102:"


proc = subprocess.Popen(["ping", ip], stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    print(line)
    if not line:
        break
    connected_ip = line.decode('utf-8').split()[3]

    if connected_ip == person:
        subprocess.Popen(["say", "Person is on the network"])
        break
