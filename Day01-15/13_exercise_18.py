# -*- coding: utf-8 -*-
import subprocess
import chardet

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# # print(chardet.detect(r))
# print('Exit code:', r)



print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(chardet.detect(output))
print(output.decode('GB2312'))
print('Exit code:', p.returncode)
