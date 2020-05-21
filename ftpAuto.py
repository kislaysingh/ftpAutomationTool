#!/usr/bin/env python
import pexpect as px
id = px.spawn('ftp 192.168.15.60')
id.expect_exact('Name')
id.sendline('msfadmin')
id.expect_exact('Password')
id.sendline('msfadmin')
id.expect_exact('ftp')
id.sendline('ls')


for line in id.before.split('\n'.encode()) :
	print (line.decode())
