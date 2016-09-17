#Sample IPMI SOL scraping script using python-ipmi:
console_parts=[]
debug=0
child = pexpect.spawn (‘ipmitool -I lanplus -H <ipaddress> -U <username> -P <password> sol activate’)
child.expect ('SOL Session operational')
child.sendline ('\r')
child.expect('login')
child.sendline ('~.')
#print "debug> got console details:  ",child.before
console_parts=child.before.split("\n")
if(debug==1):
 for item in console_parts:
  print "got: ",item
host_name=console_parts.pop()
print "host name is: ",host_name
kernel_name=console_parts.pop()
kernel_name=console_parts.pop()
print "kernel name is: ",kernel_name
OS_name=console_parts.pop()
print "OS name is: ",OS_name
