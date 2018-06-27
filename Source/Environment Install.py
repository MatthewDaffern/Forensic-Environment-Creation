Write a bash script using the below to move python to another environment along with an IDLE install


$ curl -F "file=@test.txt" https://file.io
{"success":true,"key":"2ojE41","link":"https://file.io/2ojE41","expiry":"14 days"}
$ curl https://file.io/2ojE41 
This is a test
$ curl https://file.io/2ojE41
{"success":false,"error":404,"message":"Not Found"}



def environment install
import subprocess
run=subprocess.run
list_of_tools=[
	'https://1.na.dl.wireshark.org/win64/Wireshark-win64-2.6.1.exe',
	'https://www.winitor.com/tools/pestudio/current/pestudio.zip',
	'https://download.sysinternals.com/files/ProcessExplorer.zip',
	'https://download.sysinternals.com/files/ProcessMonitor.zip',
	'https://github.com/fireeye/flare-fakenet-ng/releases/download/1.3/fakenet1.3.zip',
	'http://www.angusj.com/resourcehacker/rshacker_setup.exe',
	'https://sourceforge.net/projects/regshot/files/latest/download'
]

for i in list_of_tools:
	command="microsoft-edge"+":"+list_of_tools[i]
	run(command)
#examine for list of zips
#extract those zips
#copy the folder to the desktop
#exit cleanly
return #list of applications