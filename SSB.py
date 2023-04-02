#coding=utf-8
import os, sys, platform

os.system('rm -rf ArMam.so ArMam32.so')

try:
    if sys.argv[1]=='update':
        os.system('rm -rf ArMam.so ArMam32.so')
except:
    pass


bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('ArMam.so'):
        os.system('curl -L https://github.com/mohaghhjj/ArMam.git/executables/blob/main/ArMam.cpython-311.so?raw=true -o ArMam.so') 
        import ArMam
    else:
        import ArMam

elif bit == '32bit':
    if not os.path.isfile('ArMam32.so'):
        os.system('curl -L https://github.com/mohaghhjj/ArMam.git/executables/blob/main/ArMam32.cpython-311.so?raw=true -o ArMam32.so') 
        import ArMam32
    else:
        import ArMam32
