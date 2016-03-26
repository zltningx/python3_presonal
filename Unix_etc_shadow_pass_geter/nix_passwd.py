#!/usr/bin/env python
# coding=utf-8

import crypt
import sys
from concurrent.futures import ThreadPoolExecutor

def testpasswd(crypt_pass):
    salt = crypt_pass.split('$')[2]
    insalt = '${}${}$'.format('6',salt)
    with open(sys.argv[2],'r') as dict_file:
        for word in dict_file:
            word = word.strip('\n')
            crypt_word = crypt.crypt(word,insalt)
            if crypt_pass == crypt_word:
                print ("[+] Found Password: {}\n".format(word))
                return
    print ("[-]No Found {} ")
    return

def readpasswd():
    with open(sys.argv[1],'r') as passwd_file:
        for line in passwd_file:
            if ":" in line:
                user = line.split(':')[0]
                crypt_pass = line.split(':')[1].strip(' ')
                if len(crypt_pass) > 16:
                    print ("[*] Cracking Password For : {}".format(user))
                    with ThreadPoolExecutor(2) as Executor:
                        Executor.submit(testpasswd,crypt_pass)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print ("Usage:\n\t请准备好阴影文件和爆破字典\n\t如: ./nix_passwd.py password.txt dict.txt")
        sys.exit(0)
    readpasswd()
