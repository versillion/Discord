#!/usr/bin/python3
try:
	import requests
	import time
	import json
	import stdiomask
except ModuleNotFoundError:
	print ('You need to install module[s] ==> requests, stdiomask to run this script.')
	exit(1)
print ('Get token, wrote by Versillion [10AM::July-9-2020]')

username = input("Email => ")
password = stdiomask.getpass(mask='*')
print ('[+] Start time ==> [{}]'.format(time.time()))
session = requests.Session()
session.get('https://discord.com')
data = json.dumps({
	"captcha_key":"",
	"email":username,
	"login_source":"",
	"password":password,
	"undelete":"false"
})
headers = {
	'Content-Type': 'application/json',
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; ) Gecko/20100101 Firefox/65.0'
}
session.headers.update(headers)
data = session.post("https://discord.com/api/v6/auth/login", data=data)

try:
	print ('[+] Token ==> {}'.format(json.loads(data.text)['token']))
	print ('[+] Exit time ==> [{}]'.format(time.time()))
except KeyError:
	print ('Login failure')
